#_*_ coding:utf-8_*_
#需求：想要一款能为我所有重要文件备份的程序
import os
import time

#思路：
#	1.	需要备份的文件与目录将被指定在一个列表中。 
#	例如在Windows下：

source = ['D:\\eclipse-workspace','d:\\github'] 

# 2.备份文件必须存储在一个主备份目录中，如windows下的： 

target_dir = 'd:\\backup'

# 3.将备份文件打包压缩成zip文件,zip压缩文件的文件名，由当前日期和时间构成：

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') +'.zip'

# 5.如果目标目录（target_dir）不存在，则进行创建: 

if not os.path.exists(target_dir): 
	os.mkdir(target_dir)
	
# 我们使用haozip给文件打包：
#使用方法举例：start HaoZipC a d:\backup\back.zip d:\github\ d:\Java-Learn 这个命令就是把d盘下的github和Java-Learn两个目录压缩为back.zip 并保持在d盘的backup目录下

zip_command = 'start HaoZipC a {0} {1}'.format(target,' '.join(source))

#最后，运行备份
print ('zip command is')
print (zip_command)
print ('running:')
if os.system(zip_command) == 0:
	print ('Successful backup to', target)
else:
	print ('Backup FAILED')


