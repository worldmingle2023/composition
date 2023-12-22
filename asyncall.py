import asyncio
import aiohttp

microservices = [
    "http://ec2-3-22-186-8.us-east-2.compute.amazonaws.com:5000/",
    "https://1qajdtdqj3.execute-api.us-west-2.amazonaws.com",
    "https://cloudcomputing-worldmingle.ue.r.appspot.com/"
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

microservices = [
    "https://cloudcomputing-worldmingle.ue.r.appspot.com/",
    "https://1qajdtdqj3.execute-api.us-west-2.amazonaws.com",
     "http://ec2-3-22-186-8.us-east-2.compute.amazonaws.com:5000/",
]
for _ in range(5):
    asyncio.run(asynchronous_calls())