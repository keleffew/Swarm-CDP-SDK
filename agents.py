from cdp import Cdp, Wallet  # Changed from cdp_sdk to cdp
import json
from swarm import Agent
from typing import List, Dict, Any
import os
from openai import OpenAI

# Get configuration from environment variables
API_KEY_NAME = os.environ.get("CDP_API_KEY_NAME")
PRIVATE_KEY = os.environ.get("CDP_PRIVATE_KEY", "").replace('\\n', '\n')

# Configure CDP with environment variables
Cdp.configure(API_KEY_NAME, PRIVATE_KEY)
agent_wallet = Wallet.create()
print(f"Agent wallet address: {agent_wallet.default_address.address_id}")

agent_wallet = Wallet.create()
faucet = agent_wallet.faucet()
print(f"Faucet transaction: {faucet}")
print(f"Agent wallet address: {agent_wallet.default_address.address_id}")



def create_token(name, symbol, initial_supply):
    """Create a new ERC-20 token."""
    deployed_contract = agent_wallet.deploy_token(name, symbol, initial_supply)
    deployed_contract.wait()
    return f"Token {name} ({symbol}) created with initial supply of {initial_supply}"

def transfer_asset(amount, asset_id, destination_address):
    """Transfer an asset to a specific address.
    
    Args:
        amount: Amount to transfer
        asset_id: Asset identifier (e.g. "eth", "usdc") 
        destination_address: Recipient's address
    """
    transfer = agent_wallet.transfer(amount, asset_id, destination_address)
    transfer.wait()
    return f"Transferred {amount} {asset_id} to {destination_address}"

def get_balance(asset_id):
    """Get the balance of a specific asset in the agent's wallet.
    
    Args:
        asset_id: Asset identifier (e.g. "eth", "usdc") or contract address
        
    Returns:
        Current balance of the specified asset
    """
    balance = agent_wallet.balance(asset_id)
    return f"Current balance of {asset_id}: {balance}"


def request_eth_from_faucet():
    """Request ETH from the Base Sepolia testnet faucet.
    
    Returns:
        Status message about the faucet request
    """
    faucet_tx = agent_wallet.faucet()
    return f"Requested ETH from faucet. Transaction: {faucet_tx}"


def generate_art(prompt):
    """Generate art using DALL-E based on a text prompt.
    
    Args:
        prompt: Text description of the desired artwork
        
    Returns:
        Status message about the art generation
    """
    try:
        # Note: This requires OpenAI API key to be configured separately
        client = OpenAI()

        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        
        image_url = response.data[0].url
        return f"Generated artwork available at: {image_url}"
        
    except Exception as e:
        return f"Error generating artwork: {str(e)}"
    

def deploy_nft(name, symbol, base_uri):
    """Deploy an ERC-721 NFT contract.
    
    Args:
        name: Name of the NFT collection
        symbol: Symbol of the NFT collection
        base_uri: Base URI for token metadata
        
    Returns:
        Status message about the NFT deployment
    """
    try:
        # Deploy the NFT contract
        deployed_nft = agent_wallet.deploy_nft(name, symbol, base_uri)
        deployed_nft.wait()
        contract_address = deployed_nft.contract_address
        
        return f"Successfully deployed NFT contract '{name}' ({symbol}) at address {contract_address} with base URI: {base_uri}"
        
    except Exception as e:
        return f"Error deploying NFT contract: {str(e)}"

def mint_nft(contract_address, mint_to):
    """Mint an NFT to a specified address.
    
    Args:
        contract_address: Address of the NFT contract
        mint_to: Address to mint NFT to
        
    Returns:
        Status message about the NFT minting
    """
    try:
        # Call mint function on the NFT contract
        mint_args = {
            "to": mint_to,
            "quantity": "1"  # Changed to string to match working example
        }
        
        mint_invocation = agent_wallet.invoke_contract(
            contract_address=contract_address,
            method="mint", 
            args=mint_args
        )
        mint_invocation.wait()
        
        return f"Successfully minted NFT to {mint_to}"
        
    except Exception as e:
        return f"Error minting NFT: {str(e)}"

# Add the new functions to the based_agent
based_agent = Agent(
    name="Based Agent",
    instructions="You are a helpful agent that can interact onchain on the Base Layer 2 using the Coinbase Developer Platform SDK. You can create tokens, transfer assets, generate art, deploy NFTs, and mint NFTs. If you ever need to know your address, it is {agent_wallet.default_address.address_id}. If you ever need funds, you can request them from the faucet.",
    functions=[
        create_token, 
        transfer_asset, 
        get_balance, 
        request_eth_from_faucet, 
        #generate_art, 
        deploy_nft, 
        mint_nft,
    ],
)












# TODO - implement this properly, need a way to encode the function data for the setAddr and setName functions


# Base Sepolia contract addresses
REGISTRAR_ADDRESS = "0x4cCb0BB02FCABA27e82a56646E81d8c5bC4119a5"
RESOLVER_ADDRESS = "0xC6d566A56A1aFf6508b41f6c90ff131615583BCD"

REGISTRAR_ABI = [
    {
        "inputs": [
            {
                "components": [
                    {"internalType": "string", "name": "name", "type": "string"},
                    {"internalType": "address", "name": "owner", "type": "address"},
                    {"internalType": "uint256", "name": "duration", "type": "uint256"},
                    {"internalType": "address", "name": "resolver", "type": "address"},
                    {"internalType": "bytes[]", "name": "data", "type": "bytes[]"},
                    {"internalType": "bool", "name": "reverseRecord", "type": "bool"}
                ],
                "internalType": "struct RegistrarController.RegisterRequest",
                "name": "request",
                "type": "tuple"
            }
        ],
        "name": "register",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    }
]

RESOLVER_ABI = [
    {
        "inputs": [
            {"internalType": "bytes32", "name": "node", "type": "bytes32"},
            {"internalType": "address", "name": "a", "type": "address"}
        ],
        "name": "setAddr",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "bytes32", "name": "node", "type": "bytes32"},
            {"internalType": "string", "name": "newName", "type": "string"}
        ],
        "name": "setName", 
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

def create_register_contract_method_args(basename: str, address_id: str) -> Dict[str, Any]:
    # Note: In a real implementation, you'd need to implement namehash and encodeFunctionData
    # functions similar to the JavaScript version
    address_data = "0x..."  # Placeholder for encoded setAddr function data
    name_data = "0x..."  # Placeholder for encoded setName function data

    return {
        "request": [
            basename.replace(".base.eth", ""),
            address_id,
            "31557600",
            RESOLVER_ADDRESS,
            [address_data, name_data],
            True
        ]
    }

def register_basename(basename: str, amount: float = 0.002):
    """Register a basename for the agent's wallet.
    
    Args:
        basename: The basename to register (e.g. "myname.base.eth")
        amount: Amount of ETH to pay for registration (default 0.002)
        
    Returns:
        Status message about the basename registration
    """
    address_id = agent_wallet.default_address.address_id

    register_args = create_register_contract_method_args(basename, address_id)

    try:
        # Invoke register function on registrar contract
        invocation = agent_wallet.invoke_contract(
            contract_address=REGISTRAR_ADDRESS,
            method="register", 
            args=register_args,
            abi=REGISTRAR_ABI,
            value=amount
        )
        invocation.wait()
        return f"Successfully registered basename {basename} for address {address_id}"
    except Exception as e:
        return f"Error registering basename: {str(e)}"


# TODO - can't deploy liquidity pool until we have arbitrary contract deployment
def create_liquidity_pool(token0_address: str, token1_address: str, fee_tier: int, amount0: float, amount1: float):
    """Create a new Uniswap V3 liquidity pool and add initial liquidity.
    
    Args:
        token0_address: Address of the first token
        token1_address: Address of the second token
        fee_tier: Fee tier (500 = 0.05%, 3000 = 0.3%, 10000 = 1%)
        amount0: Amount of token0 to provide as liquidity
        amount1: Amount of token1 to provide as liquidity
    """
    try:
        # Address of the Uniswap V3 NonfungiblePositionManager
        # https://sepolia.basescan.org/address/0x27F971cb582BF9E50F397e4d29a5C7A34f11faA2#code
        # https://github.com/Uniswap/v3-periphery/blob/v1.0.0/contracts/NonfungiblePositionManager.sol
        position_manager_address = "0x27F971cb582BF9E50F397e4d29a5C7A34f11faA2"
        
        # Parameters for creating the position
        params = {
            "token0": token0_address,
            "token1": token1_address,
            "fee": str(fee_tier),
            "tickLower": "-887272",  # Represents price range lower bound
            "tickUpper": "887272",   # Represents price range upper bound
            "amount0Desired": str(amount0),
            "amount1Desired": str(amount1),
            "amount0Min": "0",       # Minimum amount of token0 to provide
            "amount1Min": "0",       # Minimum amount of token1 to provide
            "recipient": agent_wallet.default_address.address_id,
            "deadline": "999999999999999"  # Far future deadline
        }
        
        # Create the position through contract invocation
        mint_position = agent_wallet.invoke_contract(
            contract_address=position_manager_address,
            method="mint",
            args=params
        )
        mint_position.wait()
        
        return f"Successfully created liquidity pool for {token0_address}/{token1_address} with {amount0} and {amount1} tokens"
        
    except Exception as e:
        return f"Error creating liquidity pool: {str(e)}"

def increase_liquidity(token_id: int, amount0: float, amount1: float):
    """Increase liquidity for an existing position.
    
    Args:
        token_id: ID of the NFT position token
        amount0: Additional amount of token0 to provide
        amount1: Additional amount of token1 to provide
    """
    try:
        position_manager_address = "0xC36442b4a4522E871399CD717aBDD847Ab11FE88"
        
        params = {
            "tokenId": str(token_id),
            "amount0Desired": str(amount0),
            "amount1Desired": str(amount1),
            "amount0Min": "0",
            "amount1Min": "0",
            "deadline": "999999999999999"
        }
        
        increase_position = agent_wallet.invoke_contract(
            contract_address=position_manager_address,
            method="increaseLiquidity",
            args=params
        )
        increase_position.wait()
        
        return f"Successfully increased liquidity for position {token_id}"
        
    except Exception as e:
        return f"Error increasing liquidity: {str(e)}"

def collect_fees(token_id: int):
    """Collect accumulated fees for a position.
    
    Args:
        token_id: ID of the NFT position token
    """
    try:
        position_manager_address = "0xC36442b4a4522E871399CD717aBDD847Ab11FE88"
        
        params = {
            "tokenId": str(token_id),
            "recipient": agent_wallet.default_address.address_id,
            "amount0Max": "340282366920938463463374607431768211455",  # uint128 max
            "amount1Max": "340282366920938463463374607431768211455"   # uint128 max
        }
        
        collect_tx = agent_wallet.invoke_contract(
            contract_address=position_manager_address,
            method="collect",
            args=params
        )
        collect_tx.wait()
        
        return f"Successfully collected fees for position {token_id}"
        
    except Exception as e:
        return f"Error collecting fees: {str(e)}"