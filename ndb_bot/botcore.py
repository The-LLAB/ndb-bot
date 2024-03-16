from langchain_openai import OpenAI as LangChainOpenAI
from langchain.chains import LLMChain
from openai import OpenAI as OpenAIClient

# Flag to determine which endpoint to use
USE_OPENAI = False  # Set to False to use your local server

if USE_OPENAI:
    # Use OpenAI's API with the updated langchain-openai import
    openai_client = OpenAIClient(api_key="your_openai_api_key_here")
    llm = LangChainOpenAI(openai_client=openai_client)
else:
    # Use your local server
    # Ensure you have a compatible LangChain wrapper for your local model
    llm = LangChainOpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

# Since LLMChain requires a prompt, create a basic prompt template
from langchain.prompts import PromptTemplate

# Example prompt template; adjust as needed for your bot's functionality
template = "You are a helpful assistant. Answer the following question: {question}"
prompt_template = PromptTemplate(template=template, input_variables=["question"])

# Initialize LLMChain with the LangChainOpenAI instance and the prompt template
llm_chain = LLMChain(prompt=prompt_template, llm=llm)

def chat_with_bot(question):
    # Use the LLMChain with a provided question to get a response
    response = llm_chain.run({"question": question})
    return response

if __name__ == '__main__':
    welcome_text = "Hello! I'm your AI assistant. What question do you have for me today?"
    print(welcome_text)
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Chatbot: Goodbye! Hope to assist you again soon.")
            break
        bot_response = chat_with_bot(user_input)
        print(f"Chatbot: {bot_response}")
