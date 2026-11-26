
import asyncio

from app.services.ollama import generate_response


async def main():
    print("Testing local Ollama model...")

    system_prompt = """
    You are a helpful ICT University assistant.
    Answer clearly and concisely. Only provide information related to ICT University. If the question is not related to ICT University, politely decline to answer.
    """

    user_prompt = """
    Explain what a university tuition installment is
    in simple terms.
    """

    try:
        answer = await generate_response(
            system_prompt,
            user_prompt
        )

        print("\nGemma's response:")
        print(answer)

    except Exception as error:
        print("\nOLLAMA TEST FAILED:")
        print(type(error).__name__, str(error))


if __name__ == "__main__":
    asyncio.run(main())
