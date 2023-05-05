import os
import aiohttp

async def complete_prompt(prompt):
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://api.openai.com/v1/completions",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
            },
            json={
                "model": "text-davinci-003",
                "prompt": prompt,
                "max_tokens": 256,
                "temperature": 0.7,
                "stream": False,
                "stop": ["Observation:"],
            },
        ) as response:
            res = await
