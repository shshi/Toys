#-*- coding: utf-8 -*-
import time
import os
import shutil

usb_path = "D:"
print ("ready")
while not os.path.exists(usb_path):
	time.sleep(3)
print ("now")

if os.path.exists("FileList.txt"):
	print ("file")
	if not os.path.exists('C:/usbcopy'):
		os.mkdir('C:/usbcopy')
	with open ("FileList.txt",'r') as l:
		for f in l.readlines():
			try:
				shutil.copy(f.strip(), 'C:/usbcopy')
			except:
				with open ('C:/usbcopy/copy_err.log','a') as e:
					e.write(f)
					e.close()
				continue
elif os.path.exists("DirList.txt"):
	print ("dir")
	with open ("DirList.txt",'r') as l:
		for f in l.readlines():
			try:
				shutil.copytree(f.strip(), 'C:/usbcopy/%s'%f.split('\\')[-2])
			except Exception as err:
				with open ('C:/usbcopy/copy_err.log','a') as e:
					e.write(f)
					print (err)
					e.close()
				continue
else:
	print ("all")
	try:
		os.system("FileList.bat")
		shutil.copytree(usb_path, 'C:/usbcopy')
	except:
		print ("no 'FileList.bat' at current dir")
		shutil.copytree(usb_path, 'C:/usbcopy')
print ("done")
