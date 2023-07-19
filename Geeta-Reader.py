import os
from dotenv import find_dotenv, load_dotenv
from llama_index import SimpleDirectoryReader
from llama_index import GPTVectorStoreIndex
from langchain.llms.base import LLM
import openai
import json


load_dotenv(find_dotenv())

OPENAI_API_KEY=os.environ["OPENAI_API_KEY"]

class Chatbot:
    def __init__(self, api_key, index):
        self.index = index
        openai.api_key = api_key
        self.chat_history = []

    def generate_response(self, user_input):
        prompt = "\n".join([f"{message['role']}: {message['content']}" for message in self.chat_history[-5:]])
        prompt += f"\nUser: {user_input}"
        query_engine = index.as_query_engine()
        response = query_engine.query(user_input)

        message = {"role": "assistant", "content": response.response}
        self.chat_history.append({"role": "user", "content": user_input})
        self.chat_history.append(message)
        return message
    
    def load_chat_history(self, filename):
        try:
            with open(filename, 'r') as f:
                self.chat_history = json.load(f)
        except FileNotFoundError:
            pass

    def save_chat_history(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.chat_history, f)

# Load you data into 'Documents' a custom type by LlamaIndex
documents = SimpleDirectoryReader('./data').load_data() # Create a folder "data" in your source directory and add the Bhagavad-Gita.pdf

# Create an index of your documents
index = GPTVectorStoreIndex.from_documents(documents)

# Query your index!

# Swap out your index below for whatever knowledge base you want
bot = Chatbot("Add_YOUR_OPENAI_API_KEY", index=index) # Add your OPENAI_API_KEY 
bot.load_chat_history("chat_history.json")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "goodbye"]:
        print("Bot: Goodbye!")
        bot.save_chat_history("chat_history.json")
        break
    response = bot.generate_response(user_input)
    print(f"Bot: {response['content']}")