from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 80, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.pencolor("white")
        self.sety(200)
        self.score_l = 0
        self.score_r = 0
        self.write(arg= f"{self.score_l}   {self.score_r}", align= ALIGNMENT, font= FONT)

    def goal(self, x_cor):
        self.clear()
        if x_cor < 0:
            self.score_r += 1
        elif x_cor > 0:
            self.score_l += 1
        self.write(f"{self.score_l}   {self.score_r}", align=ALIGNMENT, font=FONT)

