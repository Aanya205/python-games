import turtle
import time

screen = turtle.getscreen()
screen.setup(width=700, height=700)
screen.title("Maze Game")
screen.bgcolor("skyblue")

man = turtle.Turtle()
man.penup()
man.goto(90, 350)
man.color("red")
man.shape("circle")
man.shapesize(stretch_wid=1, stretch_len=1)


score1 = 0
score = turtle.Turtle()
score.penup()
score.goto(300,300)
score.write("Score : 0", font = ("Ariel", 20, "bold"))
score.color("Black")




rectangle1 = turtle.Turtle()
rectangle1.penup()
rectangle1.goto(200,200)
rectangle1.shape("square")
rectangle1.shapesize(stretch_wid=11, stretch_len=0.5)

# to make it vertical and horizontal change the width and the height

rectangle2 = turtle.Turtle()
rectangle2.penup()
rectangle2.goto(160,90)
rectangle2.shape("square")
rectangle2.shapesize(stretch_wid=0.5, stretch_len=4)

rectangle3 = turtle.Turtle()
rectangle3.penup()
rectangle3.goto(125,110)
rectangle3.shape("square")
rectangle3.shapesize(stretch_wid=2, stretch_len=0.5)

rectangle4 = turtle.Turtle()
rectangle4.penup()
rectangle4.goto(100,130)
rectangle4.shape("square")
rectangle4.shapesize(stretch_wid=0.5, stretch_len=6)

rectangle5 = turtle.Turtle()
rectangle5.penup()
rectangle5.goto(150,150)
rectangle5.shape("square")
rectangle5.shapesize(stretch_wid=2, stretch_len=0.5)

rectangle6 = turtle.Turtle()
rectangle6.penup()
rectangle6.goto(185,90)
rectangle6.shape("square")
rectangle6.shapesize(stretch_wid=0.5, stretch_len=2)

rectangle7 = turtle.Turtle()
rectangle7.penup()
rectangle7.goto(70,150)
rectangle7.shape("square")
rectangle7.shapesize(stretch_wid=2, stretch_len=0.5)

rectangle8 = turtle.Turtle()
rectangle8.penup()
rectangle8.goto(85,170)
rectangle8.shape("square")
rectangle8.shapesize(stretch_wid=0.5, stretch_len=2)

rectangle9 = turtle.Turtle()
rectangle9.penup()
rectangle9.goto(10,90)
rectangle9.shape("square")
rectangle9.shapesize(stretch_wid=0.5, stretch_len=4)

rectangle10 = turtle.Turtle()
rectangle10.penup()
rectangle10.goto(-30,200)
rectangle10.shape("square")
rectangle10.shapesize(stretch_wid=11, stretch_len=0.5)

rectangle11 = turtle.Turtle()
rectangle11.penup()
rectangle11.goto(0,310)
rectangle11.shape("square")
rectangle11.shapesize(stretch_wid=0.5, stretch_len=4)

rectangle12 = turtle.Turtle()
rectangle12.penup()
rectangle12.goto(0,250)
rectangle12.shape("square")
rectangle12.shapesize(stretch_wid=0.5, stretch_len=4)

rectangle13 = turtle.Turtle()
rectangle13.penup()
rectangle13.goto(40,240)
rectangle13.shape("square")
rectangle13.shapesize(stretch_wid=1.5, stretch_len=0.5)

rectangle14 = turtle.Turtle()
rectangle14.penup()
rectangle14.goto(80,220)
rectangle14.shape("square")
rectangle14.shapesize(stretch_wid=0.5, stretch_len=4)

rectangle15 = turtle.Turtle()
rectangle15.penup()
rectangle15.goto(150,310)
rectangle15.shape("square")
rectangle15.shapesize(stretch_wid=0.5, stretch_len=5)

rectangle16 = turtle.Turtle()
rectangle16.penup()
rectangle16.goto(100,290)
rectangle16.shape("square")
rectangle16.shapesize(stretch_wid=2, stretch_len=0.5)

rectangle17 = turtle.Turtle()
rectangle17.penup()
rectangle17.goto(130,270)
rectangle17.shape("square")
rectangle17.shapesize(stretch_wid=0.5, stretch_len=3)

rectangle18 = turtle.Turtle()
rectangle18.penup()
rectangle18.goto(-10,150)
rectangle18.shape("square")
rectangle18.shapesize(stretch_wid=0.5, stretch_len=2)

rectangle19 = turtle.Turtle()
rectangle19.penup()
rectangle19.goto(10,170)
rectangle19.shape("square")
rectangle19.shapesize(stretch_wid=2, stretch_len=0.5)



coin1 = turtle.Turtle()
coin1.penup()
coin1.goto(10,110)
coin1.shape("circle")
coin1.fillcolor("yellow")
coin1.shapesize(stretch_wid=0.5, stretch_len=0.5)

coin2 = turtle.Turtle()
coin2.penup()
coin2.goto(100,200)
coin2.shape("circle")
coin2.fillcolor("yellow")
coin2.shapesize(stretch_wid=0.5, stretch_len=0.5)

coin3 = turtle.Turtle()
coin3.penup()
coin3.goto(20,270)
coin3.shape("circle")
coin3.fillcolor("yellow")
coin3.shapesize(stretch_wid=0.5, stretch_len=0.5)

def goup():
  y=man.ycor()
  y=y+10
  man.sety(y)
def godown():
  y=man.ycor()
  y=y-3
  man.sety(y)

def goright():
  x=man.xcor()
  x=x+3
  man.setx(x)

def goleft():
  x=man.xcor()
  x=x-3
  man.setx(x)

screen.listen()
screen.onkeypress(goup, "Up")
screen.onkeypress(godown, "Down")
screen.onkeypress(goright, "Right")
screen.onkeypress(goleft,"Left")








while True:
  screen.update()

  if (man.distance(rectangle1) < 20 or  man.distance(rectangle2) < 20 or man.distance(rectangle3) < 20 or man.distance(rectangle4) < 20 or  man.distance(rectangle5) < 20 or man.distance(rectangle6) < 20 or  man.distance(rectangle7) < 20 or man.distance(rectangle8) < 20 or man.distance(rectangle9) < 20 or man.distance(rectangle10) < 20 or  man.distance(rectangle11) < 20 or man.distance(rectangle12) < 20 or  man.distance(rectangle13) < 20 or man.distance(rectangle14) < 20 or man.distance(rectangle15) < 20 or man.distance(rectangle16) < 20 or man.distance(rectangle17) < 20 or man.distance(rectangle18) < 20):
    man.goto(90,350) and print("Game Over")


  if man.distance(coin1) < 10: 
    score.clear()
    score1 = score1+1
    time.sleep(3)
    score.write("Score : {}".format(score1),font = ("Ariel", 20, "bold"))
    coin1.hideturtle()

  if man.distance(coin2)<10:
    score.clear()
    score1=score1+1
    time.sleep(3)
    score.write("Score : {}".format(score1),font = ("Ariel", 20, "bold"))
    coin2.hideturtle()

  if man.distance(coin3)<10:
    score.clear()
    score1= score1+1
    time.sleep(3)
    score.write("Score: {}".format(score1), font = ("Areil", 20, "bold"))
    coin3.hideturtle()
    
    
    


