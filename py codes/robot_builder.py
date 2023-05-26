import turtle as t 

def rectangle(horizontal,vertical,color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for counter in range(1,3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()

t.penup()
t.speed('normal')
t.bgcolor('Dodger blue')

#feet
t.goto(-100, -150)
rectangle(50,20,'blue')
t.goto(-30,-150)
rectangle(50,20,'blue')

#legs
t.goto(-20, -50)
rectangle(15,100,'grey')
t.goto(-55,-50)
rectangle(-15,100,'grey')

#body
t.goto(-90,100)
rectangle(100,150,'red')

#arms
t.goto(-150, 70)
rectangle(60,15,'gold')
t.goto(-150,110)
rectangle(15,40,'gold')

t.goto(10, 70)
rectangle(60,15,'gold')
t.goto(55,110)
rectangle(15,40,'gold')

#neck
t.goto(-50,120)
rectangle(15,20,'gold')

#head
t.goto(-85,170)
rectangle(80,50,'pink')

#eyes
t.goto(-65, 155)
rectangle(40,15,'white')
t.goto(-60,150)
rectangle(5,5,'black')
t.goto(-40,150)
rectangle(5,5,'black')

#mouth
t.goto(-55,130)
rectangle(25,5,'black')
t.hideturtle()
