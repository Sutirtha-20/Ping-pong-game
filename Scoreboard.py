from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.lscore = 0
        self.rscore = 0
        self.shape("square")
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-50, 250)
        self.write("Score: {} | {}".format(self.lscore,self.rscore), align="center", font=("Courier", 40, "normal"))

    def leftscore(self):
        self.lscore += 1
        self.clear()
        self.write("Score: {} | {}".format(self.lscore, self.rscore), align="center", font=("Courier", 40, "normal"))

    def rightscore(self):
        self.rscore += 1
        self.clear()
        self.write("Score: {} | {}".format(self.lscore, self.rscore), align="center", font=("Courier", 40, "normal"))