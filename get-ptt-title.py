#抓取ptt電影版網頁原始碼
import urllib.request as req
import requests
import bs4

url="https://www.ptt.cc/bbs/movie/index.html"

request=requests.get(url).text

root=bs4.BeautifulSoup(request,"html.parser")
titles=root.find_all("div",class_="title") #尋找所有 class="title" 的 div 標籤
print(root.title.string)
for title in titles: #如果標題含有 a 標籤(沒被刪除) ， 印出來
    if title.a != None:
        print(title.a.string)


#解析網頁原始碼，取得每篇文章的標題