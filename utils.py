import pygame

def blit_alpha(target, source, location, opacity):
	temp = pygame.Surface((source.get_width(), source.get_height())).convert()
	temp.blit(target, (-location[0], -location[1]))
	temp.blit(source, (0, 0))
	temp.set_alpha(opacity)        
	target.blit(temp, location)

def get_offset_of_all_units(chararacters, current_character):
	offsets = []
	for char in chararacters:
		offsets.append([char.x - current_character.x, char.y - current_character.y])
	return offsets

def Pause(pause, PhaseFocus, PauseScreen, screen, isPaused):
	pause = isPaused
	while pause:
		PhaseFocus = 1
		screen.blit(PauseScreen, (100, 100))
		print("paused")

	while not pause:
		PhaseFocus = 0
		print("unpaused")

	pygame.display.update()
