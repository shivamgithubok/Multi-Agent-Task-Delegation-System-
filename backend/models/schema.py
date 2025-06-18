from pydantic import BaseModel

class UserQuery(BaseModel):
    message: str

class CategoryInput(BaseModel):
    category: str

class FinalInput(BaseModel):
    original_query: str
    category: str
    assigned_agent: str
    retrieved_info: str

class TicketLog(FinalInput):
    pass
