
import httpx

from app.config import ICTUKB_BASE_URL, ICTUKB_API_KEY


async def search_knowledge_base(question: str):
    if not ICTUKB_API_KEY:
        raise RuntimeError("ICTUKB_API_KEY is not configured.")

    url = f"{ICTUKB_BASE_URL}/v1/search"

    headers = {
        "X-API-Key": ICTUKB_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "query": question,
        "top_k": 5
    }

    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.post(
            url,
            headers=headers,
            json=payload
        )

        response.raise_for_status()

        return response.json()
