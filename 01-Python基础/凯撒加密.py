test = input('请输入文本：')
numToMove = eval(input("请输入加密的移动位数："))
afterTest = ""
for p in test: 
    if ord("a") <= ord(p) <= ord("z"):
        afterTest += chr(ord("a")+(ord(p)-ord("a")+numToMove)%26)
    elif ord("A") <= ord(p) <= ord("Z"):
        afterTest += chr(ord("A")+(ord(p)-ord("A")+numToMove)%26)
    else:
        afterTest += p
print("加密后的文本为：")
print(afterTest)
backTest = ''
for p in afterTest: 
    if ord("a") <= ord(p) <= ord("z"):
        backTest += chr(ord("z")-(ord('z')-ord(p)+numToMove)%26)
    elif ord("A") <= ord(p) <= ord("Z"):
        backTest += chr(ord("Z")-(ord('Z')-ord(p)+numToMove)%26)
    else:
        backTest += p

print("解密密后的文本为：")
print(backTest)

