#_*_ coding:utf-8 _*_

#����һ���ַ�������Ȼ��������и��ֲ���

name = 'swaroop'

if name.startswith('swa'):
	print ('yes, the string start with "swa"')
	
if 'a' in name:
	print ('yes, "a" in the string')
	
if name.find('war'):
	print ('yes, "war" in string')

mylist = ['jack','Join','Lee']

print ('_*_'.join(mylist))
print(name.split('a')[0])
print(' '.join(mylist))

for i in name:
	print(i,end=' ')