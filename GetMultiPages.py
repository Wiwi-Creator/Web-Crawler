import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/MobileComm/index.html"
print("上一頁URL為:"+ url)
for i in range(3):
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")
    sel  = soup.select("div.title a") # 標題
    u    = soup.select("div.btn-group.btn-group-paging a")
    print("本頁URL為:"+ url)
    url  = "https://www.ptt.cc/" + u[1]["href"] #組合"上一頁"的網址

for s in sel: #印出網址及標題
    print(s["href"],s.text)