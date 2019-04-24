"""
基于命令行的文件浏览器

"""

import os, os.path

QUIT = '7'

COMMANDS = ('1', '2', '3', '4', '5', '6', '7')

MENU = """1   列出当前目录内容
2   向上一级
3   向下一级
4   统计当前目录中的文件个数
5   当前目录的大小（字节）
6   查找文件
7   退出"""

def main():
    while True:
        print(os.getcwd())
        print(MENU)
        command = acceptCommand()
        runCommand(command)
        if command == QUIT:
            print("再见")
            break

def acceptCommand():
    """获取用户输入的命令"""
    while True:
        command = input("Enter a number: ")
        if not command in COMMANDS:
            print("Error: command not recognized")
        else:
            return command

def runCommand(command):
    """根据命令，执行对应操作"""
    if command == '1':
        listCurrentDir(os.getcwd())
    elif command == '2':
        moveUp()
    elif command == '3':
        moveDown(os.getcwd())
    elif command == '4':
        print("文件总数为：", \
              countFiles(os.getcwd()))
    elif command == '5':
        print("总大小为：", \
              countBytes(os.getcwd()))
    elif command == '6':
        target = input("请输入查找文件名: ")
        fileList = findFiles(target, os.getcwd())
        if not fileList:
            print("未找到")
        else:
            for f in fileList:
                print(f)

def listCurrentDir(dirName):
    """列出当前目录下所有文件"""
    lyst = os.listdir(dirName)
    for element in lyst: print(element)

def moveUp():
    """目录向上一级"""
    os.chdir("..")

def moveDown(currentDir):
    """目录向下一级"""
    newDir = input("请输入进入的目录名称: ")
    if os.path.exists(currentDir + os.sep + newDir) and \
       os.path.isdir(newDir):
        os.chdir(newDir)
    else:
        print("错误：没有此目录")

def countFiles(path):
    """递归获取当前目录下所有文件的个数（包含子目录）"""
    count = 0
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            count += 1
        else:
            os.chdir(element)
            count += countFiles(os.getcwd())
            os.chdir("..")
    return count

def countBytes(path):
    """递归获取当前目录下所有文件的大小（包含子目录）"""
    count = 0
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            count += os.path.getsize(element)
        else:
            os.chdir(element)
            count += countBytes(os.getcwd())
            os.chdir("..")
    return count

def findFiles(target, path):
    """递归查询当前目录（包含子目录）中是否包含文件"""
    files = []
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            if target in element:
                files.append(path + os.sep + element)
        else:
            os.chdir(element)
            files.extend(findFiles(target, os.getcwd()))
            os.chdir("..")
    return files

if __name__ == "__main__":
    main()
