import pygame
import time
import math
from utils import scale_image


def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)


GRASS = scale_image(pygame.image.load("imgs/grass.jng"), 2.5)
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
        self.angle = 90
        self.x = self.START_POS
        self.y = self.START_POS
        self.acceleration = 0.1
    def rotate(self, left = False, right = False):
        if left:
            self.angle = self.angle + self.rotation_vel
        elif right:
            self.angle = self.angle - self.rotation_vel
    def draw(self, win):
        blit_rotate_center(win, self.img)

    def move_player(player_car):
        keys = pygame.key.get_pressed()
        moved = False

        if keys[pygame.K_a]:
            player_car.rotate(left=True)
        if keys[pygame.K_d]:
            player_car.rotate(right=True)
        if keys[pygame.K_w]:
            moved = True
            player_car.move_forward()
        if keys[pygame.K_s]:
            moved = True
            player_car.move_backward()

        if not moved:
            player_car.reduce_speed()

    def move_forward(self,win):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()

    def move_backward(self, win):
        self.vel = max(self.vel - self.acceleration, self.max_vel/2)
    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration/2, 0)
class PlayerCar(AbstractCar):
    IMG = RED_CAR
    START_POS = (180,200)

run = True
pygame.time.Clock()
images = [(GRASS, (0,0)), (TRACK, (0,0))]
player_car = PlayerCar(4,4)

def draw():
    for img, pos in images:
        WIN.blit(img, pos)
    player_car.draw()
    pygame.display.update()

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

