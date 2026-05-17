import turtle
import random
import time
e=[]
snake=turtle.Turtle()
snake.penup()
ball=turtle.Turtle()
ball.penup()
a=turtle.Screen()
a.title("Snake game")
a.bgcolor("black")
snake.width(5)
snake.speed(0)
snake.shape("square")
snake.color("white")
snake.direction="Up"
ball.shape("circle")
ball.color("red")
def up():
    snake.direction="Up"
def down():
   snake.direction="Down"
def left():
    snake.direction="Left"
def right():
    snake.direction="Right"
a.listen()
a.onkey(up,"Up")
a.onkey(down,"Down")
a.onkey(left,"Left")
a.onkey(right,"Right")
def move():
    if snake.direction=="Up":
        b=snake.ycor()
        b=b+30
        snake.sety(b)
    elif snake.direction=="Down":
        b=snake.ycor()
        b=b-30
        snake.sety(b)
    elif snake.direction=="Left":
        b=snake.xcor()
        b=b-30
        snake.setx(b)
    elif snake.direction=="Right":
        b=snake.xcor()
        b=b+30
        snake.setx(b)
while True:
##    if snake.ycor()-5<=ball.ycor()<=snake.ycor()+5 and snake.xcor()-5<=ball.xcor()<=snake.xcor()+5:
    if snake.ycor()>=400 or snake.ycor()<=-400 or snake.xcor()>=400 or snake.xcor()<=-400:
        snake.hideturtle()
        snake.setpos(0,0)
        snake.showturtle()
        for i in e:
            i.setpos(1000,1000)
        e.clear()
    if snake.distance(ball)<=20:
        ball.hideturtle()
        ball.setpos(random.randint(-400,400),random.randint(-400,400))
        ball.showturtle()
        d=turtle.Turtle()
        d.speed(0)
        d.shape("square")
        d.color("grey")
        e.append(d)
        d.penup()
    if len(e)>0:
        e[0].setpos(snake.xcor(),snake.ycor())
        for i in range(len(e)-1,0,-1):
                x=e[i-1].xcor() 
                y=e[i-1].ycor() 
                e[i].setpos(x,y)     
    move()
    time.sleep(0.1)
    
    






    

