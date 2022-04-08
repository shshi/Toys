#-*- coding: utf-8 -*-

with open("header_conv.txt","w") as c:
    with open("header.txt", "r") as f:
        for line in f.readlines():
            line=line.strip().split(":")
            #print (line)
            new_line='"'+line[0]+'":'+'"'+line[1]+'",\n'
            print (new_line)
            c.write(new_line)


