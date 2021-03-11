#-*-coding: utf-8 -*-
import os
import time

format_get=input('此脚本用来给文件名末尾批量添加❤\n请输入需要重命名的文件类型后缀名（例：jpg）：')
for fileList in os.walk('.'):
    #print (fileList)
    for i in fileList[-1]:
        #if (i.upper()[-4:]) in ['.JPG','JPEG','.NEF','.PNG','TIFF']:
        if (i.upper()[-4:]) in '.'+format_get.upper():
            print (i)
            split_i=i.split('.')
            os.rename(i,split_i[0]+'❤'+'.'+split_i[-1])
print ('finished\n')
time.sleep(3)
