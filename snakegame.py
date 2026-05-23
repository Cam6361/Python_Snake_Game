# Simple Python Snake Game
# Controls: W A S D

import turtle
import time
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
MOVE_DISTANCE = 20
DELAY = 0.1

score = 0
segments = []

screen = turtle.Screen()
screen.title("Python Snake Game")
screen.bgcolor("#306998")  # Python blue
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

snake = turtle.Turtle()
snake.shape("square")
snake.color("#FFD43B")  # Python yellow
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(100, 100)

score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: 0", align="center", font=("Arial", 20, "normal"))


def update_score():
    score_display.clear()
    score_display.write(f"Score: {score}", align="center", font=("Arial", 20, "normal"))


def show_game_over():
    score_display.clear()
    score_display.write("Game Over!", align="center", font=("Arial", 24, "normal"))


def go_up():
    if snake.direction != "down":
        snake.direction = "up"


def go_down():
    if snake.direction != "up":
        snake.direction = "down"


def go_left():
    if snake.direction != "right":
        snake.direction = "left"


def go_right():
    if snake.direction != "left":
        snake.direction = "right"


def move_snake():
    if snake.direction == "up":
        snake.sety(snake.ycor() + MOVE_DISTANCE)
    elif snake.direction == "down":
        snake.sety(snake.ycor() - MOVE_DISTANCE)
    elif snake.direction == "left":
        snake.setx(snake.xcor() - MOVE_DISTANCE)
    elif snake.direction == "right":
        snake.setx(snake.xcor() + MOVE_DISTANCE)


def reset_game():
    global score

    show_game_over()
    time.sleep(1)

    snake.goto(0, 0)
    snake.direction = "stop"

    for segment in segments:
        segment.goto(1000, 1000)

    segments.clear()
    score = 0
    update_score()


screen.listen()
screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_left, "a")
screen.onkeypress(go_right, "d")

while True:
    screen.update()

    if snake.xcor() > 290 or snake.xcor() < -290 or snake.ycor() > 290 or snake.ycor() < -290:
        reset_game()

    if snake.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("#FFE873")  # lighter Python yellow
        new_segment.penup()
        segments.append(new_segment)

        score += 10
        update_score()

    for index in range(len(segments) - 1, 0, -1):
        previous_x = segments[index - 1].xcor()
        previous_y = segments[index - 1].ycor()
        segments[index].goto(previous_x, previous_y)

    if len(segments) > 0:
        segments[0].goto(snake.xcor(), snake.ycor())

    move_snake()

    for segment in segments:
        if segment.distance(snake) < 20:
            reset_game()

    time.sleep(DELAY)