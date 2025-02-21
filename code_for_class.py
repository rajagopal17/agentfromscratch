import os
from dotenv import load_dotenv
load_dotenv()



from mistralai import Mistral
mistrl_api_key = os.getenv("MISTRL_API_KEY")
model = "mistral-large-latest"
client    = Mistral(api_key=mistrl_api_key)

class Agent:
    def __init__(self, system_prompt=""):
        self.system_prompt = system_prompt
        self.messages = []
        if self.system_prompt:
            self.messages.append({"role": "system", "content": system_prompt})
       

    def __call__(self, message):
        self.messages.append({"role": "user", "content": message})
        result = self.execute()
        return result

    def execute(self):
        completion = client.chat.complete(
                        model        = "mistral-large-latest", 
                        temperature  = 0,
                        messages     = self.messages)
        return completion.choices[0].message.content
    

mybot = Agent("you are a marketing expert who can provide list of famous brands for the product")
agrbot = Agent("you are a agricultural expert who can provide list of pests affecting the given crop")
print(mybot('mobile phone'))
print('/n--------      AGRI BOT    -------------/n')
print(agrbot('rice'))