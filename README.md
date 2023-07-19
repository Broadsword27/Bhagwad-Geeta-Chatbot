# Bhagwad-Geeta-Chatbot
Find answers to all your questions by conversing with Shrimad Bhagavad Geeta

This is a chatbot implementation using the GPT-3.5 language model from OpenAI and the LlamaIndex library for document indexing. The chatbot allows users to have interactive conversations with the Bhagavad Geeta by inputting text messages.

# Prerequisites
Python 3.7 or higher
OpenAI API key
LlamaIndex library

# Installation
Clone the repository or download the code files.
Install the required Python packages by running the following command:

Copy code
<pip install -r requirements.txt>

# Usage
Obtain an API key from the OpenAI platform at https://platform.openai.com/account/api-keys.
Set the API key as an environment variable named OPENAI_API_KEY in a .env file or your system environment variables.
Place your data files in the ./data directory. The data files should be in a format supported by LlamaIndex.
Modify the code as needed to customize the chatbot behavior, such as adjusting the chat history file name or prompt formatting.
Run the Geeta-Reader.py script using the following command:
Copy code
python Geeta-Reader.py
Enter your messages in the terminal, and the chatbot will respond accordingly.
To exit the conversation, type "bye" or "goodbye".

# Customization
You can modify the code to change the behavior of the chatbot. For example, you can customize the prompt formatting or add additional functionality.
Adjust the data directory path in the SimpleDirectoryReader class instantiation to point to your specific data files.
Swap out the index with your preferred knowledge base by replacing the GPTVectorStoreIndex instantiation with the desired index.


# Acknowledgments
This code uses the OpenAI GPT-3.5 language model for generating responses.
LlamaIndex is used for document indexing and retrieval.
