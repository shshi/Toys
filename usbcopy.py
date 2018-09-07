#-*- coding: utf-8 -*-
import time
import os
import shutil

usb_path = "G:"
while not os.path.exists(usb_path):
	time.sleep(3)
print "now"
shutil.copytree(usb_path, 'C:/usbcopy')
