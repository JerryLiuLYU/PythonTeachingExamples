import random
import time

n = int(input('请输入循环次数'))
m = 0
startTime = time.time()
for i in range(1,n+1):
    x = random.random()
    y = random.random()
    if (x ** 2 + y ** 2) <= 1:
        m += 1
    print(i,4.0 * m / i)
pi = 4.0 * m / n
endTime = time.time()

print(pi)
print(endTime - startTime)