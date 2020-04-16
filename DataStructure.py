# 4个内建的数据结构—List（列表）、Tuple（元组）、Dictionary（字典）以及Set（集合），它们可以统称为容器（Container）
# 容器里边的元素类型不要求相同

# 列表/元组
# 列表和元组都是序列结构
# 访问列表和元组中的元素的方式都是一样的
# 从外形上看，列表是用方括号标记的，元组是用圆括号标记的
# 从功能上看，列表与元组的区别在于：列表可以被修改，而元组不可以
print ('列表/元组')
a1 = [1, 'abc', [1, 2]] # a1是一个列表，列表的第一个元素是整型1，第二个是字符串'abc'，第三个是列表[1, 2]
print(a1)
print(a1[0],a1[1],a1[2])
a2 = (1, 'abc', [1, 2]) # a2是一个元组
print(a2)
print(a2[0],a2[1],a2[2])

print ('修改列表的元素')
a1[0]='修改'
# a2[0]='修改' # 修改元组的元素会报错
print(a1)
print(a1[0],a1[1],a1[2])
print (' ')

# 复制列表
print ('引用列表')
b=a1 #b可视为a1的别名，或者说引用了a1
print(b)
print(b[0],b[1],b[2])
print ('复制列表')
b=a1[:]
b[0]='复制修改'
print(b)
print(b[0],b[1],b[2])
print (' ')

# 与列表有关的函数是list
# 与元组有关的函数是tuple
# list和tuple都是将某个对象转换为列表/元组
print ('将某个对象转换为列表/元组')
print(list('ab'))
print(list([1,2]))
print(tuple('ab'))
print(tuple([1,2]))
print (' ')

# 一些常见的与列表/元组相关的函数
# cmp(a, b)：比较两个列表/元组的元素
# len(a)：列表/元组元素个数
# max(a)：返回列表/元组元素最大值
# min(a)：返回列表/元组元素最小值
# sum(a)：将列表/元组中的元素求和
# sorted(a)：对列表的元素进行升序排序

# 作为对象来说，列表本身自带了很多实用的方法（元组不允许修改，因此方法很少）
# a.append(1)：将1添加到列表a末尾
# a.count(1)：统计列表a中元素1出现的次数
# a.extend([1, 2])：将列表[1, 2]的内容追加到列表a的末尾
# a.index(1)：从列表a中找出第一个1的索引位置
# a.insert(2, 1)：将1插入列表a中索引为2的位置
# a.pop(1)：移除列表a中索引为1的元素
print ('列表自带的方法')
c=[1,2,3,4,1,2,3,5,'牛逼']
print(c)
print(c[0],c[1],c[2],c[3],c[4],c[5],c[6],c[7],c[8])
c.append('插入')
print(c)
print(c.count('牛逼'))
c.extend([23,'整个插入'])
print(c)
print(c.index('牛逼'))
c.insert(2,'定位插入')
print(c)
c.pop(8)
print(c)
print (' ')

# 使用append函数对列表元素进行操作
# 使用列表解析进行简化
print ('使用append函数对列表元素进行操作')
d=[11,12,13]
e=[]
print(d)
print(e)
for i in d:
	e.append(i+2) # 使用append函数对列表元素进行操作
print(d)
print(e)
print ('使用列表解析进行简化')
f=[j+2 for j in d] # 使用列表解析进行简化
print(d)
print(e)
print(f)
print (' ')

# 字典
# 从数学上来讲，它实际上是一个映射
# 通俗来讲，它也相当于一个列表，然而它的“下标”不再是以0开头的数字，而是自定义的“键”（Key）
# 自定义的“键”（Key）在整个字典中必须是唯一的
print ('创建字典')
h={'yestoday':10,'today':20,'tomorrow':30}
print(h)
print(h['today'])
print(h['tomorrow'])
print (' ')

# 通过dict或者dict.fromkeys创建字典
print ('通过dict或者dict.fromkeys创建字典')
m=dict([['yestoday', 10],['today', 20], ['tomorrow', 30]]) # 也相当于{'yestoday':10,'today':20,'tomorrow':30}}
n=dict.fromkeys(['today', 'tomorrow'], 20) # 相当于{'today':20, 'tomorrow':20}print(m)
print(m)  
print(n) 
print (' ')

# 集合
# 跟列表的区别在于：①它的元素是不重复的，而且是无序的；②它不支持索引
# 集合具有一定的特殊性（特别是无序性）
# 一般我们通过花括号{}或者set()函数来创建一个集合
# 集合运算
print ('集合运算')
t={1,3,5,7,9,0,0} # 注意0会自动去重
s=set([1,2,3,4,5,6,6]) # 同样地，它将列表转换为集合
x1 = t|s  # t和s的并集
x2 = t&s  # t和s的交集
x3 = t-s  # 求差集（项在t中，但不在s中）
x4 = t^s  # 对称差集（项在t或s中，但不会同时出现在二者中）
print(t) 
print(s) 
print(x1) 
print(x2)
print(x3)
print(x4)
print (' ')



