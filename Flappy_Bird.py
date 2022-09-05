import pygame as pg 
import sys

WIDTH = 324
HEIGHT = 576

def draw_floor():
    screen.blit(floor,(floor_x, HEIGHT - HEIGHT/8))
    screen.blit(floor,(floor_x + WIDTH, HEIGHT - HEIGHT/8))


pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
clock = pg.time.Clock()

# Background (Nền)
bg = pg.image.load('assets/background-night.png').convert()
bg = pg.transform.scale( bg, (WIDTH, HEIGHT))

# Bird (Chim)
bird = pg.image.load('assets/yellowbird-midflap.png').convert()


# Floor (Sàn)
floor = pg.image.load('assets/floor.png').convert()
floor = pg.transform.scale( floor, (WIDTH, HEIGHT / 8) )
floor_x = 0

while True:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    screen.blit(bg,(0,0))
    floor_x -= 1
    draw_floor()
    if floor_x <= - WIDTH:
        floor_x = 0
    
    pg.display.update()



