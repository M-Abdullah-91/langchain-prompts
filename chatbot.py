from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,  HumanMessage, AIMessage
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url='https://openrouter.ai/api/v1',
    model='deepseek/deepseek-v3.2'
)

chat_history = [
    SystemMessage(content="You are helpful AI Assitant")
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ", result.content)


print(chat_history)