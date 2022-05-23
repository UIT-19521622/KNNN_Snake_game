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
class SNAKE:
	def __init__(snake):
		snake.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
		snake.direction = Vector2(0,0)
		snake.new_block = False


	def draw_snake(snake):

		for index,block in enumerate(snake.body):
			x_pos = int(block.x * cell_size)
			y_pos = int(block.y * cell_size)
			block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)

class MAIN:
	def __init__(snake):
		snake.snake = SNAKE()
		snake.fruit = FRUIT()


	def draw_elements(snake):
		snake.fruit.draw_fruit()
		snake.snake.draw_snake()





pygame.init()
cell_size=40
cell_number=20

screen= pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))
clock =pygame.time.Clock()
apple= pygame.image.load('Graphics/apple.png').convert_alpha()


main = MAIN()


while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(
            )
            sys.exit()
    screen.fill((100,215,70))
    main.draw_elements()
    pygame.display.update()
    clock.tick(60)
