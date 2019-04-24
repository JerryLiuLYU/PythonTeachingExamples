"""
猜数字的gui版本
"""
4
import random
from breezypythongui import EasyFrame

class GuessingGame(EasyFrame):
    """猜测数字的类，继承自EasyFrame"""

    def __init__(self):
        """初始化"""
        EasyFrame.__init__(self, title = "猜数字", width=500,height=300)
        self.myNumber = random.randint(1, 100)
        self.count = 0
        greeting = "请猜测1-100之间的一个整数."
        self.hintLabel = self.addLabel(text = greeting,
                                       row = 0, column = 0,
                                       sticky = "NSEW",
                                       columnspan = 2)
        self.addLabel(text = "输入猜测：", row = 1, column = 0)
        self.guessField = self.addIntegerField(0, row = 1,
                                               column = 1,width=50)
        self.nextButton = self.addButton(text = "点击猜测", row = 2,
                                         column = 0,
                                         command = self.nextGuess)
        self.newButton = self.addButton(text = "开始新游戏", row = 2,
                                        column = 1,
                                        command = self.newGame)

    def nextGuess(self):
        """处理猜测过程"""
        self.count += 1
        guess = self.guessField.getNumber()
        self.guessField.setValue('')
        if guess == self.myNumber:
            self.hintLabel["text"] = "正确！你一共猜了" + \
                                     str(self.count) + " 次!"
            self.nextButton["state"] = "disabled"
        elif guess < self.myNumber:
            self.hintLabel["text"] = "小了"
        else:
            self.hintLabel["text"] = "大了"

    def newGame(self):
        """开始新游戏"""
        self.myNumber = random.randint(1, 100)
        self.count = 0
        greeting = "请猜测1-100之间的一个整数."
        self.hintLabel["text"] = greeting
        self.guessField.setNumber(0)
        self.nextButton["state"] = "normal"

def main():
    GuessingGame().mainloop()

if __name__ == "__main__":
    main()
