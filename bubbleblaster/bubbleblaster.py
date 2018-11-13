# bring in tkinter library
from tkinter import *

class Ship() :

    def create_ship_parts(self, c) :
        ship_parts = list()
        ship_parts.append(c.create_polygon(15, 15, 40, 25, 15, 35, fill='red')) # control room
        ship_parts.append(c.create_oval(10, 10, 40, 40, outline='red')) # ships hull
        ship_parts.append(c.create_polygon(0, 20, 10, 20, 10, 30, 0, 30, fill='red')) # tail
        ship_parts.append(c.create_rectangle(25, 2, 28, 10, fill='red')) # telescope
        ship_parts.append(c.create_rectangle(28, 2, 33, 5, fill='red')) # telescope
        ship_parts.append(c.create_text(20, 25, anchor=W, font="Purisa", text="A")) # name
        return ship_parts
    
    def move_ship(self, x, y, ship_parts, c) :
        for i in range(len(ship_parts)) :
            c.move(ship_parts[i], x, y)

    def get_ship_hull(self, ship_parts) :
        return ship_parts[1]


# create the blue window with title 'Bubble Blaster'
HEIGHT = 500
WIDTH = 800
window = Tk()
window.title('Bubble Blaster')
c = Canvas(window, width=WIDTH, height=HEIGHT, bg='darkblue')
c.pack()

SHIP_R = 15
MID_X = WIDTH / 2
MID_Y = HEIGHT / 2

# create the red ship and move it to the center
ship = Ship()
ship_parts = ship.create_ship_parts(c)
ship.move_ship(MID_X, MID_Y, ship_parts, c)

SHIP_SPD = 10
def move_ship(event) :
    if event.keysym == 'Up' :
        ship.move_ship(0, -SHIP_SPD, ship_parts, c)
    elif event.keysym == 'Down' :
        ship.move_ship(0, SHIP_SPD, ship_parts, c)
    elif event.keysym == 'Left' :
        ship.move_ship(-SHIP_SPD, 0, ship_parts, c)
    elif event.keysym == 'Right' :
        ship.move_ship(SHIP_SPD, 0, ship_parts, c)
c.bind_all('<Key>', move_ship)


from random import randint
bub_id = list()
bub_r = list()
bub_speed = list()
MIN_BUB_R = 10
MAX_BUB_R = 30
MAX_BUB_SPD = 10
GAP = 100
def create_bubble() :
    x = WIDTH + GAP
    y = randint(0, HEIGHT)
    r = randint(MIN_BUB_R, MAX_BUB_R)
    id1 = c.create_oval(x - r, y - r, x + r, y + r, outline = 'white')
    bub_id.append(id1)
    bub_r.append(r)
    bub_speed.append(randint(1, MAX_BUB_SPD))

def move_bubbles() :
    for i in range(len(bub_id)) :
        c.move(bub_id[i], -bub_speed[i], 0)

from time import sleep, time
BUB_CHANCE = 10
TIME_LIMIT = 30
BONUS_SCORE = 1000
score = 0
bonus = 0
end = time() + TIME_LIMIT

def get_coords(id_num) :
    pos = c.coords(id_num)
    x = (pos[0] + pos[2])/2
    y = (pos[1] + pos[3])/2
    return x, y

def del_bubble(i):
    del bub_r[i]
    del bub_speed[i]
    c.delete(bub_id[i])
    del bub_id[i]

def clean_up_bubs() :
    for i in range(len(bub_id) - 1, -1, -1) :
        x, y = get_coords(bub_id[i])
        if x < -GAP :
            del_bubble(i)

from math import sqrt
def distance(id1, id2) :
    x1, y1 = get_coords(id1)
    x2, y2 = get_coords(id2)
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def collision() :
    points = 0
    for bub in range(len(bub_id)-1, -1, -1) :
        if distance(ship.get_ship_hull(ship_parts), bub_id[bub]) < (SHIP_R + bub_r[bub]) :
            points += (bub_r[bub] + bub_speed[bub])
            del_bubble(bub)
            ship.move_ship(-SHIP_SPD * 5, 0, ship_parts, c)
    return points

c.create_text(50, 30, text='TIME', fill='white')
c.create_text(150, 30, text='SCORE', fill='white')
time_text = c.create_text(50, 50, fill='white')
score_text = c.create_text(150, 50, fill='white')
def show_score(score) :
    c.itemconfig(score_text, text=str(score))
def show_time(time_left) :
    c.itemconfig(time_text, text=str(time_left))

score = 0

#MAIN GAME LOOP
while time() < end :
    if randint(1, BUB_CHANCE) == 1 :
        create_bubble()
    move_bubbles()
    clean_up_bubs()
    score += collision()
    if (int(score / BONUS_SCORE)) > bonus :
        bonus += 1
        end += TIME_LIMIT
    show_score(score)
    show_time(int(end - time()))
    window.update()
    sleep(0.01)





