import yaml
import discord
import google.generativeai as genai

class Config:
    file_path = "config.yaml"
    def __init__(self):
        with open(self.file_path, "r") as f:
            self.parser = yaml.safe_load(f)
    #load google_api_secret
    def getGoogleAPISecret(self):
        return self.parser['google_api_secret']
    #load discord_token
    def getDiscordToken(self):
        return self.parser['discord_token']
    #load target_id
    def getTargetChannelId(self):
        return self.parser['target_channel_id']
    def getMentions(self):
        return self.parser['mentions']
    def getAfterMessage(self):
        return self.parser['after_message']
    
class Client(discord.Client):
    def __init__(self, config, chat, *args, **kwargs):
        intents = discord.Intents.default()  # Create default intents
        intents.message_content = True
        super().__init__(intents=intents, *args, **kwargs)  # Pass intents to the parent class
        self.config = config
        self.chat = chat 
    

    async def on_ready(self):
        print(f'Logged in as {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return
        #short response on ping
        if (self.config.getMentions() and self.user.mentioned_in(message)):
            await message.channel.send(self.chat.send_message(message.content.lower()).text+self.config.getAfterMessage())
        #long response in channel and DMs
        if isinstance(message.channel, discord.DMChannel) or message.channel.id == self.config.getTargetChannelId():
            await message.channel.send(self.chat.send_message(message.content.lower()).text)   
        


def main():
    config = Config()
    print(config.getAfterMessage())
    genai.configure(api_key = config.getGoogleAPISecret())
    chat = genai.GenerativeModel('gemini-pro').start_chat(history=[])
    client = Client(config, chat)
    client.run(config.getDiscordToken())
   

if __name__ == "__main__":
    main()