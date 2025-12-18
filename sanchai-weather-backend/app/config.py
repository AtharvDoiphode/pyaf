#This file loads and stores secret keys (API keys) required by the backend.
# Why this file exists
# Keeps API keys out of business logic
# Avoids hardcoding secrets
# Makes the app secure and scalable

from dotenv import load_dotenv  #Loads environment variables from a .env file.

import os  #used to access environment variables.

load_dotenv() #Reads the .env file and loads variables into memory.

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY") #Fetches the OpenRouter API key securely.
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY") #Fetches the weather API key.

