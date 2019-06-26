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
