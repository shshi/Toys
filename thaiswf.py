#!/usr/bin/python
#-*- coding: utf-8 -*-

#===========================================================
# File Name: thaiswf.py
# Author：shshi
# E-mail:553102057@qq.com
# Created Time: 2014-06-25
# Version: 1.0
# Description: 
# Copyright: Wayne_Shih
#===========================================================
import re
import urllib
#url="http://www.taiguoyu.com/news/view.asp?id=3711"
page = urllib.urlopen("http://www.taiguoyu.com/news/view.asp?id=3711").read()
reg = r'<param name="movie" value="(.*?)"><fr>'
link_re = re.compile(reg)
link_list = re.findall(link_re,page)

prefix = "http://www.taiguoyu.com/news/"
for i in link_list:
    name = i.split("/")[1]
    print "processing %s"%name
    urllib.urlretrieve(prefix+i, "./thaiswf/%s"%name)

