import pygame
from utils
pressed = pygame.key.get_pressed() #If something is pressed...
if IDO.get_key(pygame.K_RIGHT): #If the right arrow key is pressed down...
	if PhaseFocus == 0 or PhaseFocus == 2: #and If the current Phase is 0 or 2 
		Reticlex +=1 # Move the reticle to the right by 1 square value
		#Character.animation_dir = 
	if Currently_Selected != 0 and Currently_Selected.Phase == 2: #If you're already moving something...
		#Char_Animation()
		#Currently_Selected.animation_dir = RunRightAnimation
		if Currently_Selected.x != Reticlex: #And if the reticle's x position and character's x position isn't the same...
			Currently_Selected.x = Reticlex #Make it the same
		if Currently_Selected.x != Reticley: # And if the reticle's y position and the chatacter's y position isn't the same...
			Currently_Selected.y = Reticley #Make it the same

if IDO.get_key(pygame.K_LEFT): # if the left key is pressed...
	if PhaseFocus == 0 or PhaseFocus == 2:
		Reticlex -=1
	if Currently_Selected != 0 and Currently_Selected.Phase == 2:
		#Char_Animation()
		#Currently_Selected.animation_dir = RunLeftAnimation
		if Currently_Selected.x != Reticlex:
			Currently_Selected.x = Reticlex
		if Currently_Selected.x != Reticley:
			Currently_Selected.y = Reticley
	
if IDO.get_key(pygame.K_UP):
	if PhaseFocus == 0 or PhaseFocus == 2:
		Reticley -=1
	if Currently_Selected != 0 and Currently_Selected.Phase == 2:
		if Currently_Selected.x != Reticlex:
			Currently_Selected.x = Reticlex
		if Currently_Selected.x != Reticley:
			Currently_Selected.y = Reticley
	if PhaseFocus == 1 and Currently_Focused_Menu != 0:
		Currently_Focused_Menu.move_cursor_up()
	
if IDO.get_key(pygame.K_DOWN):
	if PhaseFocus == 0 or PhaseFocus == 2:
		Reticley +=1
	if Currently_Selected != 0 and Currently_Selected.Phase == 2:
		#Char_Animation()
		#Currently_Selected.animation_dir = RunDownAnimation
		if Currently_Selected.x != Reticlex:
			Currently_Selected.x = Reticlex
		if Currently_Selected.x != Reticley:
			Currently_Selected.y = Reticley
	if PhaseFocus == 1 and Currently_Focused_Menu != 0 and Currently_Focused_Menu != None:
		Currently_Focused_Menu.move_cursor_down()
		
	
if IBO.get_key(pygame.K_z):
	for c in chars:
		if Reticlex == c.x and Reticley == c.y and c.Phase == 1 and c.team == "Ally" and Currently_Selected == 0 and c.Activity == c.Maxact:
			Currently_Selected = c
			Currently_Selected.StoredPositionx = Currently_Selected.x
			Currently_Selected.StoredPositiony = Currently_Selected.y
			c.StoredActivity = c.Activity
			c.Phase = 2

		if PhaseFocus == 1 and c.Phase == 3:
			ret = Currently_Focused_Menu.select(c)
			if ret != -1 and not isinstance(ret, Weapon) and not isinstance(ret, Item) and not isinstance(ret, AOEItem) and not isinstance(ret, EndTurn):# and ret != -3:
				Currently_Focused_Menu = ret
			if isinstance(ret, Weapon) or isinstance(ret, Item) or isinstance(ret, AOEItem):
				if isinstance(ret, Weapon):
					Currently_Selected.Weapon = ret
				if isinstance(ret, Item):
					ret.offset = utils.get_offset_of_all_units(chars, c)

				selectable_positions = get_positions_around_reticle((c.x, c.y), ret.offsets)
				c.Phase = 4
				selected_usable = ret
				PhaseFocus = 2
			if isinstance(ret, EndTurn):
				ret.use(Currently_Selected)
				PhaseFocus = 0
				Currently_Selected = 0
				Currently_Focused_Menu = Actions


		if c.Phase == 4:
			tile = (Reticlex, Reticley)
			if tile in selectable_positions:
				if isinstance(ret, AOEItem):
					# [PLANT USE ITEMS]
					newentity = selected_usable.use((Reticlex, Reticley))
					entities.append(newentity)
					Currently_Focused_Menu = Actions
					if Currently_Selected.Phase == 4:
						Currently_Selected.Phase = 1
						Currently_Selected = 0
					selected_usable = None
					selectable_positions = []
				else:
					# [SINGLE USE ITEMS]
					for char in chars:
						if char.x == Reticlex and char.y == Reticley:
							if isinstance(ret, Weapon) and char.team == "Enemy":
								if selected_usable.ActivityDrain <= Currently_Selected.Activity: 
									selected_usable.use(char, Currently_Selected)
							if isinstance(ret, Item) and char.team == "Ally":
								selected_usable.use(char)
							Currently_Focused_Menu = Actions
							if Currently_Selected.Phase == 4:
								Currently_Selected.Phase = 1
								Currently_Selected = 0
							selected_usable = None
							selectable_positions = []
			PhaseFocus = 0
			
if IBO.get_key(pygame.K_x) and not IBO.get_key(pygame.K_z):
	if Currently_Selected != 0:
		selectable_positions = []	
		if Currently_Selected.Phase == 3 and Currently_Focused_Menu == Actions:
			Currently_Selected.Phase = 1
			Currently_Selected.x = Currently_Selected.StoredPositionx
			Currently_Selected.y = Currently_Selected.StoredPositiony
			Currently_Selected = 0
			PhaseFocus = 0
			for c in chars:
				c.Activity = c.StoredActivity
		elif Currently_Selected.Phase == 4 or Currently_Selected.Phase == 2:
			PhaseFocus = 1
			Currently_Selected.Phase = 3
		else:
			Currently_Selected.Phase = 3

		
	if PhaseFocus == 1 and isinstance(Currently_Selected, Character) and Currently_Selected.Phase == 3:
		Currently_Focused_Menu = Currently_Focused_Menu.above
		if Currently_Focused_Menu == None:
			Currently_Focused_Menu = Actions

if  IBO.get_key(pygame.K_ESCAPE):
	pygame.mixer.Sound.play(QuitSound)
	pygame.mixer.Sound.set_volume(Volume)
	pygame.mixer.music.stop()
	screen.blit(SaveText, (200,200))
	pygame.display.flip()
	pygame.time.wait(420)
	for i in range(10, 210, 10):
		blit_alpha(screen, bLaCksCrEEn, (0,0), i)
		pygame.display.flip()
		pygame.time.wait(20)
	exit()

if IBO.get_key(pygame.K_a):
	Pause(Paused, PhaseFocus, Pause_Screen, screen, True)

if IBO.get_key(pygame.K_s):
	Pause(Paused, PhaseFocus, Pause_Screen, screen, False)