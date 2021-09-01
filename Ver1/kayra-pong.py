#!/usr/bin/python
import pygame
pygame.init()

screen = pygame.display.set_mode((1000, 600))

quit = False
MyY=250
BallX=500
BallY=300
BallS=4
PadS=7
clock = pygame.time.Clock()

while not quit:

# STAGE 1: CHECK IF QUIT	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit = True
			
# STAGE 2: CHECK IF KEYS PRESSED
	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_UP]:
		if MyY > 0:
			MyY-=PadS
	if pressed[pygame.K_DOWN]:
		if MyY < 500:
			MyY+=PadS
	screen.fill((0,0,0))
	
# STAGE 3: CALCULATE GAME PHYSICS
	BallX-=BallS
	BallY+=0

	if BallX > 5 and BallX < 125 and BallY > MyY:
		BallS=-BallS
# STAGE 4: DISPLAY OBJECTS
#red square
	pygame.draw.rect(screen, (255,0,0), pygame.Rect(75, MyY, 50, 100))
#blue square
	pygame.draw.rect(screen, (0,0,255), pygame.Rect(875, 250, 50, 100))
#Ball
	pygame.draw.rect(screen, (0,255,0), pygame.Rect(BallX,BallY,16,16))
	
	pygame.display.flip()	

# STAGE 5: A delay to stop it from going too fast	
	clock.tick(60)
