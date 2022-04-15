from turtle import Turtle,Screen
from Paddle import Paddle
from Ball import Ball
import time
from Scoreboard import Scoreboard

#creating screen
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.tracer(0)

#creating ball
# ball = Ball()

#creating right and left paddle
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(r_paddle.goup,"Up")
screen.onkey(r_paddle.godown,"Down")
screen.onkey(l_paddle.goup,"w")
screen.onkey(l_paddle.godown,"s")

tim = Turtle()
# tim.shape("square")
# tim.shapesize(stretch_wid=5,stretch_len=1)
# tim.color("white")

game_on = True
while game_on:
    time.sleep(ball.movespeed)
    screen.update()
    ball.move()
    if ball.ycor() > 285 or ball.ycor()<-285:
        ball.wall_coll()

    #detect collition with paddle
    if ball.distance(r_paddle)<50 and ball.xcor() > 320 or ball.distance(l_paddle)<50 and ball.xcor() < -320:
        ball.paddle_coll()
        ball.speedup()
        print("contact")

    #point detection from paddle
    if ball.xcor() > 380:
        ball.reset_pos(ball.xcor())
        scoreboard.leftscore()
    if ball.xcor() < -380:
        ball.reset_pos(ball.xcor())
        scoreboard.rightscore()
















screen.exitonclick()
