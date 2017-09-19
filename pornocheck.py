#-*-coding: utf-8 -*-
import Image
import os
import shutil
import sys

log = open('record.log', 'a')
log.write('\nchecking...\n')
print '\nchecking...\n'
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('jpg') or file.endswith('jpeg') or file.endswith('gif') or file.endswith('png') or file.endswith('bmp'):
            item = root + '/' + file
            #print item
            try:
                img = Image.open(item).convert('YCbCr')
            except:
                print item + 'error'
                log.write('%s ERROR\n'%item)
                break
            w, h = img.size
            data = img.getdata()
            cnt = 0
            for i, ycbcr in enumerate(data):
                y, cb, cr = ycbcr
                if 86 <= cb <= 117 and 140 <= cr <= 168:
                #if 86 <= cb <= 127 and 130 <= cr < 168:
                    cnt += 1
            if cnt > w * h * 0.3:
                yep = item + ' is a porno\n'
                print yep
                log.write(yep)
                if os.path.exists('./suckout'):
                    if os.path.exists('./suckout/%s'%file):
                        exist = "%s exists in suckout already\n"%item
                        print exist
                        log.write(exist)
                    else:
                        shutil.copy(item, './suckout/')
                else:
                    os.mkdir('./suckout')
                    shutil.copy(item, './suckout/')
            else:
                nope = item + ' is not a porno\n'
                print nope
                log.write(nope)
                #print '%s %s a porn image.'%(item, 'is' if cnt > w * h * 0.3 else 'is not')
log.write('finished.\n')
print 'finished.\n'
log.close()            
