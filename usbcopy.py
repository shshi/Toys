#-*- coding: utf-8 -*-
import time
import os
import shutil

usb_path = "I:"
print "ready"
while not os.path.exists(usb_path):
	time.sleep(3)
print "now"
os.system("FileList.bat")
shutil.copytree(usb_path, 'C:/usbcopy')
print "done"
