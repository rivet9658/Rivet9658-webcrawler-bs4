#抓取ptt八卦版網頁原始碼
import urllib.request as req
import bs4

#顯示單一頁面多個標題，並回傳上一頁網址
def getData(url):

    #讓爬蟲看起來像是一般使用者
    #建立一個 Request 物件，附加 Request Headers 的資訊
    request=req.Request(url, headers={
        "cookie":"over18=1",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    #顯示單一頁面多個標題
    root=bs4.BeautifulSoup(data,"html.parser") #讓 BeautifulSoup 幫我們解析 HTML 格式的文件
    titles=root.find_all("div",class_="title") #尋找所有 class="title" 的 div 標籤
    for title in titles: #如果標題含有 a 標籤(沒被刪除) ， 印出來
        if title.a != None:
            print(title.a.string)

    #抓取上一頁連結
    nextlink=root.find("a", string="‹ 上頁") #找到內文是 < 上頁 的 a 標籤
    return nextlink["href"] #回傳上一頁的網址

#主程式: 顯示多個頁面的多個標題
pageURL="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
while count < 5:
    pageURL="https://www.ptt.cc"+getData(pageURL)
    count+=1
