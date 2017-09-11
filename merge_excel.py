
# coding: utf-8

#将多个Excel文件簿（文件）中所有的表（sheet）合并成一个
import os
import sys
import xlrd
import xlsxwriter
import glob

#excel文件所在目录，支持中文目录
dir =  r"d:\dev\excel"
#合并后的文件存放目录
outputdir = r"d:\dev\excel\merge\\"
#合并后的新文件名
mergefile= outputdir+"合并.xlsx"

#打开一个excel文件
def open_xls(file):
    newfile=xlrd.open_workbook(file)
    return newfile

#获取excel中所有的sheet表
def getsheet(newfile):
    return newfile.sheets()

#获取sheet表的个数
def getshnum(newfile):
    x=0
    sh=getsheet(newfile)
    for sheet in sh:
        x+=1
    return x

#获取sheet表的行数
def getnrows(newfile,sheet):
    table=newfile.sheets()[sheet]
    return table.nrows

#读取文件内容并返回行内容
def getFilect(file,shnum):
    newfile=open_xls(file)
    table=newfile.sheets()[shnum]
    num=table.nrows
    for row in range(num):
        rdata=table.row_values(row)
        datavalue.append(rdata)
    return datavalue


if __name__=='__main__':
    #定义要合并的excel文件列表
    #获取指定excel文件
    #allxls=['D:/dev/excel/11.xlsx','D:/dev/excel/第二.xlsx']
    #获取目录下所有excel文件
    allxls = glob.glob(os.path.join(dir,"*.xls*"))
    #存储所有读取的结果
    datavalue=[]
    for filename in allxls:
        newfile=open_xls(filename)
        x=getshnum(newfile)
        for shnum in range(x):
            print("正在读取文件："+str(filename)+"的第"+str(shnum)+"个sheet表的内容...")
            rvalue=getFilect(filename,shnum)
    #定义最终合并后生成的新文件
    wb=xlsxwriter.Workbook(mergefile)
    #创建一个sheet工作对象
    ws=wb.add_worksheet()
    for a in range(len(rvalue)):
        for b in range(len(rvalue[a])):
            c=rvalue[a][b]
            ws.write(a,b,c)
    wb.close()
    print("文件合并完成")
