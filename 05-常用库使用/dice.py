import random
Dice = (1,2,3,4,5,6)
def Throw():
    print("投掷中...")
    d1 = random.choice(Dice)
    d2 = random.choice(Dice)
    return d1 + d2
def Game(userGuess, number):
    if (2<= number <= 5) and userGuess=="2":
        return True
    elif (9<= number <= 12) and userGuess=="1":
        return True
    else:
        return False
    
        
def Main():
    scores = 100
    while(scores > 0):
        guess = input("请选择大小？1-大 or 2-小 or 0-退出")
        if(guess == "0"):
            break        
        scores -= 10
        result = Throw()
        if Game(guess, result):
            scores += 30
            print("点数为{},你猜对了,赢了20分,当前积分为{}".format(result,scores))   
        else:
            print("点数为{},猜错了,你的积分剩余{}".format(result,scores))
    else:
        print("没有积分了，你输了，gameover")
            
if __name__ == "__main__":
    Main()
    
    
            
