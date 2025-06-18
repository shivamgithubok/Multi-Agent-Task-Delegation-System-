from langchain_core.runnables import Runnable
from langchain_core.messages import HumanMessage
import re

class InputHandlerAgent(Runnable):
    def invoke(self , input_text :str)-> str:
        if not input_text or len(input_text.strip()) < 5:
            return "input is very small"
        
        clean_text = re.sub(r'[^\x00-\x7F]+','',input_text)
        clean_text = clean_text.strip()

        if clean_text.lower() in ['hi','hello','by']:
            return "enter a valid data"
        return clean_text