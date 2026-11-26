
import asyncio

from app.config import (
    ICTUKB_API_KEY,
    ICTUKB_BASE_URL,
    OLLAMA_MODEL
)

from app.services.ictukb import search_knowledge_base


async def main():
    print("Checking ICTUKB configuration...")

    print("API key configured:", bool(ICTUKB_API_KEY))
    print("ICTUKB URL:", ICTUKB_BASE_URL)
    print("AI model:", OLLAMA_MODEL)

    if not ICTUKB_API_KEY:
        print("\nERROR: ICTUKB_API_KEY is missing.")
        return

    print("\nSending test question to ICTUKB...")

    question = "Can I pay my tuition fees in installments?"

    try:
        result = await search_knowledge_base(question)

        print("\nSUCCESS! ICTUKB responded.")

        print("\nConfidence:", result.get("confidence"))

        results = result.get("results", [])

        print("Number of results:", len(results))

        for index, item in enumerate(results, start=1):
            document = item.get("document", {})

            print(f"\nResult {index}")
            print("Title:", document.get("title"))
            print("Category:", document.get("category"))
            print("Text:", item.get("text", "")[:300])

    except Exception as error:
        print("\nICTUKB TEST FAILED:")
        print(type(error).__name__, str(error))


if __name__ == "__main__":
    asyncio.run(main())
