from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

score_board = ScoreBoard()
snake = Snake()
food = Food()
screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")
game_is_on = True
score_board.score = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()

    # Detect collision with the food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()

    # Detect collision with the wall
    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 290 or \
            snake.segments[0].ycor() < -290:
        game_is_on = False
        score_board.game_over()

    # Detect collision with the tail
    for i in range(1, len(snake.segments), 1):
        if snake.segments[0].distance(snake.segments[i]) <= 10:
            game_is_on = False
            score_board.game_over()

screen.exitonclick()