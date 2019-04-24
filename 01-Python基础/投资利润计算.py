"""
财务报表显示程序
输入初始投资金额，投资年数，和回报率
输出每年的盈利情况和总计情况
JerryLiu
20190423
"""

startBalance = float(input("输入总的投资金额： "))
years = int(input("输入投资年数: "))
rate = int(input("输入回报率%: "))
rate = rate / 100


totalInterest = 0.0#初始化总利润

# 显示表头
print("{:4}{:18}{:10}{:16}".format("Year", "Starting balance",
       "Interest", "Ending balance"))

# 计算每年的情况
for year in range(1, years + 1):
    interest = startBalance * rate
    endBalance = startBalance + interest
    print("{:4}{:18.2f}{:10.2f}{:16.2f}".format(year, startBalance, interest, endBalance))
    startBalance = endBalance
    totalInterest += interest

# 显示最终情况
print("最终金额: {:.2f}".format(endBalance))
print("最终利润: {:.2f}".format(totalInterest))
   
   
