 # LangChain agent
# What this file does
# Creates an LLM agent that decides:
# Whether to call the weather tool
# How to respond naturally 

from langchain.chat_models import ChatOpenAI
from langchain.agents import Tool, initialize_agent

from app.services.weather_tool import get_weather
from app.config import OPENROUTER_API_KEY

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    openai_api_key=OPENROUTER_API_KEY,
    openai_api_base="https://openrouter.ai/api/v1"
)

weather_tool = Tool(
    name="Weather Tool",
    func=get_weather,
    description="Fetch current weather for a city"
)

agent = initialize_agent(
    tools=[weather_tool],
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)
