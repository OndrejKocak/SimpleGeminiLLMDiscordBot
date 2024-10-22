import yaml

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
    print(config.getGoogleAPISecret())

if __name__ == "__main__":
    main()