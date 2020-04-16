# 20200415
# 正则表达式学习
# -*- coding: utf-8 -*-

import re

# \d表示匹配一个数字
# \w表示匹配一个字母或数字
# .表示匹配任意字符

# *表示任意个字符，含0个
# +表示至少1个字符
# ?表示0个或者1个字符
# {n}表示n个字符
# {n,m}表示n-m个字符




# 校验某个电话号码是否符合格式
t1='080 -   544646' 
print('电话号码校验:', t1) 
if re.match(r'^\d{3}\s+-\s+\d{3,8}$',t1): # 进行正则匹配
	print(t1,'是正确的电话号码','\n')
else:
	print(t1,'是错误的电话号码','\n')
	
# 电话号码拆分
t2='080 - 545646' 
print('电话号码拆分:',t2)
m=re.match(r'^(\d{3})\s+-\s+(\d{3,8})$',t2) # 进行正则匹配
print('区号是:',m.group(1), '，本地号码是:',m.group(2),'\n')


# 校验某个时间值是否符合格式
t3='01:08:30' # 举例
print('时间值校验:', t3) 
if re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t3):
	m=re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t3)
	print(m.groups(),'是正确的时间值','\n')
else:
	print(t3,'是错误的时间值','\n')


# 校验邮箱地址是否符合格式
e1='bill.gates@microsoft.com'
e2='s3omosdk-979_eone@gmail.com'
e3='bob#example.com'
e4='81mr_bob@example.com'
print('邮箱地址校验:','\n', e1,'\n',e2,'\n',e3,'\n',e4,'\n') 
re_email=re.compile(r'^[a-zA-Z][0-9a-zA-Z\_\-]+\@[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)+$') # 预编译正则表达式（以字母开头，且由字母、数字、下划线或中划线组成）
m1=re_email.match(e1)
m2=re_email.match(e2)
m3=re_email.match(e3)
m4=re_email.match(e4)
print('校验结果:') 
if m1==None:
	print(e1,'是错误的邮箱地址')
else:
	print(e1,'是正确的邮箱地址')
if m2==None:
	print(e2,'是错误的邮箱地址')
else:
	print(e2,'是正确的邮箱地址')
if m3==None:
	print(e3,'是错误的邮箱地址')
else:
	print(e3,'是正确的邮箱地址')
if m4==None:
	print(e4,'是错误的邮箱地址','\n')
else:
	print(e4,'是正确的邮箱地址','\n')

# 提取邮箱地址中的名字
f1='Tom_Pa-r_99is8tom@voyager.org'
f2='81Bob@example.com'
f3='Tom_Trump@voyager.org#decode'
print('提取邮箱地址中的名字:','\n', f1,'\n',f2,'\n',f3,'\n') 
re_ename=re.compile(r'^([a-zA-Z][a-zA-Z\_\-]+[a-zA-Z])[0-9a-zA-Z\_]+@[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)+$') # 预编译正则表达式（以字母开头，且以字母结尾，不包含数字的字符串）
n1=re_ename.match(f1)
n2=re_ename.match(f2)
n3=re_ename.match(f3)
print('提取名字的结果:') 
if n1==None:
	print(f1,'是错误的邮箱地址')
else:
	print(n1.group(1))
if n2==None:
	print(f2,'是错误的邮箱地址')
else:
	print(n2.group(1))
if n3==None:
	print(f3,'是错误的邮箱地址','\n')
else:
	print(n3.group(1),'\n')

#输入邮箱进行校验
email=input('请输入需要校验的邮箱地址：')
r_email=re.compile(r'^[a-zA-Z][0-9a-zA-Z\_\-]+\@[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)+$') # 预编译正则表达式（以字母开头，且由字母、数字、下划线或中划线组成）
m1=r_email.match(email)
if m1==None:
	print(email,'是错误的邮箱地址')
else:
	print(email,'是正确的邮箱地址')