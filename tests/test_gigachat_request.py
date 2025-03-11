import asyncio

from src.llm.gigachat_class import GigaChat
from src.llm.prompts import TAB_FACT_SYSTEM_PROMPT

from tests.test_md_api import test_html_table, statement

human_message_template = """
Таблица: {table}
Утверждение: {statement}
"""

async def test(llm: GigaChat, text, prompt):
    tasks = []
    for i in range(1):
        tasks.append(llm.async_ask_giga(text=text, prompt=prompt))
    res = await asyncio.gather(*tasks)
    return res

if __name__ == "__main__":
    giga = GigaChat()
    prompt = TAB_FACT_SYSTEM_PROMPT
    res = asyncio.run(
        test(
            llm=giga,
            text=human_message_template.format(table=test_html_table, statement=statement),
            prompt=prompt
        )
    )
    # print(res[0])
    print(res)