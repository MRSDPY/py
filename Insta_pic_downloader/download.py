import requests
import bs4 as b
from random_ua import random_ua

ru = random_ua.UserAgent()
header = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
          "Accept-Encoding": "gzip, deflate, br",
          "Accept-Language": "en-US,en;q=0.5",
          "Cache-Control": "max-age=0",
          "Connection": "keep-alive",
          "DNT": "1",
          "Host": "www.instagram.com",
          "Upgrade-Insecure-Requests": "1",
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0",
          }

name = input("Enter Instagram profile name : ")

content = requests.get(name)
print(content)
extract_image = b.BeautifulSoup(content.text, "html.parser")

print(extract_image.prettify())

all_img = extract_image.find_all('img')

print(all_img)
