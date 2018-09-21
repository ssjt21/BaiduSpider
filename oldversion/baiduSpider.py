# -*- coding: utf-8 -*-

"""
@author:随时静听
@file: baiduSpider.py
@time: 2018/09/21
@email:wang_di@topsec.com.cn
"""
import requests

from bs4 import  BeautifulSoup



#请求UA设置,
headers={
"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
}
#页数爬去设置
pages=15
#搜索关键子设置
keyword="inurl:?.asp学校"

#获取页面内容
def getContent(url):
    content=""
    if url:
        try:
            req=requests.get(url,headers=headers)
            content=req.content
        except:
            #这里可以打开文件请求失败的URL写入文件
            print "[!]  Get content failed: "+url
            print "[!] Statu Code:"+req.status_code

    return content

#爬去页面目标数据 (url_lst,next_page_url)
def parseContent(content):
    #存储搜索出来的URL
    a_links=[]
    next_page_link=""
    if content:
        soup=BeautifulSoup(content, 'html.parser')
        body=soup.find_all(id="content_left")
        if not body:
            return
        body= body[0]
        h3_lst=body.find_all('h3')

        for h3 in h3_lst:
            a_links.append(h3.a.get('href',""))

        page=soup.find_all(id="page")
        page= page[0] if page else []
        if not page:
            return















if __name__ == '__main__':
    pass