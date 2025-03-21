from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.listen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")

screen.title("Snake")
screen.tracer(0)

game_is_on = True

snake = Snake()
food = Food()
score = Scoreboard()

screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

while game_is_on:
    screen.update()
    time.sleep(0.06)
    snake.move()

    # Detect collision of snake with food
    if snake.head.distance(food) < 15:
        food.refresh()                          # If collision between snake and food, move food
        score.increment()                       # Increase and update display for score
        snake.extend()

    # Detect collision with wall
    if abs(snake.head.xcor()) > 290 or abs(snake.head.ycor()) > 290:
        score.reset()
        snake.reset()
    # Detect collision with tail - if tail collides with any tail segment
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()