import datetime
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite setup (or replace with Postgres/MySQL URI)
DATABASE_URL = "sqlite:///analytics_logs.db"
Base = declarative_base()

# Define Log model
class Log(Base):
    __tablename__ = "agent_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_query = Column(Text)
    category = Column(String(100))
    assigned_agent = Column(String(100))
    retrieved_info = Column(Text)
    final_response = Column(Text)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

# Initialize DB
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Logger agent
class LoggerAnalyticsAgent:
    def __init__(self):
        self.db = SessionLocal()

    def log_interaction(self, user_query, category, assigned_agent, retrieved_info, final_response):
        log = Log(
            user_query=user_query,
            category=category,
            assigned_agent=assigned_agent,
            retrieved_info=retrieved_info,
            final_response=final_response
        )
        self.db.add(log)
        self.db.commit()
        self.db.refresh(log)
        return log.id  # return log ID for traceability