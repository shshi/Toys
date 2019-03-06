#-*- coding: utf-8 -*-
#===========================================================
# Author：Sha0hua
# E-mail:shi.sh@foxmail.com
# Modified Date: 2019-01-11
#===========================================================
import re
import requests
#import urllib.request as u
#import urllib.parse as p

def getList():
    
    #usrname = input('Please input your Douban username: ')
    #password = input('Please input your password: ')
    #DoubanID = input('Please input the Douban id you wish to check: ')
    
    usrname="shishaohua7@163.com"
    password="Ssh19198918"
    DoubanID="bzjiang_n"
    
    logname='%s.log'%DoubanID
    f = open(logname,'w',encoding='utf-8')
    
    s = requests.session()
    headers_login = {"Host":"accounts.douban.com", "Connection":"keep-alive", "Content-Length":"73",
                "Upgrade-Insecure-Requests":"1", "Origin":"https://accounts.douban.com", "X-Requested-With":"XMLHttpRequest",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
                "Accept":"application/json",
                "Content-Type": "application/x-www-form-urlencoded", "Referer":"https://accounts.douban.com/passport/login",
                "Accept-Encoding":"gzip, deflate, br",
                "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8"
                }
    headers_book = {"Host":"book.douban.com", "Connection":"keep-alive", "Cache-Control":"max-age=0",
                "Upgrade-Insecure-Requests":"1", 
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "Referer":"https://www.douban.com/people/"+DoubanID+"/",
                "Accept-Encoding":"gzip, deflate, br",
                "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8"
                }
    headers_movie = {"Host":"movie.douban.com", "Connection":"keep-alive", "Cache-Control":"max-age=0",
                "Upgrade-Insecure-Requests":"1", 
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "Referer":"https://www.douban.com/people/"+DoubanID+"/",
                "Accept-Encoding":"gzip, deflate, br",
                "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8"
                }
    login_data = {"ck":"", "name":usrname, "password":password, "remember":"false", "ticket":""}

    req = s.post("https://accounts.douban.com/j/mobile/login/basic", data=login_data, headers=headers_login)

    urlList=["https://book.douban.com/people/"+DoubanID+"/wish",
            "https://book.douban.com/people/"+DoubanID+"/collect",
            "https://book.douban.com/people/"+DoubanID+"/do",
            "https://movie.douban.com/people/"+DoubanID+"/wish",
            "https://movie.douban.com/people/"+DoubanID+"/collect",
            "https://movie.douban.com/people/"+DoubanID+"/do"]
    
    def loopBook():
        req = s.get(i, headers=headers_book).text
        reg=r'<a href="https.*?title="(.*?)"'
        re_comp=re.compile(reg)
        list_all=re.findall(re_comp,req)
        
    def loopMovie():
        reg = r'<em>(.*?)</em>'
        #reg=r'<a href="https.*?<em>(.*?)</em>'
        re_comp=re.compile(reg)
        list_all=re.findall(re_comp,req)
        list_all.remove('{{= title}}')

    for i in urlList:
        num=0
        if "book" in i:
            if "wish" in i:
                print ("想看的书：")
                f.write("想看的书：\n")
                req = s.get(i, headers=headers_book).text
                
                reg=r'<a href="https.*?title="(.*?)"'
                re_comp=re.compile(reg)
                list_all=re.findall(re_comp,req)
                
                print (list_all)
                
                for item in list_all:
                    num+=1
                    f.write('%d. %s\n'%(num,item))

                while '后页&gt;</a>' in req:
                    prefix="https://book.douban.com"
                    re_comp=re.compile(r'<a href="(.*?)" >后页&gt;</a>')
                    postfix=re.findall(re_comp,req)
                    postfix=str(postfix[0])
                    nextpage=prefix+postfix
                    #print (nextpage)
                    req = s.get(nextpage, headers=headers_book).text
                    
                    reg=r'<a href="https.*?title="(.*?)"'
                    re_comp=re.compile(reg)
                    list_all=re.findall(re_comp,req)
                    
                    print (list_all)
                    for item in list_all:
                        num+=1
                        f.write('%d. %s\n'%(num,item))
                    #print ("yes!")
                else:
                    print ("fnished")
                    
            elif "collect" in i:
                print("读过的书：")
                f.write("\n读过的书：\n")
                req = s.get(i, headers=headers_book).text
                
                reg=r'<a href="https.*?title="(.*?)"'
                re_comp=re.compile(reg)
                list_all=re.findall(re_comp,req)
                
                print (list_all)

                for item in list_all:
                    num+=1
                    f.write('%d. %s\n'%(num,item))
                    
                while '后页&gt;</a>' in req:
                    prefix="https://book.douban.com"
                    re_comp=re.compile(r'<a href="(.*?)" >后页&gt;</a>')
                    postfix=re.findall(re_comp,req)
                    postfix=str(postfix[0])
                    nextpage=prefix+postfix
                    #print (nextpage)
                    req = s.get(nextpage, headers=headers_book).text
                    
                    reg=r'<a href="https.*?title="(.*?)"'
                    re_comp=re.compile(reg)
                    list_all=re.findall(re_comp,req)
                    
                    print (list_all)

                    for item in list_all:
                        num+=1
                        f.write('%d. %s\n'%(num,item))
                    
                    #print ("yes!")
                else:
                    print ("fnished")
                    
            else:
                print("正在读的书：")
                f.write("\n正在读的书：\n")
                req = s.get(i, headers=headers_book).text
                
                reg=r'<a href="https.*?title="(.*?)"'
                re_comp=re.compile(reg)
                list_all=re.findall(re_comp,req)
                
                print (list_all)

                for item in list_all:
                    num+=1
                    f.write('%d. %s\n'%(num,item))

                while '后页&gt;</a>' in req:
                    prefix="https://book.douban.com"
                    re_comp=re.compile(r'<a href="(.*?)" >后页&gt;</a>')
                    postfix=re.findall(re_comp,req)
                    postfix=str(postfix[0])
                    nextpage=prefix+postfix
                    #print (nextpage)
                    req = s.get(nextpage, headers=headers_book).text
                    
                    reg=r'<a href="https.*?title="(.*?)"'
                    re_comp=re.compile(reg)
                    list_all=re.findall(re_comp,req)
                    
                    print (list_all)
                    
                    for item in list_all:
                        num+=1
                        f.write('%d. %s\n'%(num,item))
                        
                    #print ("yes!")
                else:
                    print ("fnished")
                    
        else:
            if "wish" in i:
                print("想看的电影：")
                f.write("\n想看的电影：\n")
                req = s.get(i, headers=headers_movie).text
                
                reg=r'<em>(.*?)</em>'
                re_comp=re.compile(reg)
                list_all=re.findall(re_comp,req)
                list_all.remove('{{= title}}')
                
                print (list_all)
                
                for item in list_all:
                    num+=1
                    f.write('%d. %s\n'%(num,item))
                    
                while '后页&gt;</a>' in req:
                    prefix="https://movie.douban.com"
                    re_comp=re.compile(r'<a href="(.*?)" >后页&gt;</a>')
                    postfix=re.findall(re_comp,req)
                    postfix=str(postfix[0])
                    nextpage=prefix+postfix
                    #print (nextpage)
                    req = s.get(nextpage, headers=headers_movie).text
                    
                    reg = r'<em>(.*?)</em>'
                    #reg=r'<a href="https.*?<em>(.*?)</em>'
                    re_comp=re.compile(reg)
                    list_all=re.findall(re_comp,req)
                    list_all.remove('{{= title}}')
                    
                    print (list_all)
                    
                    for item in list_all:
                        num+=1
                        f.write('%d. %s\n'%(num,item))
                        
                    #print ("yes!")
                else:
                    print ("fnished")
                
            elif "collect" in i:
                print ("看过的电影：")
                f.write("\n看过的电影：\n")
                req = s.get(i, headers=headers_movie).text
                
                reg=r'<em>(.*?)</em>'
                re_comp=re.compile(reg)
                list_all=re.findall(re_comp,req)
                list_all.remove('{{= title}}')
                
                print (list_all)

                for item in list_all:
                    num+=1
                    f.write('%d. %s\n'%(num,item))
                
                while '后页&gt;</a>' in req:
                    prefix="https://movie.douban.com"
                    re_comp=re.compile(r'<a href="(.*?)" >后页&gt;</a>')
                    postfix=re.findall(re_comp,req)
                    postfix=str(postfix[0])
                    nextpage=prefix+postfix
                    #print (nextpage)
                    req = s.get(nextpage, headers=headers_movie).text
                    
                    reg = r'<em>(.*?)</em>'
                    #reg=r'<a href="https.*?<em>(.*?)</em>'
                    re_comp=re.compile(reg)
                    list_all=re.findall(re_comp,req)
                    list_all.remove('{{= title}}')
                    
                    print (list_all)
                    for item in list_all:
                        num+=1
                        f.write('%d. %s\n'%(num,item))
                    #print ("yes!")
                else:
                    print ("fnished")
            else:
                print("正在看的电影：")
                f.write("\n正在看的电影：\n")
                req = s.get(i, headers=headers_movie).text
                
                reg=r'<em>(.*?)</em>'
                re_comp=re.compile(reg)
                list_all=re.findall(re_comp,req)
                list_all.remove('{{= title}}')
                
                print (list_all)

                for item in list_all:
                    num+=1
                    f.write('%d. %s\n'%(num,item))
                
                while '后页 &gt;</a>' in req:
                    prefix="https://movie.douban.com"
                    re_comp=re.compile(r'<a href="(.*?)" >后页&gt;</a>')
                    postfix=re.findall(re_comp,req)
                    postfix=str(postfix[0])
                    nextpage=prefix+postfix
                    #print (nextpage)
                    req = s.get(nextpage, headers=headers_movie).text
                    
                    reg = r'<em>(.*?)</em>'
                    #reg=r'<a href="https.*?<em>(.*?)</em>'
                    re_comp=re.compile(reg)
                    list_all=re.findall(re_comp,req)
                    list_all.remove('{{= title}}')
                    
                    print (list_all)

                    for item in list_all:
                        num+=1
                        f.write('%d. %s\n'%(num,item))
                    
                    #print ("yes!")
                else:
                    print ("fnished")
    f.close()
   
getList()
