#-*-coding: utf-8 -*-
import os
import time
from PIL import Image, ImageOps, ExifTags
def add_frame(): 
    for fileList in os.walk('.'):
        #print (fileList)
        for i in fileList[-1]:
            if (i.upper()[-4:]) in ['.JPG','JPEG','.PNG','TIFF']:
                print(i)
                image = Image.open(i) 
                img_width=image.size[0]
                img_height=image.size[1]
                if img_width>img_height:
                    frame_size=int(img_width*0.05)
                else:
                    frame_size=int(img_height*0.05)
                image = ImageOps.expand(image, (frame_size,frame_size,frame_size,frame_size), fill="white") 
                #auto_rotate(image)
                split_i=i.split('.')
                name_new=split_i[0]+'_f'+'.'+split_i[-1]
                image.save(name_new) 

def auto_rotate(img):
    try:
        for orientation in ExifTags.TAGS.keys() : 
            if ExifTags.TAGS[orientation]=='Orientation' : break 
        exif=dict(img._getexif().items())
        if   exif[orientation] == 3 : 
            img=img.rotate(180, expand = True)
        elif exif[orientation] == 6 : 
            img=img.rotate(270, expand = True)
        elif exif[orientation] == 8 : 
            img=img.rotate(90, expand = True)
    except:
        pass

if __name__ == "__main__": 
    add_frame() 
    print ('finished\n')
    time.sleep(3)



