🚀 OpenAI-Assisted AI Chat Application (Full Stack)

A full-stack AI assistant application built using FastAPI (Backend) and Streamlit (Frontend), powered by OpenAI models.
Designed with professional software engineering practices including API layer, authentication, deployment, logging, and session handling.

🌐 Live Application
🔹 Frontend (Streamlit - User Interface)

👉 https://openai-assistant-drrcsaipzrb7fevqdkrhv4.streamlit.app/

🔹 Backend (FastAPI - API Server)

👉 https://ai-assistant-backend-1-0wwp.onrender.com

🔹 API Documentation (Swagger UI)

👉 https://ai-assistant-backend-1-0wwp.onrender.com/docs

🧠 Key Features

✅ AI-powered conversational assistant
✅ Multiple assistant modes (Study, Code, Career, General)
✅ REST API architecture
✅ Secure API authentication using headers
✅ Session-based chat history
✅ Backend logging and error handling
✅ Memory trimming for efficiency
✅ Deployed full-stack system (Cloud hosted)

⚙️ Tech Stack
Backend

Python 3.11+

FastAPI

OpenAI API

Pydantic

Uvicorn

REST APIs

Logging

API Key Security

Environment Variables

Frontend

Streamlit

Requests API

Session State handling

Chat UI components

Cloud Deployment

Backend: Render

Frontend: Streamlit Cloud

📂 Project Structure
openai-assistant/
│
├── backend/
│   ├── app.py          # FastAPI server
│   ├── model.py        # OpenAI logic
│   ├── memory.py       # Session management
│   ├── security.py     # API key authentication
│   ├── prompts.py      # Assistant modes
│   ├── requirements.txt
│   └── .env
│
├── streamlit_app.py     # Frontend UI
├── README.md            # Documentation
└── requirements.txt

🔐 Environment Setup

Create a .env file inside the backend folder:

OPENAI_API_KEY=your_openai_api_key
BACKEND_API_KEY=your_backend_api_key


⚠️ Do not commit real API keys to GitHub.

▶️ Run Locally
Start Backend
cd backend
python -m uvicorn app:app --reload --port 8000


Backend runs at:

http://127.0.0.1:8000

Start Frontend
cd ..
streamlit run streamlit_app.py


Frontend opens at:

http://localhost:8501

🔁 API Endpoints
Endpoint	Method	Purpose
/health	GET	Health check
/chat	POST	AI conversation
/sessions	GET	List chat sessions
/sessions/{id}	GET	Retrieve chat history
📤 API Sample Request
Headers
x-api-key: your_backend_api_key
Content-Type: application/json

Body
{
  "session_id": null,
  "mode": "General Assistant",
  "messages": [
    {"role": "user", "content": "Hello"}
  ]
}

☁️ Deployment
✅ Backend (Render)

Start command:

uvicorn app:app --host 0.0.0.0 --port 10000


Environment variables:

OPENAI_API_KEY
BACKEND_API_KEY

✅ Frontend (Streamlit Cloud)

Connected to GitHub repository
Main file path: streamlit_app.py
Deployed publicly

📜 Logging

Backend logs:

backend.log


Includes:

API requests

Errors

Session activity

🔐 Security

✅ API authentication via headers
✅ Environment variables for secrets
✅ Backend middleware validation
✅ No credentials committed to GitHub

📈 Future Enhancements

✅ User authentication
✅ Chat export
✅ File uploads (PDF / DOC)
✅ Admin dashboard
✅ Rate limiting
✅ Database integration
✅ Docker support
✅ Kubernetes deployment (Advanced scale)

👨‍💻 Developer

Peraka Sai Priya
B.Tech — Data Science
Malla Reddy Institute of Engineering & Technology
Graduation Year: 2026

🔗 GitHub: https://github.com/saipriya1322

🔗 LinkedIn: https://linkedin.com/in/peraka-saipriya-7750ba2a7

🎯 Why This Project Matters

This system demonstrates:

✅ Backend engineering
✅ Full-stack architecture
✅ Cloud deployment
✅ API security practices
✅ Real-world AI integration
✅ Industry-grade project design

Suitable for:

• Google SWE
• AI roles
• Product companies
• Startup engineering teams

⭐ If you like this project, give it a star on GitHub!