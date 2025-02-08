# Trading Strategies API with Nillion Secret Vault

This project provides a **secure backend API** for managing **trading strategies** using [**Nillion Secret Vault**](https://docs.nillion.com/build/secret-vault).

## 📌 Features
- Create, update, and retrieve **trading strategies** securely.
- Uses **Nillion Secret Vault** for encryption and data storage.
- **Swagger API documentation available at** `/docs`.
- **Docker support** for easy deployment.

---

## 🚀 Getting Started

### Set Up Env
1. Run npm install
```npm install```

2. Make sure your `.env` file include:
```
PORT=5000
NILLION_ORG_SECRET=b0.....0031870
NILLION_ORG_DID=did:nil:testnet:nill.....05la
NILLION_STRATEGY_SCHEMA_ID=08....f7d9
NILLION_INVESTOR_SCHEMA_ID=40....4700
```

## 🏃 Running Locally

```
node server.js
````

## 🐳 Running with Docker
```
docker build -t trading-strategies-api .
docker run -p 5000:5000 --env-file .env trading-strategies-api
```

API Base URL: http://localhost:5000
Swagger UI: http://localhost:5000/docs


## Usage

1. Create a Strategy `POST /strategies`
Example Input:

```
{
  "strategy_name": "Momentum Mountain",
  "strategy_code": "asdfasdf codes",
  "strategy_provider": "0x1b0ac0E93011e82066e8A6E97460c04010121156",
  "roi": 10,
  "profitability": 25,
  "risk": 0
}
```
Example Response:
```
{
  "message": "Strategy created successfully",
  "ids": [
    "b1c133ea-02e1-4411-9d46-48e847d6d879"
  ]
}
```
2. Get all Strategies `GET /strategies`

Example Response:
```
[
  {
    "_id": "87e3c2f0-ffaf-4298-9dae-79247cdef502",
    "strategy_name": "Momentum Mountain",
    "strategy_code": "asdfasdf codes",
    "strategy_provider": "0x1b0ac0E93011e82066e8A6E97460c04010121156",
    "roi": 10,
    "profitability": 25,
    "risk": 0
  }
]
```