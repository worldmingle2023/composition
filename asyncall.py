import asyncio
import aiohttp
from services import CHATGPT_URL, FORUM_URL, USER_URL

microservices = [
    CHATGPT_URL, 
    FORUM_URL, 
    USER_URL
]

async def async_call_microservice(session, url):
    async with session.get(url) as response:
        response_text = await response.text()
        print(f"Received response from {url}: {response_text}")
        print("-----------------------------------------------")

async def asynchronous_calls():
    async with aiohttp.ClientSession() as session:
        tasks = [async_call_microservice(session, url) for url in microservices]
        await asyncio.gather(*tasks)

# Repeat 10 times
for _ in range(5):
    asyncio.run(asynchronous_calls())

for _ in range(5):
    asyncio.run(asynchronous_calls())