#-*-coding: utf-8 -*-
import os
import time

#format_get=input('请输入需要重命名的文件类型后缀名（例：jpg）：')
for fileList in os.walk('.'):
    #print (fileList)
    for i in fileList[-1]:
        #if (i.upper()[-4:]) in ['.JPG','JPEG','.NEF','.PNG','TIFF']:
        if '❤' not in i and i.upper()[-3:]!='.PY':
            print (i)
            #split_i=i.split('.')
            os.rename(i,i+'❤')
        else:
            os.rename(i,i.replace('❤',''))
print ('finished\n')
#time.sleep(3)
