import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
STT_MODEL = os.getenv("STT_MODEL")
LLM_MODEL = os.getenv("LLM_MODEL")

if not GROQ_API_KEY:
    raise ValueError("Clé API Groq manquante : vérifie ton fichier .env")

print("Configuration chargée avec succès")
print(f"STT_MODEL = {STT_MODEL}")
print(f"LLM_MODEL = {LLM_MODEL}")