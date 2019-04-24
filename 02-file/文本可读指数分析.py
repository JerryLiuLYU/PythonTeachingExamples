"""
英文文本分析 - Flesch可读指数计算
JerryLiu
计算一个文本文件的可读性指数，这个指数是
基于文本中每个单词的平均音节数和每个句子的平均单词数。
索引分数通常在0到100之间
0-30 大学
50-60 高中
90-100 小学
"""

# 读取文本文件
fileName = input("输入文件名称: ")
inputFile = open(fileName, 'r')
text = inputFile.read()

# 计算文本中句子的个数
sentences = text.count('.') + text.count('?') + \
            text.count(':') + text.count(';') + \
            text.count('!')

# 获取所有单词的个数
words = len(text.split())

# 计算音节
syllables = 0
vowels = "aeiouAEIOU"
for word in text.split():
    for vowel in vowels:
        syllables += word.count(vowel)
    for ending in ['es', 'ed', 'e']:
        if word.endswith(ending):
            syllables -= 1
    if word.endswith('le'):
        syllables += 1

# 计算Flasch指数和级别
index = 206.835 - 1.015 * (words / sentences) - \
        84.6 * (syllables / words)
level = int(round(0.39 * (words / sentences) + 11.8 * \
                  (syllables / words) - 15.59))

# 输出结果
print("Flesch指数为：", index)
print("对应级别为：", level)  


