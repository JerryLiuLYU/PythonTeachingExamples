"""
查找文本文件中一系列数字的中位数

"""

fileName = input("输入文件名称： ")
f = open(fileName, 'r')
    

numbers = []
for line in f:
    words = line.split()
    for word in words:
        numbers.append(float(word))


numbers.sort()
midpoint = len(numbers) // 2
print("中位数为", end=" ")
if len(numbers) % 2 == 1:
    print(numbers[midpoint])
else:
    print((numbers[midpoint] + numbers[midpoint - 1]) / 2)
