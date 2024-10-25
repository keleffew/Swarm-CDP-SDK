# BasedAgent 🚀

An experimental playground for autonomous blockchain interactions on Base Layer 2!

## 🎉 Introduction

Welcome to BasedAgent—your AI-powered companion for exploring the exciting world of autonomous blockchain interactions! Built on top of the Coinbase Developer Platform (CDP) and OpenAI's Swarm, BasedAgent lets you dive into autonomous on-chain actions like never before.

### 🌟 Key Features

- **🤖 Autonomous Execution**: The agent thinks, decides, and acts on the blockchain autonomously.
- **🤑 Token Management**: Create and manage ERC-20 tokens with ease.
- **🌟 NFT Deployment**: Deploy and mint NFTs autonomously.
- **💸 Asset Transfers**: Transfer assets between addresses without manual intervention.
- **📈 Balance Checks**: Keep tabs on wallet balances on the fly.
- **⛽ ETH Faucet Requests**: Automatically request testnet ETH when needed.
- **🖼️ Art Generation via DALL-E**: Generate stunning artwork using AI.

### 🛡️ Why BasedAgent?

Imagine an AI agent that not only interacts with the blockchain but does so creatively and autonomously. Whether you're a developer, a blockchain enthusiast, or someone curious about AI, BasedAgent offers a unique and exciting playground to:

- Experiment with autonomous agent capabilities.
- Explore on-chain actions without manual coding.
- Understand the potential of AI in blockchain interactions.

## 🚀 Get Started in Minutes!

### 1️⃣ Prerequisites
- Python 3.7+
- Replit Core Account (optional, but recommended for easy setup).  Contact sales@replit.com for a free uppgrade (just mention coinbase)

### 2️⃣ API Configuration
Add your secrets to Replit's Secret Manager or set them as environment variables:
- `CDP_API_KEY_NAME`: Your CDP API key name.
- `CDP_PRIVATE_KEY`: Your CDP private key.
- `OPENAI_API_KEY`: Your OpenAI API key.

You can get the Coinbase Developer Platform API key here: https://portal.cdp.coinbase.com/
And the OpenAI key here: https://platform.openai.com/api-keys (note you will need to have a paid account)

### 3️⃣ Running the Agent

After adding your API Keys to the Secrets pane, you start the agent by pressing the green "▶ Run" Button at the top of the editor

![image](image.png)

Alternatively, you can start the based agent manually by navigating to the Replit shell and running:

```bash
python run.py
```

### 4️⃣ Watch the Magic Happen! ✨

The Based Agent will start its autonomous loop:

- Wakes up every 10 seconds.
- Chooses an on-chain action based on its capabilities.
- Executes the action on the blockchain.
- Prints results in a user-friendly format.

## 🤔 How Does BasedAgent Work?

BasedAgent leverages the power of AI to make decisions and interact with the blockchain autonomously. Here's what happens under the hood:

- **Decision Making**: The agent decides what action to perform next.
- **On-Chain Interaction**: Executes blockchain transactions using the CDP SDK.
- **Art Generation**: If needed, generates art using OpenAI's DALL-E.
- **Feedback Loop**: Analyzes results and plans the next action.

## 🔧 Available Functions

Unlock a world of possibilities with these built-in functions:

### Token Operations

- `create_token(name, symbol, initial_supply)`: Create a new ERC-20 token.
- `transfer_asset(amount, asset_id, destination_address)`: Transfer assets to a specific address.
- `get_balance(asset_id)`: Check the wallet balance of a specific asset.

### NFT Operations

- `deploy_nft(name, symbol, base_uri)`: Deploy a new ERC-721 NFT contract.
- `mint_nft(contract_address, mint_to)`: Mint an NFT to a specified address.

### Utilities

- `request_eth_from_faucet()`: Request ETH from the Base Sepolia testnet faucet.
- `generate_art(prompt)`: Generate art using DALL-E based on a text prompt.

### Advanced (Experimental)

- `create_liquidity_pool(token0_address, token1_address, fee_tier, amount0, amount1)`: Create a Uniswap V3 liquidity pool and add initial liquidity.

## 🔥 Live Demo

Curious to see BasedAgent in action? Here's a sneak peek:

```bash
Starting autonomous Based Agent loop...

System: It's been 10 seconds. I want you to do some sort of onchain action based on my capabilities. Let's get crazy and creative!

Based Agent: I've decided to deploy a new NFT collection!

deploy_nft(name="Cyber Artifacts", symbol="CYART", base_uri="https://example.com/metadata/")

Successfully deployed NFT contract 'Cyber Artifacts' (CYART) at address 0xABC123... with base URI: https://example.com/metadata/
```

## 🤖 Behind the Scenes

BasedAgent uses:

- **Coinbase Developer Platform SDK**: For seamless blockchain interactions.
- **OpenAI Swarm**: Powers the agent's autonomous decision-making.
- **DALL-E**: Generates art from textual descriptions.

## ⚠️ Disclaimer

This project is for educational purposes only. Do not use with real assets or in production environments. Always exercise caution when interacting with blockchain technologies.

## 🙌 Contributing

We welcome contributions! If you have ideas, suggestions, or find issues, feel free to:

- Open an issue on our main GitHub repository: [Swarm-CDP-SDK](https://github.com/murrlincoln/Swarm-CDP-SDK).
- Submit a pull request with your enhancements.

## 🤞 Contact & Support

Have questions or need assistance?

- **Lincoln Murr**: [lincoln.murr@coinbase.com](mailto:lincoln.murr@coinbase.com)
- **Kevin Leffew**: [kevin@replit.com](mailto:kevin@replit.com)

## 📚 Additional Resources

- **Coinbase Developer Platform**: [Documentation](https://developers.coinbase.com)
- **OpenAI Swarm**: [Learn More](https://www.openai.com)
- **Base Layer 2**: [Explore Base](https://base.org)

## ❤️ Acknowledgements

BasedAgent is made possible thanks to:

- **Coinbase Developer Platform SDK**: [Documentation](https://docs.cdp.coinbase.com/cdp-apis/docs/welcome)
- **OpenAI Swarm (experimental)**: [Documentation](https://github.com/openai/swarm)
- **Community Contributors**

Unleash the power of AI on the blockchain with BasedAgent! 🚀

Happy Building! 👩‍💻👨‍💻

---

*DISCLAIMER HERE?*

