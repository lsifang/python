import requests
from bs4 import BeautifulSoup
res=requests.get('http://www.julongyoule.cn')
res.encoding='gb2312'
soup=BeautifulSoup(res.text,'html.parser')
title=soup.select('.h2')
