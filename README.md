# Web Crawler 網路爬蟲

***
#### Definition :
```markdown

模擬使用者的行為，發出一個請求後把收到的資料攔截起來

而此行為其實就是利用程式網站上面的資料(多筆)複製下來，不僅是文字還有圖片。

而我們平常肉眼所見的網頁和爬蟲所見(網頁原始碼)有所不同!

較直白的說法就是讓瀏覽器透過去指定"網址"索取資料 ，並請求網址的Server回傳資料。 而這便是Python爬蟲的精隨!

註:可按F12,檢視該網頁之HTML語法

```
***

#### Mode of Operation :
```markdown

網路的基本架構，分為用戶端(Client)及伺服端(Server)。

其中，用戶端(Client)就是使用者瀏覽網頁的裝置(例：本機電腦)，當使用者點擊網頁時，
就代表請求(Request)的動作，存取該網頁連結的伺服端(Server)，
而伺服端(Server)接收連結得知使用者所要看的網頁後，將內容回應(Response)給用戶端(Client)。

```

#### Struction of Web  :
```markdown

網頁是由許多的標籤(Tag)與元素(Elements)組成，並且具有階層式的結構，
所以Python網頁爬蟲就需要透過定位，來取得所需的元素(Elements)。

Python網頁爬蟲取得元素(Elements)後，就可以利用套件及框架，
爬取其中的資料，也就是去掉元素(Elements)中的HTML標籤(Tag)。
   
```   
***   
#### Model :

```markdown
BeautifulSoup4
   
   ● 說明:借助網頁結構的特性來解析網頁的工具，可透過指令提取HTML的元素(易入門)
   ● 指令: pip install beautifulsoup4    
   
requests
   ● 說明:對網頁發出請求的模組，可實現對網頁做get、post等HTTP協定之行為。    
   ● 指令: pip install requests
   
Selenium
   ● 說明:擁有自動化測試及爬取功能，可透過Javascript爬取，非常適合需要滾動卷軸做動態載入的網站(EX:電子商務或社群)。    
   ● 指令: pip install requests   

Scrapy
   ● 說明:爬取速度更快，也有非同步的功能，適合爬取大量資料及大型爬蟲專案。
   ● 指令: pip install requests   
   
```
***
#### Process :

```markdown

```
***
#### Basic Web Crawer : 
   
 [01.基礎爬蟲HTML(PTT)](https://github.com/Wiwi-Creator/Web-Crawler/blob/main/GetMulityPages.ipynb) 
 
 [02.基礎爬蟲Picture(Dcard)](https://github.com/Wiwi-Creator/Web-Crawler/blob/main/GetPic.ipynb)

 [03.爬蟲練習(Etoday新聞雲)](https://github.com/Wiwi-Creator/Web-Crawler/blob/main/HTMLpractice.ipynb)
 


