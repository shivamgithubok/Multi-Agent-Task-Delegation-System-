from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

prompt = ChatPromptTemplate.from_template("""
You are a smart support agent that replies to user queries.

Given the following:
- User Query: {original_query}
- Category: {category}
- Assigned Agent: {assigned_agent}
- Retrieved Info: {retrieved_info}

Compose a helpful, concise, and friendly response in plain English.
Do not mention internal agent names.

Respond professionally, addressing the user directly.
""")

responder_chain: Runnable = prompt | llm

class ResponderAgent:
    def generate_response(self, original_query, category, assigned_agent, retrieved_info):
        input_data = {
            "original_query": original_query,
            "category": category,
            "assigned_agent": assigned_agent,
            "retrieved_info": retrieved_info
        }
        result = responder_chain.invoke(input_data)
        return result.content.strip()
