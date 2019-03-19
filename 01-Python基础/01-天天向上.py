import math
def DayUp(dayfactor):
    dayfactor = dayfactor / 1000
    dayup = math.pow((1.0 + dayfactor), 365) # 每天提高0.01
    daydown = math.pow((1.0 - dayfactor), 365) # 每天荒废0.01
    if dayfactor*100 < 1:
        print("N={}‰, UP={:.2f}, DW={:.2f}, UP/DW={:.2f}".format(int(dayfactor*1000),dayup,daydown,dayup/daydown))
    elif dayfactor*100 == 1:
        print("N={}%, UP={:.2f}, DW={:.2f}, UP/DW={:.2f}".format(int(dayfactor*100),dayup,daydown,dayup/daydown))  
for i in range(0,11):
    DayUp(i)
