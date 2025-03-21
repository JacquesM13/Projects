from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_movement = 3
        self.x_movement = 4
        self.move_speed = 0.02

    def move(self):
        self.goto(self.xcor() + self.x_movement, self.ycor() + self.y_movement)

    def bounce_y(self):
        self.y_movement *= -1

    def bounce_x(self):
        self.x_movement *= -1
        self.move_speed *= 0.8

    def refresh(self):
        self.goto(0, 0)
        self.bounce_x()
        self.bounce_y()
        self.move_speed = 0.02