import os
from dotenv import load_dotenv

load_dotenv()

ICTUKB_API_KEY = os.getenv("ICTUKB_API_KEY",
        "")

ICTUKB_BASE_URL = os.getenv("ICTUKB_BASE_URL", "https://ictkb-api.ictkb-api-worker.workers.dev")

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "gemma3:1b")