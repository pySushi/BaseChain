import os
import aiohttp
from expr_eval import Parser

async def google_search(question):
    async with aiohttp.ClientSession() as session:
        async with session.get(
            f"https://serpapi.com/search?api_key={os.getenv('SERPAPI_API_KEY')}&q={question}"
        ) as response:
            res = await response.json()
            return (
                res.get("answer_box", {}).get("answer")
                or res.get("answer_box", {}).get("snippet")
                or res.get("organic_results", [{}])[0].get("snippet")
            )

async def calculator(input):
    return str(Parser.evaluate(input))

tools = {
    "search": {
        "description": "a search engine...",
        "execute": google_search,
    },
    "calculator": {
        "description": "Useful for getting the result...",
        "execute": calculator,
    },
}
