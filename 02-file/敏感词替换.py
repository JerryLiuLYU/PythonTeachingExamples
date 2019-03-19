strFilePath = input("请输入读取在文件路径：") #"D:/ttt/123.txt"
wordToReplace = input("请输入需要替换在单词：")
wordReplaced = input("请输入替换为什么？：")
t = strFilePath.split('.')
newFileName = t[0] + "_2." + t[1]
fileRead = open(strFilePath,"r")
fileWrite = open(newFileName,"w")
contentRead = fileRead.readlines()
contentWrite = []
for i in contentRead:
    contentWrite.append(i.replace(wordToReplace, wordReplaced))
fileWrite.writelines(contentWrite)
fileRead.close()
fileWrite.close()
print("文件处理完成，新文件为{0}".format(newFileName))
