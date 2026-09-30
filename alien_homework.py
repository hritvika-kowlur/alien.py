import pgzrun
from random import randint

WIDTH = 500
HEIGHT = 500
TITLE = "Good Shot"

bee = Actor("bee - homework task.png")

message=""

vx = 2
vy = 2

def update():
    global vx, vy
    bee.x += vx
    bee.y += vy

    if bee.left < 0 or bee.right > WIDTH:
        vx = -vx
    if bee.top < 0 or bee.bottom > HEIGHT:
        vy = -vy

def place_bee():
    bee.x = randint(50, WIDTH - 50)
    bee.y = randint(50, HEIGHT - 50)
def draw():
    screen.clear()
    screen.fill((0,0,100))
    bee.draw()
    screen.draw.text(message,center=(400, 10), fontsize=30)

def on_mouse_down(pos):
    global message
    if bee.collidepoint(pos):
        place_bee()
        message="Good Shot"
    else:
        message="You Missed"

place_bee                

pgzrun.go()