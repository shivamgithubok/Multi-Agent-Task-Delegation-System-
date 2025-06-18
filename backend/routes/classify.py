from fastapi import APIRouter
from models.schema import UserQuery, CategoryInput
from services.agent_services import classify_intent, assign_task

router = APIRouter()

@router.post("/classify")
def classify(user_input: UserQuery):
    category = classify_intent(user_input.message)
    return {"category": category}

@router.post("/assign")
def assign(category: CategoryInput):
    assigned = assign_task(category.category)
    return {"assigned_agent": assigned}
