'''
猜数小游戏
jerryliu
20190423
'''
import random

smaller = int(input("输入最小值: "))
larger = int(input("输入最大值: "))
myNumber = random.randint(smaller, larger)
count = 0
while True:
    count += 1
    userNumber = int(input("输入猜测值: "))
    if userNumber < myNumber:
        print("小了")
    elif userNumber > myNumber:
        print("大了")
    else:
        print("猜对了，共猜了{}次".format(count))
        break
