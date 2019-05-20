class League:
    def __init__(self, name=""):
        self.Name = name
        self.__teams = []
    def AddTeam(self, team):
        result = [item for item in self.__teams if item.Name == team.Name]
        if len(result) == 0:
            self.__teams.append(team)
            return team
        else:
            return -1
    def GetTeam(self, teamName):
        result = [item for item in self.__teams if item.Name == teamName]
        if (len(result) == 1):
            return result[0]
        else:
            return None
    def Print(self):
        print("球队名称\t球队攻击力\t球队防御力\t球队稳定性\t球队综合能力")
        for i in self.__teams:
            print("{}\t{:.2f}\t{:.2f}\t{:.2f}\t{:.2f}".format(i.Name,i.GetTeamAttackPower(),i.GetTeamDefendPower(),i.GetTeamStabilityPower(),i.GetRate()))