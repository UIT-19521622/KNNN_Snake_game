import imp
from random import random
from turtle import Screen, width


import pygame, sys, random

from pygame.math import Vector2

class FRUIT:
    def __init__(self) :
        self.x=random.randint(0,cell_number-1)
        self.y=random.randint(0,cell_number-1)
        self.pos=Vector2(self.x,self.y)

    def draw_fruit(self):
        fruit_rect=pygame.Rect(int(self.pos.x*cell_size),int(self.pos.y*cell_size),cell_size,cell_size)
        screen.blit(apple,fruit_rect)

  



pygame.init()
cell_size=40
cell_number=20

screen= pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))
clock =pygame.time.Clock()
apple= pygame.image.load('Graphics/apple.png').convert_alpha()


fruit= FRUIT()


while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(
            )
            sys.exit()
    screen.fill((100,215,70))
    fruit.draw_fruit()
    pygame.display.update()
    clock.tick(60)
