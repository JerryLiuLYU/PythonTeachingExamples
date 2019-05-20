from Team import Team
from TeamMember import *
class DataInit:
    def DataInit(league):
        team1 = Team()
        team1.Name = "巴萨"
        team2 = Team()
        team2.Name = "皇马"
        team3 = Team()
        team3.Name = "中国队"
        coach1 = Coach()
        coach1.Name = "巴尔韦德"
        coach1.PersonalPower = 80
        coach1.TacticsPower = 85
        team1.AddCoach(coach1)
        coach2 = Coach()
        coach2.Name = "齐达内"
        coach2.PersonalPower = 97
        coach2.TacticsPower = 90
        team2.AddCoach(coach2)
        coach3 = Coach()
        coach3.Name = "里皮"
        coach3.PersonalPower = 90
        coach3.TacticsPower = 80
        team3.AddCoach(coach3)

        player11 = Player()
        player11.Name = "梅西"
        player11.Id = "001"
        player11.Position = "前锋"
        player11.AttackPower = 99
        player11.DefendPower = 40
        player11.Stability = 90
        team1.AddPlayer(player11)

        player12 = Player()
        player12.Name = "布斯克斯"
        player12.Id = "002"
        player12.Position = "中场"
        player12.AttackPower = 69
        player12.DefendPower = 70
        player12.Stability = 90
        team1.AddPlayer(player12)

        player13 = Player()
        player13.Name = "皮克"
        player13.Id = "003"
        player13.Position = "后卫"
        player13.AttackPower = 30
        player13.DefendPower = 80
        player13.Stability = 78
        team1.AddPlayer(player13)

        player14 = Player()
        player14.Name = "特尔施特根"
        player14.Id = "004"
        player14.Position = "门将"
        player14.AttackPower = 10
        player14.DefendPower = 90
        player14.Stability = 95
        team1.AddPlayer(player14)

        player21 = Player()
        player21.Name = "本泽马"
        player21.Id = "021"
        player21.Position = "前锋"
        player21.AttackPower = 89
        player21.DefendPower = 30
        player21.Stability = 90
        team2.AddPlayer(player21)

        player22 = Player()
        player22.Name = "莫德里奇"
        player22.Id = "022"
        player22.Position = "中场"
        player22.AttackPower = 88
        player22.DefendPower = 60
        player22.Stability = 95
        team2.AddPlayer(player22)

        player23 = Player()
        player23.Name = "瓦拉内"
        player23.Id = "023"
        player23.Position = "后卫"
        player23.AttackPower = 30
        player23.DefendPower = 85
        player23.Stability = 80
        team2.AddPlayer(player23)

        player24 = Player()
        player24.Name = "库尔图瓦"
        player24.Id = "024"
        player24.Position = "门将"
        player24.AttackPower = 10
        player24.DefendPower = 90
        player24.Stability = 90
        team2.AddPlayer(player24)

        player31 = Player()
        player31.Name = "吴磊"
        player31.Id = "031"
        player31.Position = "前锋"
        player31.AttackPower = 70
        player31.DefendPower = 10
        player31.Stability = 70
        team3.AddPlayer(player31)

        player32 = Player()
        player32.Name = "蒿俊闵"
        player32.Id = "032"
        player32.Position = "中场"
        player32.AttackPower = 65
        player32.DefendPower = 40
        player32.Stability = 60
        team3.AddPlayer(player32)

        player33 = Player()
        player33.Name = "张琳芃"
        player33.Id = "033"
        player33.Position = "后卫"
        player33.AttackPower = 20
        player33.DefendPower = 65
        player33.Stability = 70
        team3.AddPlayer(player33)

        player34 = Player()
        player34.Name = "王大雷"
        player34.Id = "034"
        player34.Position = "门将"
        player34.AttackPower = 10
        player34.DefendPower = 60
        player34.Stability = 60
        team3.AddPlayer(player34)

        league.AddTeam(team1)
        league.AddTeam(team2)
        league.AddTeam(team3)

