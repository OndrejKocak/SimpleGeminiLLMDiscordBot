import discord
import google.generativeai as genai
from dotenv import load_dotenv
import os

class Client(discord.Client):
    def __init__(self, chat, *args, **kwargs):
        intents = discord.Intents.default()  # Create default intents
        intents.message_content = True
        super().__init__(intents=intents, *args, **kwargs)  # Pass intents to the parent class
        self.chat = chat 
    
    async def on_ready(self):
        print(f'Logged in as {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return
        if (os.getenv('MENTIONS').lower() == "true" and self.user.mentioned_in(message)): #short response on ping
            await message.channel.send(self.chat.send_message(message.content.lower(), generation_config = genai.types.GenerationConfig(candidate_count = 1,max_output_tokens = 100, top_p = 0.6, top_k = 5, temperature = 0.6)).text)
        #long response in channel and DMs
        if (isinstance(message.channel, discord.DMChannel) or message.channel.id == int(os.getenv('TARGET_CHANNEL_ID'))) and not self.user.mentioned_in(message):
            await message.channel.send(self.chat.send_message(message.content.lower(), generation_config= genai.types.GenerationConfig()).text)   
        
def main():
    load_dotenv()
    genai.configure(api_key = os.getenv('GOOGLE_API_SECRET'))
    client = Client(genai.GenerativeModel('gemini-pro').start_chat(history=[]))
    client.run(os.getenv('DISCORD_TOKEN'))
   
if __name__ == "__main__":
    main()