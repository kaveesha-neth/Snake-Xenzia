import turtle

def setup_screen():
    screen = turtle.Screen()
    screen.title("Snake Xenzia")
    screen.bgcolor("black")
    screen.setup(width=600, height=600)
    screen.tracer(0)
    return screen

def draw_border():
    draw = turtle.Turtle()
    draw.speed(10)
    draw.pencolor("white")
    draw.penup()
    draw.goto(-260, 240)
    draw.hideturtle()
    draw.pendown()
    for _ in range(2):
        draw.forward(520)
        draw.right(90)
        draw.forward(500)
        draw.right(90)

def create_head():
    head = turtle.Turtle()
    head.speed(0)
    head.shape("square")
    head.color("white")
    head.penup()
    head.goto(0, 0)
    head.direction = "stop"
    return head

def create_food():
    food = turtle.Turtle()
    food.speed(0)
    food.shape("circle")
    food.color("red")
    food.penup()
    food.goto(0, 100)
    return food

def create_scoreboard():
    board = turtle.Turtle()
    board.speed(0)
    board.shape("square")
    board.color("white")
    board.penup()
    board.hideturtle()
    board.goto(0, 260)
    board.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))
    return board

