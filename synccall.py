import requests
from services import CHATGPT_URL, FORUM_URL, USER_URL

microservices = [
    CHATGPT_URL, 
    FORUM_URL, 
    USER_URL
]

def call_microservice(url):
    response = requests.get(url)
    print(f"Received response from {url}: {response.text}")
    print("-----------------------------------------------")

def synchronous_calls():
    for url in microservices:
        call_microservice(url)

synchronous_calls()
