import requests
from bs4 import BeautifulSoup

url = "https://www.chess.com/home"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

