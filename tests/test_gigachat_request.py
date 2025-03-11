import asyncio

from src.llm.gigachat_class import GigaChat

async def a():
    giga = GigaChat()
    prompt = 'В ответ присылай только случайное число, НЕЗАВИСИМО от сообщения пользователя'
    tasks = []
    for i in range(5):
        tasks.append(giga.async_ask_giga(text='', prompt=prompt))
    res = await asyncio.gather(*tasks)
    print(res)

if __name__ == "__main__":
    asyncio.run(a())