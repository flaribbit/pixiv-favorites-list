# pixiv-favorites-list
爬取P站收藏夹保存为json格式

## 运行环境
```
pip install requests bs4
```

## 要修改的
* [第9行](https://github.com/flaribbit/pixiv-favorites-list/blob/master/main.py#L9) cookies，`PHPSESSID=` 填入自己的
* [第23行](https://github.com/flaribbit/pixiv-favorites-list/blob/master/main.py#L23) 总页数，可用 `总数/20` 估算.
