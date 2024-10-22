import yaml
import os
import google.generativeai as genai

class Config:
    file_path = "config.yaml"
    def __init__(self):
        with open(self.file_path, "r") as f:
            self.parser = yaml.safe_load(f)
    #load google_api_secret
    def getGoogleAPISecret(self):
        return self.parser['google_api_secret']



def main():
    config = Config()
    genai.configure(api_key = config.getGoogleAPISecret())
    chat_model = genai.GenerativeModel('gemini-pro')
    chat = chat_model .start_chat(history=[])
    response = chat.send_message("co je sha256, zhrn do dvoch viet bez diakkritiky")
    print(response.text)

if __name__ == "__main__":
    main()