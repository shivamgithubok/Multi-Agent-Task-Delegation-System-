from langchain.google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = "gemini-1.5-flash",
    api_key = os.getenv("GOOGLE_API_KEY")
)

prompt = ChatPromptTemplate.from_template("""
You are an intelligent agent assigner in a support system.

Based on the category, assign the appropriate internal agent.
Only return the agent's name.

### Mapping Rules:
- Technical Support → tech_support_bot_2
- Billing → billing_bot_1
- Feedback → feedback_logger
- Account/Login Issues → auth_support_bot_3
- General Inquiry → general_assistant_bot

Category: "{category}"       
""")

assigner_chain: Runnable = prompt | llm
class TaskAssignerAgent:
    def assign_task(self,category:str)->str:
        response = assigner_chain.invoke({"category":category})
        return response.content.strip()