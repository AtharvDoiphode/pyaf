from fastapi import APIRouter
from app.schemas import ChatRequest, ChatResponse
from app.services.weather_tool import get_weather

router = APIRouter()

def extract_city(message: str) -> str:
    message = message.lower()
    for key in ["weather of", "weather in", "weather at"]:
        if key in message:
            return message.split(key)[-1].replace("?", "").strip()
    return ""

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        message = request.message.lower()

        if "weather" in message:
            city = extract_city(message)

            if not city:
                return ChatResponse(reply="Please specify a city name.")

            weather_info = get_weather(city)
            return ChatResponse(reply=weather_info)

        return ChatResponse(
            reply="Hello! I can help you with weather information. Please ask about any city."
        )

    except Exception as e:
        print("ERROR:", e)
        return ChatResponse(reply="Internal error occurred.")
