import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0
segments = []

def go_up(head):
    if head.direction != "down":
        head.direction = "up"

def go_down(head):
    if head.direction != "up":
        head.direction = "down"

def go_left(head):
    if head.direction != "right":
        head.direction = "left"

def go_right(head):
    if head.direction != "left":
        head.direction = "right"

def move(head):
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    elif head.direction == "down":
        head.sety(head.ycor() - 20)
    elif head.direction == "left":
        head.setx(head.xcor() - 20)
    elif head.direction == "right":
        head.setx(head.xcor() + 20)

def bind_keys(screen, head):
    screen.listen()
    screen.onkeypress(lambda: go_up(head), "Up")
    screen.onkeypress(lambda: go_down(head), "Down")
    screen.onkeypress(lambda: go_left(head), "Left")
    screen.onkeypress(lambda: go_right(head), "Right")

def reset_game(head, board):
    global score, delay, segments
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"

    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()

    score = 0
    delay = 0.1
    update_score(board)

def update_score(board):
    board.clear()
    board.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

def check_collisions(head, board):
    if head.xcor() > 250 or head.xcor() < -240 or head.ycor() > 220 or head.ycor() < -240:
        reset_game(head, board)

    for segment in segments:
        if segment.distance(head) < 20:
            reset_game(head, board)

def check_food(head, food, board):
    global score, high_score, delay
    if head.distance(food) < 20:
        x = random.randint(-240, 240)
        y = random.randint(-220, 220)
        food.goto(x, y)

        score += 10
        if score > high_score:
            high_score = score

        delay = max(0.01, delay - 0.001)
        add_segment()
        update_score(board)

def add_segment():
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("grey")
    new_segment.penup()
    segments.append(new_segment)

def move_segments(head):
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if segments:
        segments[0].goto(head.xcor(), head.ycor())

def get_delay():
    return delay
