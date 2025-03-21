from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        # self.speed("fastest")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)
        self.left(90)

    def paddle_up(self):
        self.forward(10)

    def paddle_down(self):
        self.backward(10)