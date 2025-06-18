# Multi-Agent-Task-Delegation-System-
📦 mats-project/
├── 🧠 agents/
│   ├── input_handler.py
│   ├── classifier_agent.py
│   ├── task_assigner.py
│   ├── knowledge_retriever.py
│   ├── response_generator.py
│   └── logger_analytics.py
│
├── ⚙️ backend/
│   ├── main.py                 # FastAPI entrypoint
│   ├── routes/
│   │   ├── ticket.py           # API for /submit-ticket
│   │   ├── classify.py         # API for classification
│   │   └── response.py         # API for generating responses
│   ├── services/
│   │   ├── agent_service.py    # Call agents here
│   │   └── database.py         # DB operations
│   ├── models/
│   │   └── schemas.py          # Pydantic models
│   └── database.db             # (Or link to MongoDB/Postgres)
│
├── 🌐 frontend/ (React)
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   └── TicketForm.jsx
│   │   ├── pages/
│   │   │   └── Dashboard.jsx
│   │   ├── services/
│   │   │   └── api.js          # Axios functions
│   │   └── App.js
│   └── package.json
│
├── 📜 README.md
└── 🐳 docker-compose.yml (Optional for full-stack deployment)

data flow 
React Form 
   ↓
POST /submit-ticket (FastAPI)
   ↓
[Agent Chain Execution]
   ↳ input_handler → classifier → assigner → retriever → responder → logger
   ↓
Response sent back to React