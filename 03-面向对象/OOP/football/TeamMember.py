class TeamMember:
    Positions = ("前锋","中场","后卫","门将","教练")
    def __init__(self):
        self.Id = ""
        self.Name = ""
        self.Position = ""
    def GetRate(self):
        pass

class Player(TeamMember):
    def __init__(self):
        self.AttackPower = 0.0
        self.DefendPower = 0.0
        self.Stability = 0.0
    def GetRate(self):
        if self.Position == "前锋":
            return (self.AttackPower * 0.7 + self.DefendPower * 0.1 + self.Stability * 0.2)
        elif self.Position == "中场":
            return (self.AttackPower * 0.4 + self.DefendPower * 0.4 + self.Stability * 0.2)
        elif self.Position == "后卫":
            return (self.AttackPower * 0.1 + self.DefendPower * 0.5 + self.Stability * 0.4)
        elif self.Position == "门将":
            return (self.AttackPower * 0.0 + self.DefendPower * 0.6 + self.Stability * 0.4)

class Coach(TeamMember):
    def __init__(self):
        self.PersonalPower = 0.0
        self.TacticsPower = 0.0
        self.Position = "教练"
    def GetRate(self):
        return (self.PersonalPower * 0.3 + self.TacticsPower * 0.7)