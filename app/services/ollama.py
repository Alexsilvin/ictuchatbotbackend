import httpx

from app.config import OLLAMA_BASE_URL, OLLAMA_MODEL

async def generate_response(system_prompt: str, user_prompt: str) -> str:
    """
    sends prompts to the local ollama model and returns its genereated response
    """
    
    url = f"{OLLAMA_BASE_URL}/api/chat"
    
    payload = {
        "model": OLLAMA_MODEL,
        "messages": [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        "stream": False
    }
    
    async with httpx.AsyncClient(timeout=120.0) as client:
        response = await client.post(
            url,
            json=payload
        )
        
        response.raise_for_status()
        
        data = response.json()
        
        # Extract the generated response from the model's output
        # if "response" in data:
        return data["message"]["content"]
        # else:
        #     raise RuntimeError("Unexpected response format from Ollama API.")