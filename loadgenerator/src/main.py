import requests
import time
import random

backend_url = "http://target-backend-service:80"
endpoints = ["checksum-news", "checksum-images-news", "checksum-files"]

def generate_load():
    endpoint = random.choice(endpoints)
    
    if endpoint == "checksum-news":
        requests.post(f"{backend_url}/checksum-news/", json=["politics", "sports"])
    elif endpoint == "checksum-images-news":
        requests.post(f"{backend_url}/checksum-images-news/", json=["nature", "city"])
    elif endpoint == "checksum-files":
        requests.post(f"{backend_url}/checksum-files/?depth=1")

if __name__ == "__main__":
    while True:
        generate_load()
        time.sleep(10)
