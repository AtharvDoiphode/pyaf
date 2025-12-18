#Defines input and output structure for API requests.
# Why this file exists
# Enforces data validation
# Prevents invalid inputs
# Enables auto documentation in FastAPI

from pydantic import BaseModel  #Pydantic is used for data validation and settings management.
#Base class for defining data models with validation.
class ChatRequest(BaseModel): #Defines the request body structure.
    message: str  #User's input message for the chatbot.

class ChatResponse(BaseModel): #Defines API response structure.
    reply: str  #Chatbot's response message.