"""
心理辅导程序
模仿1960sMIT开发的ELIZA心理医生程序的简单版本
"""

import random
#元组，保存引导语句
hedges = ("哦.",
          "是的，很多其他病人也这么说过.",
          "然后呢？")
#元组，保存问句的前导语
questions = ("你为什么说",
              "你似乎认为",
              "为什么你觉得")
#字典，保存人称互换规则
replacements = {"我":"你","你":"我"} 

def reply(sentence):
    """回复程序"""
    probability = random.randint(1, 3)#以一定概率选择下面的两个方法
    if probability == 1: #避免正面回答，使用引导语句
        return random.choice(hedges)
    else: #进一步询问，使用问句
        return random.choice(questions) + changePerson(sentence)

def changePerson(sentence):
    """改变人称代词"""
    replyWords = []
    for word in sentence:
        replyWords.append(replacements.get(word, word))
    return "".join(replyWords) 

def main():
    print("你好，今天你感觉怎么样？")
    while True:
        sentence = input("\n>> ")
        if sentence.upper() == "Q":
            print("再见")
            break
        print(reply(sentence))

if __name__ == "__main__":
    main()

