from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.listen()
screen.tracer(0)
screen.setup(width= 800, height= 600)
screen.bgcolor("black")
screen.title("Pong")

paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))

ball = Ball()

score = Score()

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)
    screen.onkeypress(paddle_right.paddle_up, "Up")
    screen.onkeypress(paddle_right.paddle_down, "Down")
    screen.onkeypress(paddle_left.paddle_up, "w")
    screen.onkeypress(paddle_left.paddle_down, "s")

    # Detect collision with ceiling/floor
    if abs(ball.ycor()) > 280:
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.distance(paddle_left) < 50 and ball.xcor() < -330) or (ball.distance(paddle_right) < 50 and ball.xcor() > 330):
        ball.bounce_x()

    # Detect goals and update score
    elif abs(ball.xcor()) > 360:
        score.goal(ball.xcor())
        ball.refresh()

screen.exitonclick()