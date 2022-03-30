import requests
from bs4 import BeautifulSoup

a = requests.get("https://www.ptt.cc/bbs/MobileComm/index.html") #將此網頁HTML 利用get()取下
print(a.text) #將網頁HTML印出
soup   = BeautifulSoup(a.text,"html.parser") #將網頁資料存入html.parser
sel = soup.select("div.title a")#取HTML標中的 <div class="title"></div> 中的<a>標籤存入sel

