#_*_ coding:utf-8_*_
#������Ҫһ����Ϊ��������Ҫ�ļ����ݵĳ���
import os
import time

#我的

#˼·��
#	1.	��Ҫ���ݵ��ļ���Ŀ¼����ָ����һ���б��С� 
#	������Windows�£�

source = ['D:\\eclipse-workspace','d:\\github'] 

# 2.�����ļ�����洢��һ��������Ŀ¼�У���windows�µģ� 

target_dir = 'd:\\backup'

# 3.�������ļ����ѹ����zip�ļ�,zipѹ���ļ����ļ������ɵ�ǰ���ں�ʱ�乹�ɣ�

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') +'.zip'

# 5.���Ŀ��Ŀ¼��target_dir�������ڣ�����д���: 

if not os.path.exists(target_dir): 
	os.mkdir(target_dir)
	
# ����ʹ��haozip���ļ������
#ʹ�÷���������start HaoZipC a d:\backup\back.zip d:\github\ d:\Java-Learn ���������ǰ�d���µ�github��Java-Learn����Ŀ¼ѹ��Ϊback.zip ��������d�̵�backupĿ¼��

zip_command = 'start HaoZipC a {0} {1}'.format(target,' '.join(source))

#������б���
print ('zip command is')
print (zip_command)
print ('running:')
if os.system(zip_command) == 0:
	print ('Successful backup to', target)
else:
	print ('Backup FAILED')


