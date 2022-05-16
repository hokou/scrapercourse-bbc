import requests
from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
}

try:
    response = requests.get(
        "https://www.bbc.com/zhongwen/trad/topics/c83plve5vmjt",
        headers=headers, timeout=10)

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, "lxml")
        title = soup.find(
            "span", {"class": "lx-stream-post__header-text gs-u-align-middle"})

        if title:
            result = title.getText()
            print(result)

        else:
            print("元素不存在!")
            
    else:
        print("狀態碼非200!")

except Exception as e:
    print(str(e))