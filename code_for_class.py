import os
from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_ai import Agent,ModelRetry
from mistralai import Mistral
from pydantic_ai.models.mistral import MistralModel
import json
from mistralai import Mistral

load_dotenv()
mistrl_api_key = os.getenv("MISTRL_API_KEY")
model          = "mistral-large-latest"
client         = Mistral(api_key=mistrl_api_key)
mist_model     = MistralModel('mistral-small-latest',api_key=mistrl_api_key)

class ResponseModel(BaseModel):
    pest_name   : list[str]
    description  : list[str]


class ZAgent:
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
        completion       = client.chat.complete(
                            model         = "mistral-large-latest", 
                            temperature   = 0,
                            messages      = self.messages)
        response_content = completion.choices[0].message.content
        f_agent          =  Agent( model  = mist_model, 
                            result_type   = ResponseModel,
                            system_prompt = f'''you are a helpful assistant..you need to copy the  data of {response_content} in required format
                                             ''')

        final_format     = f_agent.run_sync('hi')

        return final_format.data.model_dump()
    

#mybot = ZAgent("you are a marketing expert who can provide list of famous brands for the product")
#techbot_response = mybot('laptop')
agrbot = ZAgent("you are a agricultural expert who can provide list of pests affecting the crop requested")
botresponse = agrbot('wheat')
print(f"--------     Agri Bot    -------------\n")

import pandas as pd
df = pd.DataFrame(botresponse, columns = ['pest_name','description'])
print(df)

