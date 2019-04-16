#-*- coding: utf-8 -*-
import time
import xlrd
#import xlwt
import csv

class extract():
	filename = ''
	def __init__(self, filename):
		workbook = xlrd.open_workbook(filename)
		sheet_names= workbook.sheet_names()
		self.sheet1 = workbook.sheet_by_name(sheet_names[0])
		self.id_list = self.sheet1.col_values(3)

	def getList(self):
		with open('extract.txt','r') as fp:
			self.list=[]
			self.list.append(self.sheet1.row_values(0))
			#print (a)
			for i in fp:
				i=i.strip('\n')
				if i in self.id_list:
					row_num=self.id_list.index(i)
					matched=self.sheet1.row_values(row_num)
					try:
						matched[7]=xlrd.xldate.xldate_as_datetime(self.sheet1.cell(row_num,7).value, 0).strftime('%Y/%m/%d')
						matched[10]=xlrd.xldate.xldate_as_datetime(self.sheet1.cell(row_num,10).value, 0).strftime('%Y/%m/%d')
						matched[12]=xlrd.xldate.xldate_as_datetime(self.sheet1.cell(row_num,12).value, 0).strftime('%Y/%m/%d')
					except:
						pass
					self.list.append(matched)
				else:
					print ('数据库中没有匹配到该生信息')
		print (self.list)
		return self.list
		
	def writecsv(self):	
		list=self.getList()
		with open('result.csv', 'w', newline='') as csvfile:
			writer  = csv.writer(csvfile)
			for row in list:
				writer.writerow(row)


	def data_write(self):
		list=self.getList()
		f = xlwt.Workbook()
		sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True) #创建sheet 
		#将数据写入第 i 行，第 j 列
		i = 0
		for data in list:
			for j in range(len(data)):
				sheet1.write(i,j,data[j])
			i = i + 1       
		f.save('result.xls') #保存文件
if __name__ == '__main__':
	x = extract('2019新生名单+.xlsx')
	#x.data_write()
	x.writecsv()
	print ('\n匹配完成！')
	time.sleep(7)
	