def Encrypt(test, numToMove):
    afterTest = ""
    for p in test: 
        if ord("a") <= ord(p) <= ord("z"):
            afterTest += chr(ord("a")+(ord(p)-ord("a")+numToMove)%26)
        elif ord("A") <= ord(p) <= ord("Z"):
            afterTest += chr(ord("A")+(ord(p)-ord("A")+numToMove)%26)
        else:
            afterTest += p
    return afterTest
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
test = input('请输入文本：')
num = eval(input("请输入加密的移动位数："))
after = Encrypt(test, num)
print("加密后的文本为：")
print(after)
print("解密密后的文本为：")
print(Decrypt(after,num))

