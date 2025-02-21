import os
from dotenv import load_dotenv
load_dotenv()



from mistralai import Mistral
mistrl_api_key = os.getenv("MISTRL_API_KEY")
model = "mistral-large-latest"
client    = Mistral(api_key=mistrl_api_key)

class Agent:
    def __init__(self, system_msgs=""):
        self.system_msgs = system_msgs
        self.messages = []
        if self.system_msgs:
            self.messages.append({"role": "system", "content": system_msgs})

    def __call__(self, message):
        self.messages.append({"role": "user", "content": message})
        result = self.execute()
        self.messages.append({"role": "assistant", "content": result})
        return result

    def execute(self):
        completion = client.chat.complete(
                        model        = "mistral-large-latest", 
                        temperature  = 0,
                        messages     = self.messages)
        return completion.choices[0].message.content
    
prompt        = ''#"you are a useful assistant that can answer queries"
get_result    = Agent()
final_result  = get_result("what is the capital of France?")
#print(final_result)
#print(get_result("what is the capital of France?"))
next_prompt   = "then what is its population?"
#print(get_result(next_prompt))
#next_3 = "a few lines about its history"
#print(get_result(next_3))
print(get_result('who is its mayor?'))
print(get_result('when was she elected as mayor?'))
print(get_result('regarding which city are we discussing now'))
print(get_result.messages)
