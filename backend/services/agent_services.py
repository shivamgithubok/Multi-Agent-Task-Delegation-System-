import sys
import os

# Add the root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from agents.classifier_agent import ClassifierAgent
from agents.classifier_agent import ClassifierAgent
from agents.knowledge_retriever import KnowledgeRetrieverAgent
from agents.response_generator import ResponderAgent

classifier = ClassifierAgent()
assigner = ClassifierAgent()
retriever = KnowledgeRetrieverAgent()
responder = ResponderAgent()

def classify_intent(message: str) -> str:
    return classifier.classify(message)

def assign_task(category: str) -> str:
    return assigner.assign(category)

def retrieve_answer(message: str) -> str:
    return retriever.retrieve(message)

def generate_response(data) -> str:
    return responder.generate_response(
        original_query=data.original_query,
        category=data.category,
        assigned_agent=data.assigned_agent,
        retrieved_info=data.retrieved_info
    )