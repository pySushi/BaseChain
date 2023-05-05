import os
from .tools import tools
from .utils import complete_prompt

async def answer_question(question):
    prompt_template = open("templates/prompt.txt", "r").read()
    prompt = prompt_template.replace("${question}", question).replace(
        "${tools}",
        "\n".join([f"{name}: {tool['description']}" for name, tool in tools.items()])
    )

    while True:
        response = await complete_prompt(prompt)
        prompt += response

        action = response.split("Action: ")[1].split("\n")[0].strip() if "Action: " in response else None

        if action:
            action_input = response.split('Action Input: ')[1].split('\n')[0].strip()
            result = await tools[action].execute(action_input)
            prompt += f"Observation: {result}\n"
        else:
            return response.split("Final Answer: ")[1].split("\n")[0].strip()
