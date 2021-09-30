x1=int(input("x1:"))
y1=int(input("y1:"))
x2=int(input("x2:"))
y2=int(input("y2:"))
length=(((x1-x2)**2+(y1-y2)**2))**0.5

import turtle
t=turtle.Turtle()
t.shape("turtle")
t.up()
t.goto(x1,x2)
t.down()
t.goto(x2,y2)
t.write("두 점 사이의 길이:"+str(length))
