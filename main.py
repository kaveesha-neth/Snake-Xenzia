import time
from gui import setup_screen, draw_border, create_head, create_food, create_scoreboard
from functions import *

screen = setup_screen()
draw_border()

head = create_head()
food = create_food()
score_board = create_scoreboard()

bind_keys(screen, head)

while True:
    screen.update()

    check_collisions(head, score_board)
    check_food(head, food, score_board)
    move_segments(head)
    move(head)

    time.sleep(get_delay())
