import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/zhongwen/trad/topics/c83plve5vmjt"

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")
titles = soup.find_all("span", {"class": "lx-stream-post__header-text gs-u-align-middle"})

title_list = []
for title in titles:
    title_list.append(title.getText())

print(title_list)