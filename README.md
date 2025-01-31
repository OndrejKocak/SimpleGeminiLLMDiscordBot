# SimpleGeminiLLMDiscordBot

**SimpleGeminiLLMDiscordBot** is a lightweight Discord bot written in Python. It leverages a Gemini Large Language Model (LLM) to enable intelligent interactions with users on a Discord server.

## Features
- Provides AI-driven responses using Gemini LLM.
- Easy setup and configuration.
- Extensible to include custom functionality.

## Requirements
- Python 3.8 or later
- A Discord account and bot token
- GOOGLE API key

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/OndrejKocak/SimpleGeminiLLMDiscordBot.git
   cd SimpleGeminiLLMDiscordBot
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure the bot:
   - Copy `env_example` to `.env` and fill in the required details (e.g., Discord bot token, API key).

4. Run the bot:
   ```bash
   python main.py
   ```
   
## Docker Deployment:
1. Build the Docker image:
   ```bash
   docker build -t simple-gemini-bot .
   ```
2. Run the container:
   ```bash
   docker run -d simple-gemini-bot
   ```
   
## Usage
- Add the bot to your Discord server using the bot's URL from the [Discord Developer Portal](https://discord.com/developers).
- Create channel reserved for chat with bot (optional)
- Interact with the bot through pings in any server channel it has access to.

## License
This project is licensed under the MIT License. For more details, see the [LICENSE](LICENSE) file.

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request on GitHub.
