#!coding=utf-8
#Description: python 匹配从文本里面匹配相应的邮箱
import re
import sys
 
 
def compile_mail(file_path):
 
    #匹配想要的邮箱,去除不想要的内容
     
    address = re.compile(
    '''
    (?![\w\d.+]+@139.com)  #去除不想要的邮箱
    [\w\d.+]+   #匹配前缀
    @   
    ([\w\d.]+\.)+  #匹配域名
    com  #匹配结尾
    ''',
    re.UNICODE | re.VERBOSE)
 
    with open(r'c:\333.txt') as fd:
        for x in fd:
            match = address.search(x)
            if match:
                print match.group()
 
 
if __name__ == '__main__':
 
    file_path = sys.argv[1]
    compile_mail(file_path)
