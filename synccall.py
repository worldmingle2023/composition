import requests

microservices = [
    "http://ec2-3-22-186-8.us-east-2.compute.amazonaws.com:5000/",
    "https://1qajdtdqj3.execute-api.us-west-2.amazonaws.com"

]

def call_microservice(url):
    response = requests.get(url)
    print(f"Received response from {url}: {response.text}")

def synchronous_calls():
    for url in microservices:
        call_microservice(url)

synchronous_calls()
