from fastapi import APIRouter
from models.schema import UserQuery, FinalInput
from services.agent_service import retrieve_knowledge, generate_response

router = APIRouter()

@router.post("/retrieve")
def retrieve(user_input: UserQuery):
    answer = retrieve_knowledge(user_input.message)
    return {"retrieved_answer": answer}

@router.post("/respond")
def respond(data: FinalInput):
    reply = generate_response(data)
    return {"response": reply}
