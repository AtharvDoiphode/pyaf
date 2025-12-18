# 🌤️ Weather Chat Assistant (PYAF)

A full-stack **Weather Chat Assistant** built as part of an assessment.  
The application allows users to ask weather-related questions for any city and receive real-time responses using a clean chat-style interface.

<img width="1919" height="907" alt="image" src="https://github.com/user-attachments/assets/884ed3d0-a0bc-4bde-a0e8-551a122b7a55" />


## 🛠️ Tech Stack

### Frontend
- React (Vite)
- Axios
- CSS (Glassmorphism UI)
- Responsive Design

### Backend
- FastAPI
- Python
- OpenWeather API

---

## 📂 Project Structure

sanchai-weather/
│
├── sanchai-weather-frontend/
│ ├── src/
│ │ ├── App.jsx
│ │ ├── App.css
│ │ ├── assets/
│ │ │ └── sky.jpg
│ │ └── main.jsx
│ └── package.json
│
├── sanchai-weather-backend/
│ ├── app/
│ │ └── main.py
│ ├── requirements.txt
│ └── .env (ignored)
│
└── README.md


---

## ✨ Features

- Chat-based weather queries
- Real-time weather data
- City name validation
- Clean glassmorphism UI
- Responsive layout (mobile, tablet, desktop)
- Error handling for invalid inputs

---

## ⚙️ Backend Setup (FastAPI)

1. Navigate to backend folder:
   ```bash
   cd sanchai-weather-backend
Create virtual environment:

python -m venv venv


Activate venv:

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


Add .env file:

OPENWEATHER_API_KEY=your_api_key_here


Run server:

python -m uvicorn app.main:app --reload


Backend runs on:

http://127.0.0.1:8000

🎨 Frontend Setup (React)

Navigate to frontend folder:

cd sanchai-weather-frontend


Install dependencies:

npm install


Start frontend:

npm run dev


Frontend runs on:

http://localhost:5173

🧪 API Endpoint Used
POST /chat
{
  "message": "What is the weather of Pune?"
}


Response:

{
  "reply": "The temperature in Pune is 21.89°C with clear sky."
}

🧠 What I Learned

Integrating FastAPI with a React frontend

Handling API keys securely using .env

Managing Git repositories properly

Building responsive UI with glassmorphism

Debugging Git and deployment issues

🚀 Future Enhancements

Weather icons

City-based background changes

Typing animation

Deployment on Netlify / Vercel

Backend deployment on Render
