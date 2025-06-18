from fastapi import FastAPI
from routes import ticket, classify, response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Multi-Agent Support System")

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include route modules
app.include_router(ticket.router, prefix="/api")
app.include_router(classify.router, prefix="/api")
app.include_router(response.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Backend is running!"}





















# from fastapi import FastAPI, Request
# from pydantic import BaseModel
# from input_handler_agent import InputHandlerAgent

# app = FastAPI()
# handler_agent = InputHandlerAgent()

# class UserInput(BaseModel):
#     message: str

# @app.post("/api/validate-input")
# def validate_input(payload: UserInput):
#     response = handler_agent.invoke(payload.message)
#     return {"processed_input": response}

# from classifier_agent import ClassifierAgent

# app = FastAPI()
# classifier = ClassifierAgent()

# class QueryRequest(BaseModel):
#     message: str

# @app.post("/api/classify")
# def classify_message(request: QueryRequest):
#     category = classifier.classify(request.message)
#     return {"category": category}

# from task_assigner import TaskAssignerAgent

# assigner = TaskAssignerAgent()

# class CategoryRequest(BaseModel):
#     category: str

# @app.post("api/assign-task")
# def assign_task(request: CategoryRequest):
#     agent_name = assigner.assign_task(request.category)
#     return {"assigned_agent": agent_name}

# from retriever_agent import KnowledgeRetrieverAgent

# app = FastAPI()
# retriever = KnowledgeRetrieverAgent()

# class QueryRequest(BaseModel):
#     message: str

# @app.post("/api/retrieve")
# def retrieve_knowledge(request: QueryRequest):
#     answer = retriever.retrieve_answer(request.message)
#     return {"retrieved_answer": answer}

# from responder_agent import ResponderAgent

# app = FastAPI()
# responder = ResponderAgent()

# class ResponseRequest(BaseModel):
#     original_query: str
#     category: str
#     assigned_agent: str
#     retrieved_info: str

# @app.post("/api/respond")
# def generate_response(request: ResponseRequest):
#     final_reply = responder.generate_response(
#         request.original_query,
#         request.category,
#         request.assigned_agent,
#         request.retrieved_info
#     )
#     return {"response": final_reply}

# from logger_agent import LoggerAnalyticsAgent

# app = FastAPI()
# logger = LoggerAnalyticsAgent()

# class LogRequest(BaseModel):
#     user_query: str
#     category: str
#     assigned_agent: str
#     retrieved_info: str
#     final_response: str

# @app.post("/api/log")
# def log_interaction(request: LogRequest):
#     log_id = logger.log_interaction(
#         request.user_query,
#         request.category,
#         request.assigned_agent,
#         request.retrieved_info,
#         request.final_response
#     )
#     return {"message": "Logged", "log_id": log_id}