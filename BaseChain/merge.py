from .utils import complete_prompt

async def merge_history(question, history):
    merge_template = open("templates/merge.txt", "r").read()
    prompt = merge_template.replace("${question}", question).replace("${history}", history)
    return await complete_prompt(prompt)
