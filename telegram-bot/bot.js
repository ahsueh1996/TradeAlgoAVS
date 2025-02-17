require('dotenv').config();
const express = require('express');
const TelegramBot = require('node-telegram-bot-api');
const { ChatOpenAI } = require("@langchain/openai");


const axios = require('axios');

const BOT_TOKEN = process.env.TELEGRAM_BOT_TOKEN;
const API_ENDPOINT = process.env.API_ENDPOINT;
const OPENAI_API_KEY = process.env.OPENAI_API_KEY;
const WEBHOOK_URL = `${process.env.WEBHOOK_BASE_URL}/webhook`; // Example: https://your-cloud-run-url/webhook

const bot = new TelegramBot(BOT_TOKEN);
const app = express();
app.use(express.json());

// Set webhook for Telegram
bot.setWebHook(WEBHOOK_URL)
  .then(() => console.log(`✅ Webhook set to: ${WEBHOOK_URL}`))
  .catch(err => console.error("❌ Error setting webhook:", err));

app.post("/webhook", (req, res) => {
  bot.processUpdate(req.body);
  res.sendStatus(200);
});

const runningTasks = new Map(); // Store running tasks

// --- "/start" command ---
bot.onText(/\/start/, (msg) => {
    const chatId = msg.chat.id;
    bot.sendMessage(chatId, "Hello! Use /schedule_task to run a task.");
});

// --- "/schedule_task" command: Executes every 5 seconds for 5 times ---
bot.onText(/\/schedule_task/, (msg) => {
    const chatId = msg.chat.id;

    if (runningTasks.has(chatId)) {
        bot.sendMessage(chatId, "⚠️ A task is already running! Wait until it completes.");
        return;
    }

    bot.sendMessage(chatId, "✅ Task started! Executing every 5 seconds for 5 times.");

    let count = 0;
    const maxExecutions = 5;
    const intervalTime = 5000; // 5 seconds

    const task = setInterval(() => {
        count++;
        bot.sendMessage(chatId, `⏳ Task Execution #${count}`);

        if (count >= maxExecutions) {
            clearInterval(task);
            runningTasks.delete(chatId); // Remove from running tasks
            bot.sendMessage(chatId, "✅ Task completed.");
        }
    }, intervalTime);

    runningTasks.set(chatId, task);
});

// --- "/cancel_task" command: Stop running task ---
bot.onText(/\/cancel_task/, (msg) => {
    const chatId = msg.chat.id;

    if (runningTasks.has(chatId)) {
        clearInterval(runningTasks.get(chatId));
        runningTasks.delete(chatId);
        bot.sendMessage(chatId, "❌ Task cancelled.");
    } else {
        bot.sendMessage(chatId, "⚠️ No running task to cancel.");
    }
});

// --- "/status" command: Check if a task is running ---
bot.onText(/\/status/, (msg) => {
    const chatId = msg.chat.id;

    if (runningTasks.has(chatId)) {
        bot.sendMessage(chatId, "🔄 A task is currently running.");
    } else {
        bot.sendMessage(chatId, "✅ No task is currently running.");
    }
});

// --- "/fetch" command: Fetch data from API ---
bot.onText(/\/fetch/, async (msg) => {
  const chatId = msg.chat.id;
  const userId = msg.from.id;  // Telegram User ID
  const firstName = msg.from.first_name || "Unknown"; // User's First Name
  const lastName = msg.from.last_name || ""; // User's Last Name (Optional)
  const username = msg.from.username ? `(@${msg.from.username})` : ""; // Username (if exists)


  try {
    // Call API with user ID
    const response = await axios.get(API_ENDPOINT, { params: { user_id: userId } });
    const data = response.data;

    // Format and send response
    const message = `
👤 *User Info:*
🆔 *User ID:* \`${userId}\`
📛 *Name:* ${firstName} ${lastName} ${username}

📢 *API Response:*
\`\`\`json
${JSON.stringify(data, null, 2)}
\`\`\`
`;

    bot.sendMessage(chatId, message, { parse_mode: "Markdown" });

  } catch (error) {
    console.error("Error fetching API data:", error.message);
    bot.sendMessage(chatId, "⚠️ Error fetching data. Try again later.");
  }
});

// --- "/chat" command: Start AI chat mode ---
bot.onText(/\/chat (.+)/, async (msg, match) => {
  const chatId = msg.chat.id;
  const userMessage = match[1]; // Extract user input after /chat

  try {
    const model = new ChatOpenAI({
      modelName: "gpt-4",
      temperature: 0.7,
      apiKey: OPENAI_API_KEY
    });


    // Define a system prompt to control AI responses
    const systemPrompt = `
You are an AI assistant in a Telegram bot. Your goal is to provide clear, concise, and helpful answers.
Keep responses professional but friendly. Avoid discussing harmful, unethical, or controversial topics.
If the user asks something irrelevant, politely decline.
      `;

    // Generate AI response using structured prompts
    const aiResponse = await model.invoke([
      { role: "system", content: systemPrompt },
      { role: "user", content: userMessage }
    ]);
    // const aiResponse = await model.invoke(userMessage);

    // Send AI response
    bot.sendMessage(chatId, `🤖 *AI Reply:*\n${aiResponse.content}`, { parse_mode: "Markdown" });

  } catch (error) {
    console.error("Error with AI chat:", error);
    bot.sendMessage(chatId, "⚠️ Error processing AI response. Try again later.");
  }
});



// Start Express server
const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
  console.log(`🚀 Bot is running on port ${PORT}`);
});
