# 函数式编程（Functional programming）或者函数程序设计又称泛函编程，是一种编程范型，它将计算机运算视为数学上的函数计算，并且避免使用程序状态以及易变对象。
# 简单来讲，函数式编程是一种“广播式”编程，通常是结合前面提到的lambda定义函数用于科学计算中，会显得简洁方便。
# 函数式编程主要由几个函数的使用构成：lambda、map、reduce、filter

# map函数
print ('map函数')
# 使用列表解析操作列表元素
print ('使用列表解析操作列表元素')
a=[1,2,3,4,1,2,3,5]
b = [i+2 for i in a]
print (a)
print (b)
print ('使用map函数操作列表元素')
c = map(lambda x: x+2, a)
c = list(c) 
print (a)
print (c)
print (' ')

# 也就是说，我们首先要定义一个函数，然后再用map命令将函数逐一应用到（map）列表中的每个元素，最后返回一个数组。map命令也接受多参数的函数，如map(lambda x,y: x*y, a, b)表示将a、b两个列表的元素对应相乘，把结果返回新列表。

# 有了列表解析，为什么还要有map命令呢？其实列表解析虽然代码简短，但是本质上还是for命令，而Python的for命令效率并不高，而map函数实现了相同的功能，并且效率更高，原则上来说，它的循环命令是C语言速度的。


# reduce函数
# map用于逐一遍历，而reduce用于递归计算
# 在Python 3.x中，reduce函数已经被移出了全局命名空间，被置于fuctools库中，使用时需要通过from fuctools import reduce引入reduce。
# 使用reduce计算n的阶乘
# from fuctools import reduce # 导入reduce函数
print ('使用reduce计算n的阶乘')
d=reduce(lambda x,y: x*y, range(1, n+1))
print (d)
print (' ')
