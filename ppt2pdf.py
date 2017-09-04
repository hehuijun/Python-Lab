
# coding: utf-8

#将ppt、pptx文件批量转换为pdf格式
import sys
import os
#glob模块是最简单的模块之一，内容非常少。用它可以查找符合特定规则的文件路径名。跟使用windows下的文件搜索差不多。查找文件只用到三个匹配符："*", "?", "[]"。"*"匹配0个或多个字符；"?"匹配单个字符；"[]"匹配指定范围内的字符，如：[0-9]匹配数字。
import glob
#windows下用python处理word、excel、PowerPoint、access文件
import win32com.client

#ppt文件所在目录，支持中文目录
dir =  r"d:\dev\ppt2pdf"
#生成的pdf文件存放目录
outputdir = r"d:\dev\ppt2pdf\pdf"

def convert(files, formatType = 32):
	#调用Powerpoint方法
	powerpoint = win32com.client.Dispatch("Powerpoint.Application")
	# 显示界面，设为0为不显示界面后台运行，但是报错
	powerpoint.Visible = 1
	#显示警报
	powerpoint.DisplayAlerts = 1
	#遍历所有文件
	for filename in files:
		newname = os.path.splitext(filename)[0] + ".pdf"
		newname = os.path.split(newname)[1]
		newname = os.path.join(outputdir,newname)
		#打开ppt文件
		deck = powerpoint.Presentations.Open(filename)
		#保存转换后的pdf文件，如目录下有同名文件，则直接覆盖
		deck.SaveAs(newname, formatType)
		deck.Close()
	powerpoint.Quit()

#glob.glob返回所有匹配的文件路径列表。它只有一个参数pathname，定义了文件路径匹配规则，这里可以是绝对路径，也可以是相对路径。
files = glob.glob(os.path.join(dir,"*.ppt*"))
#打印读取的文件名称
print(files)
#启动转换，转换过程中占用cpu高，建议空闲时间运行
convert(files)
print("转换完成！")

