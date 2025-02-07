import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';
import swaggerUi from 'swagger-ui-express';
import swaggerJsDoc from 'swagger-jsdoc';
import { v4 as uuidv4 } from 'uuid';
import { SecretVaultWrapper } from 'nillion-sv-wrappers';
import { orgConfig } from './nillionOrgConfig.js';

dotenv.config();

const app = express();
app.use(cors());
app.use(express.json());

const PORT = process.env.PORT || 5000;
const NILLION_STRATEGY_SCHEMA_ID = process.env.NILLION_STRATEGY_SCHEMA_ID;
const NILLION_INVESTOR_SCHEMA_ID = process.env.NILLION_INVESTOR_SCHEMA_ID;

// Swagger Configuration
const swaggerOptions = {
  definition: {
    openapi: "3.0.0",
    info: {
      title: "Trading Strategies API",
      version: "1.0.0",
    },
    servers: [{ url: `http://localhost:${PORT}` }],
  },
  apis: ["./server.js"],
};

const swaggerDocs = swaggerJsDoc(swaggerOptions);
app.use("/docs", swaggerUi.serve, swaggerUi.setup(swaggerDocs));

/**
 * @swagger
 * components:
 *   schemas:
 *     TradingStrategy:
 *       type: object
 *       required:
 *         - _id
 *         - strategy_name
 *         - strategy_code
 *         - strategy_provider
 *         - roi
 *         - profitability
 *         - risk
 *       properties:
 *         _id:
 *           type: string
 *           format: uuid
 *         strategy_name:
 *           type: string
 *         strategy_code:
 *           type: string
 *         strategy_provider:
 *           type: string
 *         roi:
 *           type: number
 *         profitability:
 *           type: number
 *         risk:
 *           type: number
 *       example:
 *         strategy_name: "Momentum Mountain"
 *         strategy_code: "asdfasdf codes"
 *         strategy_provider: "0x1b0ac0E93011e82066e8A6E97460c04010121156"
 *         roi: 10
 *         profitability: 25
 *         risk: 0
 */

/**
 * @swagger
 * /strategies:
 *   post:
 *     summary: Create a new trading strategy
 *     tags:
 *       - Strategies
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             $ref: '#/components/schemas/TradingStrategy'
 *     responses:
 *       201:
 *         description: Strategy successfully created
 *       500:
 *         description: Internal server error
 */
app.post('/strategies', async (req, res) => {
  try {
    const { strategy_name, strategy_code, strategy_provider, roi, profitability, risk } = req.body;

    const data = [{
      strategy_name: { $allot: strategy_name },
      strategy_code: { $allot: strategy_code },
      strategy_provider: { $allot: strategy_provider },
      roi,
      profitability,
      risk
    }];

    const collection = new SecretVaultWrapper(orgConfig.nodes, orgConfig.orgCredentials, NILLION_STRATEGY_SCHEMA_ID);
    await collection.init();
    const dataWritten = await collection.writeToNodes(data);
    console.log(`Data written: ${JSON.stringify(dataWritten)}`);
    const newIds = [...new Set(dataWritten.map((item) => item.result.data.created).flat())];

    res.status(201).json({ message: "Strategy created successfully", ids: newIds });
  } catch (error) {
    console.error("Error creating strategy:", error);
    res.status(500).json({ error: error.message });
  }
});

/**
 * @swagger
 * /strategies:
 *   get:
 *     summary: Get all trading strategies
 *     tags:
 *       - Strategies
 *     responses:
 *       200:
 *         description: List of trading strategies
 *       500:
 *         description: Internal server error
 */
app.get('/strategies', async (req, res) => {
  try {
    const collection = new SecretVaultWrapper(orgConfig.nodes, orgConfig.orgCredentials, NILLION_STRATEGY_SCHEMA_ID);
    await collection.init();
    const decryptedCollectionData = await collection.readFromNodes({});

    res.status(200).json(decryptedCollectionData);
  } catch (error) {
    console.error("Error retrieving strategies:", error);
    res.status(500).json({ error: error.message });
  }
});

/**
 * @swagger
 * components:
 *   schemas:
 *     Investor:
 *       type: object
 *       required:
 *         - email
 *         - password
 *         - wallet_address
 *         - twofa
 *       properties:
 *         email:
 *           type: string
 *         password:
 *           type: string
 *         wallet_address:
 *           type: string
 *         twofa:
 *           type: string
 */

/**
 * @swagger
 * /investors:
 *   post:
 *     summary: Create a new investor
 *     tags:
 *       - Investors
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             $ref: '#/components/schemas/Investor'
 *     responses:
 *       201:
 *         description: Investor successfully created
 *       500:
 *         description: Internal server error
 */
app.post('/investors', async (req, res) => {
  try {
    const { email, password, wallet_address } = req.body;
    const investorId = uuidv4();

    const data = [{
      _id: investorId,
      email: { $share: email },
      password: { $share: password },
      wallet_address: { $share: wallet_address }
    }];

    const collection = new SecretVaultWrapper(orgConfig.nodes, orgConfig.orgCredentials, NILLION_INVESTOR_SCHEMA_ID);
    await collection.init();
    const dataWritten = await collection.writeToNodes(data);
    console.log(`Investor created: ${JSON.stringify(dataWritten)}`);

    res.status(201).json({ message: "Investor created successfully", id: investorId });
  } catch (error) {
    console.error("Error creating investor:", error);
    res.status(500).json({ error: error.message });
  }
});

/**
 * @swagger
 * /investors:
 *   get:
 *     summary: Get all investors
 *     tags:
 *       - Investors
 *     responses:
 *       200:
 *         description: List of investors
 *       500:
 *         description: Internal server error
 */
app.get('/investors', async (req, res) => {
  try {
    const collection = new SecretVaultWrapper(orgConfig.nodes, orgConfig.orgCredentials, NILLION_INVESTOR_SCHEMA_ID);
    await collection.init();
    const decryptedCollectionData = await collection.readFromNodes({});

    res.status(200).json(decryptedCollectionData);
  } catch (error) {
    console.error("Error retrieving investors:", error);
    res.status(500).json({ error: error.message });
  }
});

app.listen(PORT, () => {
  console.log(`✅ Server running on http://localhost:${PORT}`);
  console.log(`📄 Swagger docs available at http://localhost:${PORT}/docs`);
});
