import requests
from bs4 import BeautifulSoup
from ..database import SessionLocal
from ..models import Item

def fetch_item_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Извлечение названия, описания и рейтинга
    name = soup.find("h1").text
    description = soup.find("p", class_="description").text
    rating = float(soup.find("span", class_="rating").text)

    return {"name": name, "description": description, "rating": rating}
