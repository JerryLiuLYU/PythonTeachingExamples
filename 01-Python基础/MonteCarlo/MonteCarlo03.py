import random
import time
import pickle
def InitPoints(p):
    MAX_RANGE=10000
    startTime = time.time()
    i2 = []
    for i in range(MAX_RANGE):
        i2.append((i/(MAX_RANGE-1))**2)
    for px in range(MAX_RANGE):
        for py in range(MAX_RANGE):
            if ( i2[px] + i2[py]) <= 1.0:
                p.append(1)
            else:
                p.append(0)
    endTime = time.time()
    print(endTime - startTime)
    with open('points.bin', 'wb') as f:
        pickle.dump(p, f)

def CalcuPi(n):
    #startTime = time.time()
    m = sum(random.sample(Points, k=n))
    pi = 4.0 * m / n
    #endTime = time.time()
    #print(endTime - startTime)
    #print(pi)
    return pi


#numOfThrow = int(input('请输入每次投掷次数'))
#numOfGame = int(input('请输入游戏的次数'))
numOfThrow = 1000
numOfGame = 10000000
Results = []
Points = []
try:
    with open('points.bin', 'rb') as f:
        Points = pickle.load(f)
except:
    InitPoints(Points)
for i in range(1,numOfGame+1):
    Pi = CalcuPi(numOfThrow)
    Results.append(Pi)
    if i % 10 == 0:
        print(sum(Results)/len(Results))
Result = sum(Results) / numOfGame
print(Results)
print(Result)
