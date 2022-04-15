from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.7,stretch_wid=0.7)
        self.color("white")
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.movespeed = 0.1

    def move(self):
        new_x = self.xcor()+ self.xmove
        new_y = self.ycor()+ self.ymove
        self.goto(new_x,new_y)

    def wall_coll(self):
        self.ymove *= -1

    def paddle_coll(self):
        self.xmove *= -1

    def reset_pos(self,x_pos):
        self.goto(0,0)
        self.movespeed = 0.1
        if x_pos>380:
            self.xmove *= -1
        elif x_pos<-380:
            self.xmove *= -1

    def speedup(self):
        self.movespeed *= 0.9