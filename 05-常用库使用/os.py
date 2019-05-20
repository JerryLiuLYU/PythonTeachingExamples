import os
def main():
    myPath = input("请输入一个路径")
    isShowAll = input("是否显示所有文件？Y or N").upper()
    if isShowAll=="Y":
        for dirpath,dirnames,filenames in os.walk(myPath):
            for filename in filenames:
                print(os.path.join(dirpath,filename))
    else:
        for file in os.listdir(myPath):
            if os.path.isfile(os.path.join(myPath, file)):
                print(os.path.join(myPath, file))

if __name__ == "__main__":
    main()
