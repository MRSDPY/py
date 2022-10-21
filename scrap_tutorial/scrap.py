from bs4 import BeautifulSoup
import requests
import pandas as pd


final_data = {}
index = 0
url = "https://www.programmableweb.com/category/all/apis"

responce = requests.get(url)

scrap = BeautifulSoup(responce.content, 'html.parser')

table = scrap.find_all('tr')

for data in table[1:]:
    a = "https://www.programmableweb.com" + data.find('a').get('href') if data.find('a').get('href') else "N/A"
    des = data.find(class_="views-field views-field-search-api-excerpt views-field-field-api-description hidden-xs visible-md visible-sm col-md-8").get_text() if data.find(class_="views-field views-field-search-api-excerpt views-field-field-api-description hidden-xs visible-md visible-sm col-md-8").get_text() else "N/A"
    api_name = data.find('a').get_text() if data.find('a').get_text() else "N/A"
    category = data.find(class_="views-field views-field-field-article-primary-category").get_text() if data.find(class_="views-field views-field-field-article-primary-category").get_text() else "N/A"

    # print("\n Api name = ", api_name, "\n url = ", a, "\n category = ", category, "\n des = ", des)
    index += 1
    final_data[index] = [api_name, a, category, des]


final = pd.DataFrame.from_dict(final_data, orient='index', columns=["Api_name", "Api_URL", "Category", "Description"])

final.to_csv('my_scrap.csv')
