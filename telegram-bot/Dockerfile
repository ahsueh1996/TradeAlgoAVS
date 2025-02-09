# Use an official Node.js image as the base image
FROM node:18

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json (if available)
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the bot's source code into the container
COPY . .

# Expose the port for the webhook server
EXPOSE 8080

# Run the bot
CMD ["node", "bot.js"]
