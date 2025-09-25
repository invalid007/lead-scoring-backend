# app/config.py

import os

# Openai API key 
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your_api_key_here")

# other globl constants
RULE_MAX_SCORE = 50
AI_MAX_SCORE = 50
