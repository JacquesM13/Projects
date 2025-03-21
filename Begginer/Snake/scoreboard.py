from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 22, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        # self.high_score = 0
        self.score = -1
        self.hideturtle()
        self.penup()
        self.sety(270)
        self.pencolor("white")
        self.increment()

    def increment(self):
        self.clear()
        self.score += 1
        self.write(arg= f"Score: {self.score}   High Score: {self.high_score}", align= ALIGNMENT, font= FONT)

    # def game_over(self):
    #     self.sety(0)
    #     self.write(arg=f"Game Over", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            with open("high_score.txt", mode= "w") as file:
                file.write(str(self.score))
                self.high_score = self.score
        self.clear()
        self.score = 0
        self.write(arg=f"Score: {self.score}   High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

