"""
牛顿方法计算平方根
JerryLiu
20190422
"""

import math
print("计算平方根")
x = float(input("请输入一个正整数： "))


tolerance = 0.000001# 初始化结束条件
estimate = 1.0 #估计值，默认为1.0

# 牛顿法 估计平方根
while True:
     estimate = (estimate + x / estimate) / 2
     difference = abs(x - estimate ** 2)
     if difference <= tolerance:
         break

print("牛顿法估计平方根为{}".format(estimate))
print("系统math库计算的值为{}".format(math.sqrt(x)))
