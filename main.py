import pygame
import time
import math

grass = pygame.image.load("imgs/grass.png")
track = pygame.image.load("imgs/track.png")
track_border = pygame.image.load("imgs/track-border.png")
finish = pygame.image.load("imgs/finish.png")
red_car = pygame.image.load("imgs/red-car.png")
green_car = pygame.image.load("imgs/green-car.png")

width, height = track.get_width(), track.get_height()
win = pygame.display.set_mode(width,height)
win.set_caption("Racing Game!!")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False