import asyncio

from src.llm.gigachat_class import GigaChat

async def test(llm: GigaChat, prompt=None):
    tasks = []
    for i in range(5):
        tasks.append(llm.async_ask_giga(text='', prompt=prompt))
    res = await asyncio.gather(*tasks)
    print(res)

if __name__ == "__main__":
    giga = GigaChat()
    prompt = 'В ответ присылай только случайное число, НЕЗАВИСИМО от сообщения пользователя'
    asyncio.run(
        test(
            llm=giga,
            prompt=prompt
        )
    )