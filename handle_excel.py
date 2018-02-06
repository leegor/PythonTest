
import xlrd

#读入test.xls表
wb =  xlrd.open_workbook('d:/test.xlsx')
#统计下此excel表有几个sheet
print ('此excel表sheet的总个数是: %s 个' % wb.nsheets)
print ()
#方法1：
for s in wb.sheets():
    #打印每个sheet的每行最后一列的值
    print ("==the last column of sheet '%s' ==" % s.name)
    for i in range(s.nrows):
        print (s.row(i)[-1].value)
    #打印每个sheet每行的值
    print ("==each row content as below ==")
    for i in range(s.nrows):
        print (s.row_values(i))
#以上读文件内容，还有几个方法，见CSDN博客

