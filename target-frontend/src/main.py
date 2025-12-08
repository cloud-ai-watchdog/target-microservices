from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()
templates = Jinja2Templates(directory="src/templates")

backend_url = "http://target-backend-release-target-backend-service"

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/checksum-news")
async def checksum_news():
    response = requests.post(f"{backend_url}/checksum-news/", json=["ai", "machine learning"])
    return response.json()

@app.post("/checksum-images")
async def checksum_images():
    response = requests.post(f"{backend_url}/checksum-images-news/", json=["cat", "dog"])
    return response.json()

@app.post("/checksum-files")
async def checksum_files():
    response = requests.post(f"{backend_url}/checksum-files/?depth=2")
    return response.json()
