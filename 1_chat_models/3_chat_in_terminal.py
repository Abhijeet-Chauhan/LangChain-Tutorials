from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(model="llama3-8b-8192")

chat_history = []

system_message = SystemMessage(content="You are a very helpful AI Assistant")

chat_history.append(system_message)

while True:
    query = input("You: ")
    if query.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=query))

    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))

    print(f"AI: {response}")

print("--------Message History-------")
print(chat_history)
