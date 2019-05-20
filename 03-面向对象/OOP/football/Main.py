from League import League 
from Team import Team
from TeamMember import *
from DataInit import DataInit
from Match import *
def NewTeam(league):
    newTeam = Team()
    strNewTeamName = input("请输入球队名称：")
    newTeam.Name = strNewTeamName
    while True:
        isAddPlayer = input("是否添加球员？Y or N :")
        if isAddPlayer.upper() == "N":
            break
        else:
            strNewPlayerName = input("请输入球员姓名：")
            strNewPlayerId = input("请输入球员ID：")
            strNewPlayerPosition = input("请输入球员位置：(前锋,中场,后卫,门将) ")
            while strNewPlayerPosition not in TeamMember.Positions:
                print("输入有误")
                strNewPlayerPosition = input("请输入球员位置：(前锋,中场,后卫,门将) ")
            strNewPlayerAttack = input("请输入球员攻击力（0-100）：")
            strNewPlayerDefend = input("请输入球员防御力（0-100）：")
            strNewPlayerStability = input("请输入球员稳定性（0-100）：")
            newPlayer = Player()
            newPlayer.Name = strNewPlayerName
            newPlayer.Id = strNewPlayerId
            newPlayer.Position = strNewPlayerPosition
            newPlayer.AttackPower = float(strNewPlayerAttack)
            newPlayer.DefendPower = float(strNewPlayerDefend)
            newPlayer.Stability = float(strNewPlayerStability)
            newTeam.AddPlayer(newPlayer)
    print("请添加教练信息")
    strNewCoachName = input("请输入教练姓名：")
    strNewCoachId = input("请输入教练ID：")
    strNewCoachPersonalPower = input("请输入教练个人魅力（0-100）：")
    strNewCoachTacticsPower = input("请输入教练战术指数（0-100）：")
    newCoach = Coach()
    newCoach.Name = strNewCoachName
    newCoach.Id = strNewCoachId
    newCoach.PersonalPower = float(strNewCoachPersonalPower)
    newCoach.TacticsPower = float(strNewCoachTacticsPower)
    newTeam.AddCoach(newCoach)

    league.AddTeam(newTeam)

def ShowTeam(league):
    teamName = input("请输入显示的队伍名称：")
    team = league.GetTeam(teamName)
    if team is not None:
        team.Print()

def StartMatch(league):
    homeTeamName = input("请输入主队队伍名称：")
    awayTeamName = input("请输入客队队伍名称：")
    homeTeam = league.GetTeam(homeTeamName)
    awayTeam = league.GetTeam(awayTeamName)
    if homeTeam is not None and awayTeam is not None:
        match = Match(homeTeam, awayTeam)
        match.Run()
        match.Print()
def MultiMatch(league):
    homeTeamName = input("请输入主队队伍名称：")
    awayTeamName = input("请输入客队队伍名称：")
    homeTeam = league.GetTeam(homeTeamName)
    awayTeam = league.GetTeam(awayTeamName)
    match = Match(homeTeam, awayTeam)
    num = int(input("比赛次数："))
    results = []
    homeWins = 0
    Draws = 0
    awayWins = 0
    for i in range(num):
        homeGoals, awayGoals = match.Run()
        results.append("{}:{}".format(homeGoals, awayGoals))
        if homeGoals > awayGoals:
            homeWins += 1
        elif homeGoals == awayGoals:
            Draws += 1
        else:
            awayWins += 1
    print("共比赛{}场，{}赢{}次，平{}次，输{}次".format(num, homeTeamName, homeWins, Draws, awayWins))
    print(results)


MENUS = ("退出","新建球队", "显示球队信息","显示联赛信息","开始比赛","比赛多次")
strName = input("请输入联赛名称：")
league = League(strName)
DataInit.DataInit(league)
while True:
    print("欢迎进入{}联赛".format(strName))
    print("-" * 80)
    for i,item in enumerate(MENUS):
        print(i, "-", item)
    print("-" * 80)
    userSelect = input("请选择操作：")
    if userSelect == "0":
        break # 退出
    elif userSelect == "1":
        pass  #新建球队
        NewTeam(league)
    elif userSelect == "2":
        pass  #显示球队信息
        ShowTeam(league)
    elif userSelect == "3":
        pass  #显示联赛信息
        league.Print()
    elif userSelect == "4":
        pass  #开始比赛
        StartMatch(league)
    elif userSelect == "5":
        pass  #比赛多次
        MultiMatch(league)
    else:
        print("选择错误，请重新选择")

