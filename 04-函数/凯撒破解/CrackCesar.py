import time
EnglishWords = []
def Decrypt(test, numToMove):
    afterTest = ""
    for p in test: 
        if ord("a") <= ord(p) <= ord("z"):
            afterTest += chr(ord("z")-(ord('z')-ord(p)+numToMove)%26)
        elif ord("A") <= ord(p) <= ord("Z"):
            afterTest += chr(ord("Z")-(ord('Z')-ord(p)+numToMove)%26)
        else:
            afterTest += p
    return afterTest

def IsFind(test,rate=0.7):
    words = test.split()
    totalCount = len(words)
    findCount = 0
    for word in words:
        if word in EnglishWords:
            findCount += 1
    if findCount / totalCount > rate:
        return True
    else:
        return False

def crack(test):
    for i in range(1,27):
        crackTest = Decrypt(test, i)
        if IsFind(crackTest):
            return crackTest
    return None

def ReadEnglishWords():
    result = []
    fileRead = open(r"D:\Documents\GitHub\PythonTeachingExamples\04-函数\凯撒破解\最常用2000英语单词.txt","r",encoding="utf-8")
    contentRead = fileRead.readlines()
    for i in contentRead:
        lineContents = i.split()
        if len(lineContents)>1 and lineContents[0].isdigit():
            result.append(lineContents[1])
    return result



EnglishWords = ReadEnglishWords()
encryptTest = input("请输入密文：")
print("开始破解...")
startTime = time.time()
orgTest = crack(encryptTest)
endTime = time.time()
print(orgTest)
print("破解时间：",endTime - startTime)
