
import asyncio

from app.services.rag import answer_question


async def main():

    print("Testing complete RAG pipeline...")

    question = "Can I pay my tuition fees in installments?"

    try:

        result = await answer_question(question)

        print("\n========== CHATBOT RESPONSE ==========")

        print("\nQuestion:")
        print(question)

        print("\nAnswer:")
        print(result["answer"])

        print("\nConfidence:")
        print(result["confidence"])

        print("\nSources:")

        for source in result["sources"]:
            print("-", source["title"])
            print("  Last verified:", source["last_verified"])
            print("  Potentially outdated:", source["stale"])

    except Exception as error:

        print("\nRAG TEST FAILED:")
        print(type(error).__name__, str(error))


if __name__ == "__main__":
    asyncio.run(main())
