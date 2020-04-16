import math
import math as m # 使用别名导入库


# 使用math库进行数学运算
print('使用math库进行数学运算') 
print(math.sin(1)) # 计算正弦
print(math.cos(1)) # 计算余弦
print(math.tan(1)) # 计算正切
# print(math.cot(0)) # 计算余切  思考点：不能计算余切？？？
print(math.pi) # 内置的圆周率常数
print(' ') 

# 使用别名导入math库进行数学运算
print('使用别名导入math库进行数学运算') 
print(m.sin(1)) # 计算正弦
print(m.cos(1)) # 计算余弦
print(m.tan(1)) # 计算正切
# print(m.cot(0)) # 计算余切
print(m.pi) # 内置的圆周率常数
print(' ') 

# 通过名称导入指定函数
from math import exp as e # 只导入math库中的exp函数，并起别名e
print('通过名称导入指定函数') 
print(e(1)) # 计算指数
# print(sin(1)) # 此时sin(1)和math.sin(1)都会出错，因为没被导入
print(' ') 

# 导入库中所有函数
# 直接导入math库，也就是去掉math.，但如果大量地这样引入第三库，就容易引起命名冲突
# from math import * 
# print('导入库中所有函数') 
# print(sin(1)) 
# print(exp(1))
# print(' ') 

# 导入future特征
# 将print变成函数形式，即用print(a)格式输出
# from __future__ import print_function

# 3.x的3/2=1.5，3//2才等于1；2.x中3/2=1
# from __future__ import division