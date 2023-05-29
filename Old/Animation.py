import pygame

class Animation:

	index = 0
	ticksuntilnext = 0
	tick = 0
	anim = []
		
	def __init__(filename, frames):
	
		for i in range(1, frames+1):
			self.anim.append(pygame.image.load(filename+str(i)+ ".png"))
			
			
	def render (screen,x ,y):
		if tick > ticksuntilnext:
	
			tick = 0
			index += 1
			if index > len(self.anim) - 1:
				index = 0
				
		tick += 1
		screen.blit(anim[index], (300, 300))