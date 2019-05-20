import re
email = input("请输入Email地址（输入 q 退出）：")
while email != "q":    
    if(re.match("^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$",email) != None):
        print("合法的Email地址")
    else:
        print("Email地址错误")
    email = input("请输入Email地址（输入 q 退出）：")
