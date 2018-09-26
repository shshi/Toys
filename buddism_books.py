#!/usr/bin/python
#-*- coding: utf-8 -*-

#===========================================================
# File Name: Buddism.py
# Author：Sha0hua
# E-mail:553102057@qq.com
# Created Time: 2017-01-10
# Version: 1.0
# Description: 
# Copyright: Sha0hua
#===========================================================
import re
import urllib
import os
import time

print "\nHi, this is Shaohua, the writer of this script, thanks for using it. If there's any problem plz send me email: cell.fantasy@qq.com. Enjoy Learning!\n"
page = urllib.urlopen("http://urbandharma.org/pdf4/").read()
reg = r'<a href="(.*?.pdf)">'
link_re = re.compile(reg)
link_list = re.findall(link_re,page)

prefix = "http://urbandharma.org"
for i in link_list:
    name = i.split("/")[2]
    if os.path.exists("./Buddism Books/"):
        if os.path.exists("./Buddism Books/%s"%name):
            print "%s exists already"%name
        else:
            print "Downloading %s"%name
            urllib.urlretrieve(prefix+i, "./Buddism Books/%s"%name)
    else:
        os.makedirs("./Buddism Books/")    
        print "Downloading %s"%name
        urllib.urlretrieve(prefix+i, "./Buddism Books/%s"%name)

print "Done"
time.sleep(3)
