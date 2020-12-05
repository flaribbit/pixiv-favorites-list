import requests
import json
from bs4 import BeautifulSoup


def getPage(n):
    res = requests.get("https://www.pixiv.net/bookmark.php?rest=show&p="+str(n), headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
        "cookie": "PHPSESSID=62xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx3A",
    })
    soup = BeautifulSoup(res.content)
    items = soup.select(".image-item")
    result = []
    for item in items:
        img = item.select_one("img")
        result.append((item.select_one(".title").text,
                       img["data-id"], img["data-tags"]))
    return result


# %%
result = []
for i in range(10):
    try:
        result += getPage(i+1)
        print("[OK ]", i+1)
    except:
        print("[Err]", i+1)
file = open("result.json", "w", encoding="utf8")
file.write(json.dumps(result, ensure_ascii=False))
file.close()
