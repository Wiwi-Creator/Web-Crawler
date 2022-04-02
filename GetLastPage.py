import requests
from bs4 import BeautifulSoup

a = requests.get("https://www.ptt.cc/bbs/MobileComm/index.html") #將此網頁HTML 利用get()取下
soup = BeautifulSoup(a.text,"html.parser") #將網頁資料存入html.parser
sel  = soup.select("div.btn-group.btn-group-paging a")  #"上一頁"按鈕的標籤</a>
url  = "https://www.ptt.cc/" + sel[1]["href"] #組合"上一頁"的網址

print("上一頁網址為:" + url)