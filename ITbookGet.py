#-*- coding: utf-8 -*-
#===========================================================
# Author：Sha0hua
# E-mail:shi.sh@foxmail.com
# Modified Date: 2019-01-11
#===========================================================
import re
import requests
import time
import json
from lxml import etree

def getPSW(bookLink):
     
    s = requests.session()

    headers_resp={"Host":"dt4.8tupian.com",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0",
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                "Accept-Encoding":"gzip, deflate",
                "Connection":"keep-alive",
                "Referer":"%s"%bookLink,
                "Cookie":"UM_distinctid=17529b47191818-096515ad34e9c2-4c3f257b-1fa400-17529b471938f5; CNZZDATA1272667929=1564527789-1602721428-%7C1605659478; HBGKxy_ECGMAC=36733223a90",
                "Upgrade-Insecure-Requests":"1"
                }
    try:
        res = s.get("%s"%bookLink, headers=headers_resp,verify=False)
        html=res.content.decode("utf-8")
        Etree=etree.HTML(html)
        elementTXT=Etree.xpath('//*[@id="p2"]')[0]
        text = etree.tostring(elementTXT, pretty_print=True, method='html', encoding='utf-8').decode("utf-8")
        text=text[14:-5]
        print (text)
        with open('result.txt', 'a',encoding="utf-8") as file:
            file.write(bookLink+"\t"+text+"\n")
    except  Exception as e:
        print (e)   
def loop():
    with open('link_list.txt','r') as fp:
        for bookLink in fp:
            try:
                bookLinkORG=bookLink.strip().strip('\n')
                print (bookLinkORG)
                n=40
                while n<100:
                    bookLink=bookLinkORG+"8_t=%d"%n
                    getPSW(bookLink)
                    #time.sleep(3)
                    n+=1
            except Exception as e:
                print ('\nERROR occured from processing %s\n'%bookLink)
                with open('Book_Download_Error.log','a') as er:
                    er.write(bookLink+'   '+str(e)+'\n')
                continue

loop()
