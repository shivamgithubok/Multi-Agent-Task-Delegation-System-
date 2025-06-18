from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
import datetime
from models.schema import TicketLog

DB_URL = "sqlite:///analytic_logs.db"
engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class InteractionLog(Base):
    __tablename__ = "agent_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_query = Column(Text)
    category = Column(String(100))
    assigned_agent = Column(String(100))
    retrieved_info = Column(Text)
    final_response = Column(Text)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

Base.metadata.create_all(bind=engine)

def log_ticket(ticket: TicketLog):
    db = Session()
    log = InteractionLog(
        user_query=ticket.original_query,
        category=ticket.category,
        assigned_agent=ticket.assigned_agent,
        retrieved_info=ticket.retrieved_info,
        final_response=ticket.final_response
    )
    db.add(log)
    db.commit()
    db.refresh(log)
    return log.id
