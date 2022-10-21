from bs4 import BeautifulSoup
import requests


url = "https://ncov2019.live/"

responce = requests.get(url)

scrap = BeautifulSoup(responce.content, 'html.parser')

find_data = scrap.find_all("tbody")[2].find_all("tr")
# print(find_data)


for data in find_data:
    print(data.get_text().split("\n"))

