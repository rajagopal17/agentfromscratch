import os
from dotenv import load_dotenv
load_dotenv()



from mistralai import Mistral
mistrl_api_key = os.getenv("MISTRL_API_KEY")
model = "mistral-large-latest"
messages = [
            {"role": "assistant", "content": f'''analyze the user query, think about the end goal of the user, and provide step by step instructions to achieve the goal.
                                              always display the thinking process and the steps in a clear and concise manner.'''},
                                              {"role": "user", "content": "how to convert a  excel file to csv file"}]
client    = Mistral(api_key=mistrl_api_key)
response  = client.chat.complete(
    model = model,
    
    messages = messages,
    #tools = tools,
    tool_choice = "any",
)
#print(response.choices[0].message.content)
######################### function to accumulate messages 

def get_chat_response(user_message, message_history=None):
    """
    Get chat response from Mistral API with message history management
    
    Args:
        user_message (str): The user's input message
        message_history (list, optional): Previous message history
    
    Returns:
        tuple: (response_content, updated_message_history)
    """
    mistrl_api_key = os.getenv("MISTRL_API_KEY")
    model = "mistral-large-latest"
   
    # Initialize message history if None
    if message_history is None:
        message_history = [
            {
                "role": "assistant",
                "content": """analyze the user query, think about the end goal of the user, and provide step by step instructions to achieve the goal.
                             always display the thinking process and the steps in a clear and concise manner."""
            }
        ]
    
    # Add user message to history
    message_history.append({"role": "user", "content": user_message})
    
    client = Mistral(api_key=mistrl_api_key)
    response = client.chat.complete(
        model=model,
        messages=message_history,
        tool_choice="any",
    )
    
    # Get response content
    response_content = response.choices#[0].message.content
    
    # Add assistant's response to history
    message_history.append({"role": "assistant", "content": response_content})
    
    return response_content, message_history

# Example usage:
#if __name__ == "__main__":
user_query = "what is the capital of indonesia? what is its population,.? and what is its GDP as on 2022"
response_text, messages = get_chat_response(user_query)
print(response_text)
print('------------------------\n')
print(messages)
#    print('------------------------\n')