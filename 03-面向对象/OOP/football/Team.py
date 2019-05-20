class Team:
    MaxNumOfPlayer = 4
    def __init__(self):
        self.Name = ""
        self.__players = []
        self.__coach = None
    def AddPlayer(self, player):
        self.__players.append(player)
    def AddCoach(self, coach):
        self.__coach = coach
    def GetRate(self):
        return (self.GetTeamAttackPower() + self.GetTeamDefendPower() + self.GetTeamStabilityPower()) / 3
    def GetTeamAttackPower(self):
        result = 0.0
        attackPlayers = [item for item in self.__players if item.Position in ("前锋","中场")]
        for item in attackPlayers:
            result += item.AttackPower
        return result/ len(attackPlayers)
    def GetTeamDefendPower(self):
        result = 0.0
        defendPlayers = [item for item in self.__players if item.Position in ("后卫","门将")]
        for item in defendPlayers:
            result += item.DefendPower
        return result/ len(defendPlayers)
    def GetTeamStabilityPower(self):
        result = 0.0
        for item in self.__players:
            result += item.Stability
        return result/ len(self.__players) * (self.__coach.GetRate()/100)
    def Print(self):
        print("姓名\t身份证号\t位置\t攻击指数\t防守指数\t稳定性\t综合评价")
        for i in self.__players:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(
                i.Name,i.Id,i.Position,i.AttackPower,i.DefendPower,i.Stability,i.GetRate()))

