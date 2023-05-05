import os
import asyncio
from dotenv import load_dotenv
from BaseChain import answer_question, merge_history

load_dotenv()

async def main():
    history = ""

    while True:
        question = input("How can I help? ")

        if history:
            question = await merge_history(question, history)

        answer = await answer_question(question)
        print(answer)

        history += f"Q: {question}\nA: {answer}\n"

if __name__ == "__main__":
    asyncio.run(main())
