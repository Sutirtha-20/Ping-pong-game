from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.left(90)
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(position)

    def goup(self):
        self.forward(20)

    def godown(self):
        self.back(20)
