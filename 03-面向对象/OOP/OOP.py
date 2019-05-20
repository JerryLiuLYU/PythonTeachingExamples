class MyClass:
    STUDENTS_NUM=5
    def __init__(self):
        self.Name = ""
        self.Students = []
    def AddStudent(self, stu):
        if len(self.Students)<5:
            self.Students.append(stu)
        else:
            print("班级只能有5个学生")
    def Print(self):
        print("{}-成绩列表：".format(self.Name))
        for stu in self.Students:
            print(stu.Name, stu.Score)
        print("不及格的学生：")
        less60student = [stu.Name for stu in self.Students if stu.Score < 60]
        print(less60student)
class Student:
    def __init__(self,name,score):
        self.Name = name
        self.Score = score

myClass = MyClass()
myClass.Name = "计科01"
for i in range(myClass.STUDENTS_NUM):
    strName = input("请输入第{}学生的姓名".format(i + 1))
    intScore = int(input("请输入第{}学生的成绩".format(i + 1)))
    stu = Student(strName, intScore)
    myClass.AddStudent(stu)
myClass.Print()