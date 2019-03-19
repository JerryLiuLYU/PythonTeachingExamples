import turtle
turtle.setup(650,350,200,200)#设置画布 setup(宽650，高350)
turtle.pensize(25)#设置画笔大小
turtle.pencolor("purple")#设置画笔颜色

turtle.penup()#抬起笔
turtle.bk(200)#画笔后移200个像素
turtle.pendown()#落下笔

turtle.right(40)#像右转40度
for i in range(3):#循环3次
    turtle.circle(40,80)#画圆circle(半径，角度)
    turtle.circle(-40,80)
turtle.circle(40,40)
turtle.fd(40)#向前移40个像素
turtle.circle(16,180)#画半径为16角度为180的圆
turtle.fd(15)#画笔前移15个像素

turtle.done()#使画笔完成后 关闭画布
