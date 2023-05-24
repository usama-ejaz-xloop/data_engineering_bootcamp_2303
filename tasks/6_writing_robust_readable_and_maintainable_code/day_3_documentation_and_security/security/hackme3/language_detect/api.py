import requests
from bs4 import BeautifulSoup
from langdetect import detect
from fastapi import FastAPI


app = FastAPI()


@app.get("/detect_language")
def detect_language(url: str) -> dict:
    response = requests.get(url, timeout=2)
    content = response.content.decode("utf-8", errors="ignore")

    soup = BeautifulSoup(content)
    text = soup.get_text()

    language = detect(text)

    return {
        "text_without_tags": text,
        "language": language,
    }
