import json
import random
from fastapi import FastAPI, HTTPException
from services import CHATGPT_URL, FORUM_URL, USER_URL
import httpx
import asyncio
import requests


app = FastAPI()

@app.get("/aggregate")
async def aggregate_data():
    async with httpx.AsyncClient() as client:
        try:

            service1_response = await client.get(CHATGPT_URL)
            service2_response = await client.get(FORUM_URL)
            service3_response = await client.get(USER_URL)

            print('response')
            print(service1_response)
            print('response')
            print(service3_response)
            service1_data = service1_response.text
            service2_data = service2_response.json()
            service3_data = service3_response.text

            aggregated_data = {
                "service1_data": service1_data,
                "service2_data": service2_data,
                "service3_data": service3_data
            }
            return aggregated_data

        except json.decoder.JSONDecodeError:
            raise HTTPException(status_code=500, detail="Invalid JSON received from one of the services")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


async def get_service_data(client, url):
    response = await client.get(url)
    print(f"Received response from {url}: {response.status_code}")
    if 'json' in response.headers.get('Content-Type', ''):
        return response.json()
    return response.text

@app.get("/aggregate_asynch")
async def aggregate_data():
    async with httpx.AsyncClient() as client:
        urls = [
            CHATGPT_URL, 
            FORUM_URL, 
            USER_URL
        ]

        for _ in range(10):
            shuffled_urls = random.sample(urls, len(urls))
            tasks = [get_service_data(client, url) for url in shuffled_urls]
            results = await asyncio.gather(*tasks)
            aggregated_data = {
                "service1_data": results[0],
                "service2_data": results[1],
                "service3_data": results[2]
            }
            print(f"Aggregated Data: {aggregated_data}")

        return aggregated_data

def get_data_synchronously():
    urls = [
        CHATGPT_URL, 
        FORUM_URL, 
        USER_URL
    ]

    for url in urls:
        response = requests.get(url)
        print(f"Received response from {url}: {response.status_code}")

get_data_synchronously()