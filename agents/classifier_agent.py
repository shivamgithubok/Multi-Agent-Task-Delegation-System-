from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable
from dotenv import load_dotenv
import os

load_dotenv()

# Check if API key is set
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY environment variable is not set. Please set it in your .env file.")

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    api_key=api_key
)

prompt = ChatPromptTemplate.from_template("""
You are a classification agent for customer queries.

Classify the following message into one of the categories:
- Technical Support
- Billing
- Feedback
- Account/Login Issues
- General Inquiry

Respond with only the category name.

Message: "{query}"
""")

classifier_chain: Runnable = prompt | llm

class ClassifierAgent:
    def classify(self, query: str) -> str:
        response = classifier_chain.invoke({"query": query})
        return response.content.strip()
