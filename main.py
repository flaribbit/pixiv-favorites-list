import requests
import json


def getPage(n: int):
    res = requests.get(f"https://www.pixiv.net/ajax/user/8046435/illusts/bookmarks?tag=&offset={n*100:d}&limit=100&rest=show&lang=zh", headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
        "cookie": "PHPSESSID=62xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx3A",
    })
    data = res.json()
    result = []
    for e in data["body"]["works"]:
        result.append((
            e["title"], e["id"], e["pageCount"],
            e["userName"], e["userId"], e["tags"]))
    return result


# print(getPage(0))
result = []
for i in range(20):
    try:
        result += getPage(i+1)
        print("[OK ]", i+1)
    except:
        print("[Err]", i+1)
with open("result.json", "w", encoding="utf8") as f:
    json.dump(result, f, ensure_ascii=False)
