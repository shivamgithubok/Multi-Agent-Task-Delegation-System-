from fastapi import APIRouter
from models.schema import TicketLog
from services.database import log_ticket

router = APIRouter()

@router.post("/log")
def log_ticket_data(ticket: TicketLog):
    log_id = log_ticket(ticket)
    return {"message": "Interaction logged", "log_id": log_id}
