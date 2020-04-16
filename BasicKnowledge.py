# -*- coding: utf-8 -*
# 注明编码，如果脚本中带有中文，最好在文件头注明编码，并将脚本保存为utf-8的编码格式。

print ("Hello,workd !")
print (' ')

# 将2+3的结果复制给a，并将输出a的赋值运算结果
print ('a的赋值运算结果')
a=2+3 
print(a)
print (' ')

# 打印中文
print ('打印中文')
print('世界，你好！')
print (' ')


# 基本运算
print ('基本运算')
b1=3 # 赋值运算
b2=b1*3 # 乘法运算
b3=b1**3 # 幂运算
print(b1,b2,b3)
print (' ')

# 多重赋值
print ('多重赋值')
c1,c2,c3=2,3,4
print(c1,c2,c3)
print (' ')

# 字符串操作
print ('字符串操作')
d='I like python'
print(d+' very much') # 拼接字符串
d.split(' ') # 以空格分割字符串
print(d)
print (' ')

# if判断	
print ('if判断')
e=0
if e==1:
	print(e)
else:
	print('e不等于1')
	print (' ')
	
# while循环
# 该循环过程就是求1+2+3+...+100
# 自增和求和两个先后顺序不同的区别
print ('while循环')
Sum01,Sum02,f,g=0,0,0,0
while f<100: # 先自增1，再求和
	f=f+1
	Sum01=Sum01+f
print(Sum01,f)

while g<101: # 先求和，再自增1
	Sum02=Sum02+g
	g=g+1
print(Sum02,g)
print (' ')

# for循环
# 该循环过程就是求1+2+3+...+100
# in是用来判断一个元素是否在列表/元组中
# range用来生成连续的序列，一般语法为range(a, b, c)，表示以a为首项、c为公差且不超过b-1的等差数列
print ('for循环')
Sum03=0
for h in range(101):
	Sum03=Sum03+h
print(Sum03,h)
print (' ')

# 使用range生成等差数列
print ('使用range生成等差数列')
i=0
if i in range(4):
	print('i在0,1,2,3中')
if i not in range(1,4,1):
	print('i不在1,2,3中')
print (' ')

# 使用def来自定义函数
print ('使用def来自定义函数')
def add1(j):
	return j+2
print(add1(8))
print (' ')

# 函数返回值可以是各种形式，可以返回列表，甚至返回多个值
print ('函数返回值可以是各种形式')
k1,k2,k3,k4,k5,k6,k7,k8=0,0,0,0,0,0,0,0 # 思考点：必须先声明函数的参数值？？？
def add2(k1,k2):
	return[k1+2,k2+2] # 返回值是一个列表
k3,k4=add2(1,7)
print (add2(1,7))
print(k1,k2,k3,k4)

def add3(k5,k6): 
	return k5+3,k6+3 # 双重返回
k7,k8=add3(1,2)
print (add3(1,2))
print(k5,k6,k7,k8)
print (' ')

# 使用lambda对简单的功能定义“行内函数”
print ('使用lambda对简单的功能定义“行内函数”')
m=lambda m1:m1+2  # 定义函数m(m1)=m1+2
n=lambda n1,n2:n1+n2 # 定义函数n(n1,n2)=n1+n2
print(m(32))
print(n(3,50))
print ('')

