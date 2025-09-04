import os
from dotenv import load_dotenv

# import env variables from .env
load_dotenv()

# Now pull all the env variables into python variables using os
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Choose a model from Groq cloud sites - goto console.groq.com/docs/models
MODEL_NAME = "llama-3.1-8b-instant"
