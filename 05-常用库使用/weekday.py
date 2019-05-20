import datetime
WeekNumToChinese = ("零","一","二","三","四","五","六","日",)
strdate = input("请输入一个日期（年-月-日）：")
d = datetime.datetime.strptime(strdate,"%Y-%m-%d")
n = d.isoweekday()
print("{}为星期{}".format(strdate,WeekNumToChinese[n]))
