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
		
		snake.head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
		snake.head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()
		snake.head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()
		snake.head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()
		
		snake.tail_up = pygame.image.load('Graphics/tail_up.png').convert_alpha()
		snake.tail_down = pygame.image.load('Graphics/tail_down.png').convert_alpha()
		snake.tail_right = pygame.image.load('Graphics/tail_right.png').convert_alpha()
		snake.tail_left = pygame.image.load('Graphics/tail_left.png').convert_alpha()

		snake.body_vertical = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
		snake.body_horizontal = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()

		snake.body_tr = pygame.image.load('Graphics/body_tr.png').convert_alpha()
		snake.body_tl = pygame.image.load('Graphics/body_tl.png').convert_alpha()
		snake.body_br = pygame.image.load('Graphics/body_br.png').convert_alpha()
		snake.body_bl = pygame.image.load('Graphics/body_bl.png').convert_alpha()


	def draw_snake(snake):
		snake.update_head_graphics()
		snake.update_tail_graphics()

		for index,block in enumerate(snake.body):
			x_pos = int(block.x * cell_size)
			y_pos = int(block.y * cell_size)
			block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
			
			if index == 0:
				screen.blit(snake.head,block_rect)
			elif index == len(snake.body) - 1:
				screen.blit(snake.tail,block_rect)
			else:
				previous_block = snake.body[index + 1] - block
				next_block = snake.body[index - 1] - block
				if previous_block.x == next_block.x:
					screen.blit(snake.body_vertical,block_rect)
				elif previous_block.y == next_block.y:
					screen.blit(snake.body_horizontal,block_rect)
				else:
					if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
						screen.blit(snake.body_tl,block_rect)
					elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
						screen.blit(snake.body_bl,block_rect)
					elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
						screen.blit(snake.body_tr,block_rect)
					elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
						screen.blit(snake.body_br,block_rect)

	def update_head_graphics(snake):
		head_relation = snake.body[1] - snake.body[0]
		if head_relation == Vector2(1,0): snake.head = snake.head_left
		elif head_relation == Vector2(-1,0): snake.head = snake.head_right
		elif head_relation == Vector2(0,1): snake.head = snake.head_up
		elif head_relation == Vector2(0,-1): snake.head = snake.head_down

	def update_tail_graphics(snake):
		tail_relation = snake.body[-2] - snake.body[-1]
		if tail_relation == Vector2(1,0): snake.tail = snake.tail_left
		elif tail_relation == Vector2(-1,0): snake.tail = snake.tail_right
		elif tail_relation == Vector2(0,1): snake.tail = snake.tail_up
		elif tail_relation == Vector2(0,-1): snake.tail = snake.tail_down
			
			
	
	

class MAIN:
	def __init__(snake):
		snake.snake = SNAKE()
		snake.fruit = FRUIT()


	def draw_elements(snake):
		snake.fruit.draw_fruit()
		snake.snake.draw_snake()

	def draw_elements(snake):
		snake.fruit.draw_fruit()
		snake.snake.draw_snake()
		snake.draw_score()

	

	def draw_score(snake):
		score_text = str(len(snake.snake.body) - 3)
		score_surface = game_font.render(score_text,True,(56,74,12))
		score_x = int(cell_size * cell_number - 60)
		score_y = int(cell_size * cell_number - 40)
		score_rect = score_surface.get_rect(center = (score_x,score_y))
		apple_rect = apple.get_rect(midright = (score_rect.left,score_rect.centery))
		bg_rect = pygame.Rect(apple_rect.left,apple_rect.top,apple_rect.width + score_rect.width + 6,apple_rect.height)

		pygame.draw.rect(screen,(167,209,61),bg_rect)
		screen.blit(score_surface,score_rect)
		screen.blit(apple,apple_rect)
		pygame.draw.rect(screen,(56,74,12),bg_rect,2)



pygame.init()
cell_size=40
cell_number=20

screen= pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))
clock =pygame.time.Clock()
apple= pygame.image.load('Graphics/apple.png').convert_alpha()
game_font = pygame.font.Font('Font/font.ttf',25)

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
