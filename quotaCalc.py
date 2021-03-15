#-*- coding: utf-8 -*-
import csv

def x_3():
    d = 0
    (range_a, range_b, range_c, quota_a, quota_b, quota_c)=(8,15,20,27120,17560,9560)
    for a in range(range_a):
        for b in range(range_b):
            for c in range(range_c):
                if 290000< (quota_a*a + quota_b*b +quota_c*c) <310000 and a<b<c:
                    d += 1
                    print("x_3 第%d个解为:(一等%d,二等%d,三等%d)"%(d,a,b,c))
                    data.append([a,b,c])
    print("the end")


def writecsv():	
    with open('quotaResult.csv', 'a', newline='') as csvfile:
        writer  = csv.writer(csvfile)
        for row in data:
            writer.writerow(row)

data=[['一等','二等','三等']]
x_3()
writecsv()
