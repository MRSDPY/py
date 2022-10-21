from ast import parse
import json
from urllib.request import urlretrieve
import pickle
import os

lname = "border-crossing.json"
parse = os.path.join(os.path.dirname(__file__),'parse.txt')
url = "https://faculty.cs.niu.edu/~dakoop/cs503-2022fa/a3/border-crossing.json"

def download_data():
  if not os.path.exists(lname):
    urlretrieve(url, lname)

def get_data():
  temp = {}
  parse_data()
  with open(parse, "rb") as f:
    temp = pickle.load(f)
  return temp

def parse_data():
  if not os.path.exists(parse):
    download_data()

    data = json.load(open(lname))
    temp = {sub['Port Code'] : sub for sub in data}
  
    with open(parse, "wb") as f:
      pickle.dump(temp, f)
