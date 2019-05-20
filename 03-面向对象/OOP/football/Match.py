import random
import time
class MatchInfo:
    def __init__(self,homeName,awayName):
        self.homeTeamName = homeName
        self.awayTeamName = awayName
        self.homeTeamGoal = 0
        self.awayTeamGoal = 0
        self.Details = []

class Match:
    Descriptions = (
        "点球！点球！他竟然把球踢向了看台",
        "比赛沉闷至极，球迷都睡着了",
        "裁判出示了黄牌，这个犯规太恶劣了",
        "好机会，球进了！裁判举旗了，越位在先",
        "这么好的机会竟然没有打门，他在思考人生吗？",
        "比赛你来我往，十分精彩",
        "门将发挥太出色了，看来很难进球",
        "天若有情天亦老，看到哈特来一脚",
        "面对空门，竟然没有打进，不得不说，这个球打不进的难度更大",
        "他鱼跃冲顶，可惜偏出球门",
        "面对门将了，可惜单刀没有打进")
    def __init__(self, homeTeam,awayTeam):
        self.__awayTeam = awayTeam
        self.__homeTeam = homeTeam
        self.__info = MatchInfo(homeTeam.Name, awayTeam.Name)
    def Print(self):
        for i,item in enumerate( self.__info.Details):
            print("第{}分钟,{}".format((i+1)*10,item))
            time.sleep(1)
        print("裁判一声哨向，比赛结束")
        print("{}vs{},比分{}:{}".format(self.__info.homeTeamName,self.__info.awayTeamName,self.__info.homeTeamGoal,self.__info.awayTeamGoal))
    def Run(self):
        self.__info.awayTeamGoal = 0
        self.__info.homeTeamGoal = 0
        self.__info.Details.clear()
        isHomeNotGood = self.__IsTrueByProb(1 - (self.__homeTeam.GetTeamStabilityPower() / 100))
        isAwayNotGood = self.__IsTrueByProb(1 - (self.__awayTeam.GetTeamStabilityPower() / 100))
        homeTeamRateAtGame = self.__homeTeam.GetRate() * 0.8  if isHomeNotGood else self.__homeTeam.GetRate()
        awayTeamRateAtGame = self.__awayTeam.GetRate() * 0.8  if isAwayNotGood else self.__awayTeam.GetRate()
        for i in range(9):
            n1 = abs((self.__homeTeam.GetTeamAttackPower() - self.__awayTeam.GetTeamDefendPower()))
            n2 = abs((self.__awayTeam.GetTeamAttackPower() - self.__homeTeam.GetTeamDefendPower()))
            #print(n1 + n2)
            prob = (n1 + n2 + random.uniform(5.0, 10.0)) / 100
            #print(prob)
            isGoal = self.__IsTrueByProb(prob)
            if isGoal:
                isHomeGoal = self.__IsTrueByProb(homeTeamRateAtGame / (homeTeamRateAtGame + awayTeamRateAtGame))
                if isHomeGoal:
                    self.__info.homeTeamGoal += 1
                    self.__info.Details.append("Goal~{}进球了，太精彩了,主场球迷欢欣鼓舞！".format(self.__homeTeam.Name))
                else:
                    self.__info.awayTeamGoal += 1
                    self.__info.Details.append("Goal~{}在客场进球，难以置信！".format(self.__awayTeam.Name))
            else:
                self.__info.Details.append(random.choice(Match.Descriptions))
        return self.__info.homeTeamGoal,self.__info.awayTeamGoal


    def __IsTrueByProb(self, prob):
        if prob > 1.0:
            prob = 1.0
        rad = random.random()
        if rad < prob:
            return True
        else:
            return False
