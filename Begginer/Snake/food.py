from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()                                               # So we don't draw lines between food locations
        self.shapesize(stretch_len= 0.5, stretch_wid= 0.5)         # Halve default 20x20 dimensions
        self.color("green")
        self.speed("fastest")                                      # So we don't have to see the food moving across screen
        self.refresh()                                             # Initial position

    def refresh(self):
        rand_x = random.randint(-280, 280)                      # Playing field is -300 to 300 in x and y...
        rand_y = random.randint(-280, 260)                      # ... don't want food right on the edge
        self.goto(rand_x, rand_y)