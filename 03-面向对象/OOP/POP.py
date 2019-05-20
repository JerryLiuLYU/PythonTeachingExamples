STUDENT_NUM = 5
StudentNames = []
StudentScores = []
for i in range(STUDENT_NUM):
    strName = input("请输入第{}学生的姓名".format(i + 1))
    intScore = int(input("请输入第{}学生的成绩".format(i + 1)))
    StudentNames.append(strName)
    StudentScores.append(intScore)

print("成绩列表：")
for n, name in enumerate(StudentNames):
    print(name, StudentScores[n])
print("不及格的学生：")

less60student = [StudentNames[i] for i, score in enumerate(StudentScores) if score < 60]
print(less60student)

