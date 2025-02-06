# TradeAlgoAVS

## Overview

**TradeAlgoAVS** is a decentralized **noncustodial hedge fund platform** where users can create and subscribe to **trading strategies** without transferring custody of their funds. Strategy providers monetize their strategies while keeping their proprietary code confidential, as execution is handled by a network of **off-chain Operators**.

Operators can be **any computational instance** capable of executing strategies securely and correctly. To ensure efficiency and reliability, we have spun up **AI Agent Operators** built from **Custom Templates hosted on Autonome**, which autonomously execute trading strategies as defined by strategy providers.

Leveraging **EigenLayer's AVS framework**, **TradeAlgoAVS** achieves **trust-minimized execution** and **on-chain verifiability**, with **EigenLayer restaking** securing the network.


## Comparison: Traditional Hedge Funds vs. TradeAlgoAVS

| Feature                     | Traditional Hedge Fund                                    | TradeAlgoAVS                                        |
|-----------------------------|----------------------------------------------------------|-----------------------------------------------------|
| **Custody of Funds**        | Users must transfer assets to the fund manager.         | Users retain full control of their assets.        |
| **Strategy Transparency**   | Investors blindly trust the hedge fund’s strategy.     | Strategies remain private but validated via statistical proofs. |
| **Execution Model**         | Trades executed by centralized entities.                | Trades executed by decentralized Operators, including AI Agents. |
| **Fees & Access**           | High fees, often locked for long periods.               | Competitive fees, full transparency, and no lock-up periods. |
| **Investor Protection**     | Requires trust in fund managers and regulators.        | On-chain validation ensures fair execution.        |

See [AVS README.md](https://github.com/ehsueh/trade-algo-avs) for details on the design of the protocol's **Trust Model** and **Task Definitions**.

## Opensource References and Libs

Our AVS is built on top of Layr Labs's Eigen Layer AVS, bootstrapped from their opensource [incredible-squaring-avs example](https://github.com/Layr-Labs/incredible-squaring-avs/tree/master)


