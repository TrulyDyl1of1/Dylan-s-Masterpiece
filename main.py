import pygame
import time
import math
from utils import scale_image


def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)


GRASS = scale_image(pygame.image.load("imgs/grass.png"), 2.5)
TRACK = scale_image(pygame.image.load("imgs/track.png"), 0.9)
TRACK_BORDER = scale_image(pygame.image.load("imgs/track-border.png"), 0.9)
FINISH = pygame.image.load("imgs/finish.png")
RED_CAR = scale_image(pygame.image.load("imgs/red-car.png"), 0.55)
GREEN_CAR = scale_image(pygame.image.load("imgs/green-car.png"), 0.55)

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode(WIDTH,HEIGHT)
pygame.display.set_caption("Racing Game!!")

FPS = 60
class AbstractCar:
    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = self.START_POS
        self.acceleration = 0.1

run = True
pygame.time.Clock()
images = [(GRASS, (0,0)), (TRACK, (0,0))]

def draw():
    for img, pos in images:
        WIN.blit(img, pos)

while run:
    time.clock.tick(FPS)
    draw(WIN, images)
    WIN.blit(GRASS, (0,0))
    WIN.blit(TRACK, (0,0))
    WIN.blit(RED_CAR, (0,0))

    pygame.display.update()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

pygame.quit()

