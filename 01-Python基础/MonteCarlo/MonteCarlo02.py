import random
import time
import pickle
def InitPoints(p):
    MAX_RANGE=1000
    startTime = time.time()
    i2 = []
    for i in range(MAX_RANGE):
        i2.append(i**2)
    for px in range(MAX_RANGE):
        for py in range(MAX_RANGE):
            if ( i2[px] + i2[py]) < MAX_RANGE ** 2:
                p.append(1)
            else:
                p.append(0)
    endTime = time.time()
    print(endTime - startTime)
    with open('points.bin', 'wb') as f:
        pickle.dump(p, f)

def CalcuPi(n):
    #startTime = time.time()
    m = sum(random.choices(Points, k=n))
    pi = 4.0 * m / n
    #endTime = time.time()
    #print(endTime - startTime)
    print(pi)
    return pi


#numOfThrow = int(input('请输入每次投掷次数'))
#numOfGame = int(input('请输入游戏的次数'))
numOfThrow = 1000
numOfGame = 100
Results = []
Points = []
try:
    with open('points.bin', 'rb') as f:
        Points = pickle.load(f)
except:
    InitPoints(Points)
for i in range(numOfGame):
    Pi = CalcuPi(numOfThrow)
    Results.append(Pi)
Result = sum(Results) / numOfGame
print(Results)
print(Result)
