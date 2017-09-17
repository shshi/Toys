#!/usr/bin/python
# -*- coding: utf-8 -*-

#===========================================================
# File Name: notebacup.py
# Author：shshi
# E-mail:shishaohua7@163.com
# Created Time: 2014-05-31
# Version: 1.0
# Description: 
# Copyright: Wayne_Shih
#===========================================================

import os
import time
import shutil

#1.The files and directories to be backed up are specified in a list.
A=r'C:\Users\Administrator\Desktop\N.txt'
B=r'C:\Users\Administrator\Desktop\desknote.log'
C=r'C:\Users\Administrator\Documents\\bookmarks.html'
D=r'C:\Users\Administrator\Documents\\bookmarks*?.json'
source = [A,B,C,D]

#Copy files to a certain directory
#TGT_dir = ur'G:\D\noteBACKUP\\'
#for i in source:
#    shutil.copy(i,TGT_dir)

#2.The backup must be stored in a main backup directory
target_dir = r'G:\D\noteBACKUP\notebacup'

#3.The files are backed up into a zip file.
#4.The name of the zip archive is the current date and time
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.rar'

rar_path = r'C:\WinRAR.exe'

#5.We use the zip command (in Linux) to put the files in a zip archive
rar_command = rar_path + " a %s %s" %(target, ' '.join(source))
print ' '.join(source)
#if you backup a directory, use follow:
#rar_command = rar_path + " a -r %s %s" %(target, ' '.join(source))

#Run the backup
if os.system(rar_command) == 0:
    print('Successfull backup to', target)
else:
    print('Backup FAILED')
