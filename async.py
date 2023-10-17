# pip install requests
# pip install BS4
import asyncio
import requests
from bs4 import BeautifulSoup


url = 'https://finewords.ru/sluchajnye-citaty'
response = requests.get(url)
print(response.status_code)
htmlcode = response.text

soup = BeautifulSoup(htmlcode, 'lxml')
links_list = soup.findAll(class_ = 'contentbk')
print(links_list[0])
links = []
for string in links_list:
    parsedlinks = string.findAll('li')
    links.append(parsedlinks)

print(links)
db = []
for i_elem in links:
    for j_elem in i_elem:
        link = j_elem.find('a')
        if link is not None and 'href' in link.attrs:
            quote_link = dict()
            href = link['href']
            text = link.get_text()
            print(f"Link: {href}, Text: {text}")
            quote_link['Ссылка'] = href
            quote_link['Тема'] = text
            db.append(quote_link)

print(db)
