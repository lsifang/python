import json
import requests
from bs4 import BeautifulSoup
import pandas
import xlwt
import sqlite3
def linksurl(url):
    result=[]
    res=requests.get(url)
    # res.encoding='utf-8'
    jd=json.loads(res.text.lstrip(' data_callback(').rstrip(')'))
    for liurl in jd:
        result.append(comenturl(liurl['docurl']))
    return result
def comenturl(url):
    result={}
    res=requests.get(url)
    soup=BeautifulSoup(res.text,"html.parser")
    result['title']=soup.select('#epContentLeft h1')[0].text
    result['data']=(soup.select('.post_time_source')[0].text.strip()).rpartition(':')[0].rstrip('来源').strip()
    result['article']='\n'.join([p.text for p in soup.select('#endText p')])
    result['editer']=soup.select('.ep-editor')[0].text.lstrip('责任编辑：')
    return result
listurl='http://bendi.news.163.com/zhejiang/special/04098FBT/xinxiliu.js?callback=data_callback&_=1516588468946'
new_tatol=linksurl(listurl)
df=pandas.DataFrame(new_tatol)
df.to_excel('zhejiang.xlsx')
with sqlite3.connect('news.sqlite') as db:
    df.to_sql('zhejiang',con=db)

exit('the end')