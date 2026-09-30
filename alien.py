import pgzrun
from random import randint

WIDTH = 500
HEIGHT = 500
TITLE = "Good Shot"

alien = Actor("alien.png")

message=""
def place_alien():
    alien.x = randint(50, WIDTH - 50)
    alien.y = randint(50, HEIGHT - 50)
def draw():
    screen.clear()
    screen.fill((128,0,0))
    alien.draw()
    screen.draw.text(message,center=(400, 10), fontsize=30)

def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        place_alien()
        message="Good Shot"
    else:
        message="You Missed"

place_alien                

pgzrun.go()