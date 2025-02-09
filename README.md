# TradeAlgoAVS

![TradeAlgoAVS Logo](./logo.png)

## Overview
<p align="center">
  <a href="https://www.agentic2025.com" target="_blank">
    <img src="partners/agentic2025.png" alt="Agentic 2025" width="150"/>
  </a>
</p>

**TradeAlgoAVS** is a hackathon project spawned at [EthGlobal's Agentic virtual hackathon](https://ethglobal.com/events/agents) in February 2025. TradeAlgoAVS or Agentic Trading is a decentralized **noncustodial hedge fund platform** where users can create and subscribe to **trading strategies** without transferring custody of their funds. Strategy providers monetize their strategies while keeping their proprietary code confidential, as execution is handled by a network of **off-chain Operators**.

Operators can be **any computational instance** capable of executing strategies securely and correctly. To ensure efficiency and reliability, we have spun up **AI Agent Operators** built from **Custom Templates hosted on Autonome**, which autonomously execute trading strategies as defined by strategy providers.

Leveraging **EigenLayer's AVS framework**, **TradeAlgoAVS** achieves **trust-minimized execution** and **on-chain verifiability**, with **EigenLayer restaking** securing the network.

TradeAlgoAVS allows:

1. Successful traders to scale their strategies into hedge fund-like structures without taking on the liabilities of managing client funds.
2. Investors to allocate funds to self-curating, on-chain-verified trading strategies based on performance statistics.
3. Coders and AI engineers to design and develop autonomous trading agents and earn commission.
4. Supporters to stake on operators and participate in the network’s security and growth.


## Comparison: Traditional Hedge Funds vs. TradeAlgoAVS

| Feature                     | Traditional Hedge Fund                                    | TradeAlgoAVS                                        |
|-----------------------------|----------------------------------------------------------|-----------------------------------------------------|
| **Custody of Funds**        | Users must transfer assets to the fund manager.         | Users retain full control of their assets.        |
| **Strategy Transparency**   | Investors blindly trust the hedge fund’s strategy.     | Strategies remain private but validated via statistical proofs. |
| **Execution Model**         | Trades executed by centralized entities.                | Trades executed by decentralized Operators, including AI Agents. |
| **Fees & Access**           | High fees, often locked for long periods.               | Competitive fees, full transparency, and no lock-up periods. |
| **Investor Protection**     | Requires trust in fund managers and regulators.        | On-chain validation ensures fair execution.        |

## Key Functionalities

1. Decentralized & Non-Custodial Trading Strategies
- Users retain full control over their assets.
- Strategy providers monetize their algorithms without revealing their proprietary code.
- Execution is performed by off-chain Operators, including AI agents hosted on Autonome.
2. Trust-Minimized Execution & On-Chain Verification
- Operators stake funds and are slashed for malicious behavior.
- Trading execution is validated using M-of-N statistical aggregation.
- Fraud-proof mechanisms detect deviations from expected performance benchmarks.
- The goal is to implement WYSIWYG literally what you see when you click subscribe in terms of strategy expected performance statistics should be what you get consistently in the long run.
3. Self-Curating Autonomous Strategies
- Strategies are on-chain verified based on real-time performance statistics.
- Poor-performing strategies are naturally filtered out.
- Strategy providers must backtest and paper trade before publishing.

![UI](./ui.png)

## Trust Modelling and Protocol Design

See [AVS README.md](https://github.com/ehsueh/trade-algo-avs) for details on the design of the protocol's **Trust Model** and **Task Definitions**.

![AVS Design](./tradealgoavs-design.png)

![Simplified Sequence Diagram](./tradealgoavs-simplified-seq-diagram.png)

## Technologies Used

1. Our AVS is built on top of Layr Labs's [Eigen Layer AVS](https://docs.eigenlayer.xyz/developers/avs-developer-guide), bootstrapped from their opensource [incredible-squaring-avs example](https://github.com/Layr-Labs/incredible-squaring-avs/tree/master)

2. Strategy secrets and investor credentials are stored in [Nillion Secret Vaults](https://docs.nillion.com/build/secret-vault).

3. Operators are built with [Autonome's Agent Custom Templates](https://dev.autonome.fun/autonome) integrated with Wealthsimple.

4. Coinbase Developer Platform's [OnchainKit](https://onchainkit.xyz/getting-started) allowed easy frontend chain integration and [AgentKit](https://docs.cdp.coinbase.com/agentkit/docs/welcome) allowed llm functionalities with account queries.

5. [Alchemy](https://www.alchemy.com/) used for RPC.

6. [Google Cloud Web3 and Platform](https://cloud.google.com/web3) for generous testnet funds (web3 faucets) and staging environment hosting.



## Partners

Huge thank-you's to the following organizations!

<p align="center">
  <a href="https://www.alchemy.com" target="_blank">
    <img src="partners/alchemy.png" alt="Alchemy" width="150"/>
  </a>
  <a href="https://www.autonome.io" target="_blank">
    <img src="partners/autonome.png" alt="Autonome" width="150"/>
  </a>
  <a href="https://www.cdp.com" target="_blank">
    <img src="partners/cdp.png" alt="CDP" width="150"/>
  </a>
  <a href="https://www.eigenlayer.xyz" target="_blank">
    <img src="partners/eigenlayer.png" alt="EigenLayer" width="150"/>
  </a>
  <a href="https://ethglobal.com" target="_blank">
    <img src="partners/ethglobal.png" alt="ETHGlobal" width="150"/>
  </a>
  <a href="https://cloud.google.com" target="_blank">
    <img src="partners/gcp.png" alt="Google Cloud Platform" width="150"/>
  </a>
  <a href="https://www.nillion.com" target="_blank">
    <img src="partners/nillion.png" alt="Nillion" width="150"/>
  </a>
</p>