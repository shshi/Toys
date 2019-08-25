#-*- coding: utf-8 -*-
#===========================================================
# Author：Sha0hua
# E-mail:shi.sh@foxmail.com
# Modified Date: 2019-03-26
# Version Description: fixed file naming bug
#===========================================================
import re
import requests
import csv
import os
import tkinter as tk
from tkinter.messagebox import *
from tkinter import *

#isbn='9781594480003'
class BookCheck: 
	def __init__(self,root):
		print ("initiating..." )

		frame=Frame(root)
		frame.pack()			
		#绘制label,grid()确定行列
		Label(frame, text="ISBN号:").grid(row=0,column=0)
		#导入输入框
		self.E1=Entry(frame,bd=2)
		#设置输入框的位置
		self.E1.grid(row=0, column=1, padx=10, pady=5)
		self.E1.bind('<Key-Return>',self.infoGet)
		Button(frame, text="清空页面", command=self.clean).grid(row=2, column=0, sticky=W, padx=10, pady=5)
		Button(frame, text="退出系统", command=root.quit).grid(row=2, column=1, sticky=E, padx=10, pady=5)
		self.infobox=tk.Text(root,height=35)#这里设置文本框高
		self.infobox.pack()

	def infoGet(self,Keyinfo):
		self.infobox.delete('0.0','end')
		try:
			self.isbn=self.E1.get()
			#print ('	-------\n')
			self.isbn.strip().strip('\n')
			self.E1.delete(0, END)
						
			s = requests.session()
			response = s.get("http://api.douban.com/book/subject/isbn/%s?apikey=0b6f04e23b1ae4a4224d0ea6b150adec"%self.isbn).text
			with open('log.log','w') as p:
				p.write(response)
		except:
			print ('-------\n查无此书')
			self.infobox.insert('end','-------\n查无此书\n')#insert
			return 'Error'
			
		bookDict={}
			
		re_title=re.compile(r'<db:attribute name="title">(.*?)</db:attribute>')
		title=str(re.findall(re_title,response)[0])
		bookDict.update(书名=title)

		try:
			re_title=re.compile(r'<db:attribute name="aka">(.*?)</db:attribute>')
			aka=str(re.findall(re_title,response)[0])
		except:
			aka=''
		bookDict.update(别名=aka)
		
		re_isbn13=re.compile(r'<db:attribute name="isbn13">(.*?)</db:attribute>')
		isbn13=str(re.findall(re_isbn13,response)[0])
		bookDict.update(ISBN=isbn13)
		
		try:
			re_author=re.compile(r'<db:attribute name="author">(.*?)</db:attribute>')
			author=str(re.findall(re_author,response)[0])
		except:
			author=''
		bookDict.update(作者=author)
		
		try:
			re_translator=re.compile(r'<db:attribute name="translator">(.*?)</db:attribute>')
			translator=str(re.findall(re_translator,response)[0])
		except:
			translator=''
		bookDict.update(译者=translator)

		try:
			re_pages=re.compile(r'<db:attribute name="pages">(.*?)</db:attribute>')
			pages=str(re.findall(re_pages,response)[0])
		except:
			pages=''
		bookDict.update(页数=pages)

		try:
			re_price=re.compile(r'<db:attribute name="price">(.*?)</db:attribute>')
			price=str(re.findall(re_price,response)[0])
		except:
			price=''
		bookDict.update(价格=price)

		try:
			re_publisher=re.compile(r'<db:attribute name="publisher">(.*?)</db:attribute>')
			publisher=str(re.findall(re_publisher,response)[0])
		except:
			publisher=''
		bookDict.update(出版社=publisher)
		
		try:
			re_pubdate=re.compile(r'<db:attribute name="pubdate">(.*?)</db:attribute>')
			pubdate=str(re.findall(re_pubdate,response)[0])
		except:
			pubdate=''
		bookDict.update(出版年=pubdate)

		try:
			re_binding=re.compile(r'<db:attribute name="binding">(.*?)</db:attribute>')
			binding=str(re.findall(re_binding,response)[0])
		except:
			binding=''
		bookDict.update(装帧=binding)
			
		try:
			re_author_intro=re.compile(r'<db:attribute name="author-intro">(.*?)</db:attribute>')
			author_intro=str(re.findall(re_author_intro,response)[0])
		except:
			author_intro=''
		bookDict.update(作者简介=author_intro)

		try:
			re_summary=re.compile(r'<summary>(.*?)</summary>')
			summary=str(re.findall(re_summary,response,re.S)[0])
			#summary=re.search(re_summary,response,re.S)
		except:
			summary=''
		bookDict.update(内容简介=summary)

		try:
			re_doubanID=re.compile(r'<link href="(.*?)" rel="alternate"/>')
			doubanID=str(re.findall(re_doubanID,response)[0])
		except:
			doubanID=''
		bookDict.update(豆瓣链接=doubanID)
		
		data=bookDict
		keys=list(data.keys())
		values=list(data.values())

		display='-------\n%s:	%s\n%s:	%s\n%s:	%s\n%s:	%s\n%s:	%s\n%s:	%s\n%s:	%s\n%s:	%s\n%s:	%s\n%s:	%s\n%s:	%s\n%s:	%s\n%s:	%s\n'%(keys[0],values[0],keys[1],values[1],keys[2],values[2],keys[3],values[3],keys[4],values[4],keys[5],values[5],keys[6],values[6],keys[7],values[7],keys[8],values[8],keys[9],values[9],keys[10],values[10],keys[11],values[11],keys[12],values[12])
		print (display)
		self.infobox.insert('end','%s\n'%display)#insert
		
		dataYN=os.path.exists('BookData.csv')
		if dataYN:
			with open('BookData.csv', 'a', newline='') as csvfile:
				writer  = csv.writer(csvfile)
				writer.writerow(values)
		else:
			with open('BookData.csv', 'a', newline='') as csvfile:
				writer  = csv.writer(csvfile)
				writer.writerow(keys)
				writer.writerow(values)	
	def clean(self):
		self.infobox.delete('0.0','end')


if __name__ == "__main__":
	root=tk.Tk()
	root.title('图书查询系统')
	#root.geometry('450x700')

	Select=tk.Label(root,text='\n点击下框扫描/输入书后的条形码')
	Select.pack()

	app=BookCheck(root)

	#foot=tk.Label(root,text='\nPowered by@ShaoTech\nCopyriht © 大理大学留学生教育服务中心 版权所有\n如有问题请联系：石少华，Email: shi.sh@foxmail.com')
	foot=tk.Label(root,text='\nCopyriht © ShaoTech 版权所有\n如有问题请联系：Email: shi.sh@foxmail.com\n')
	foot.pack()
	root.mainloop()
	print ("the end")
#wrtData()