
import pygame
import random

# all of the importing from different files
from math import sin, cos
from resources import *
from usables import *
from utils import *
from Map import *
from Menu import *
from InputManager import *
from Animation import *
from WavyText import *
from Character import *

pygame.init() # Initialising pygame so that we can use its functions
pygame.font.init() # initialising pygame fonts so that we can use fonts in pygame
pygame.joystick.init() # initialising pygame joystick so that we can use controllers in pygame
Currently_Selected = 0 # Defining Currrently_Selected. Has different uses in this program. For now, it shows if we have selected a character or not. 0 Not selected, 1 is selected.
pygame.key.set_repeat(2000, 9) # Uses a function from a previous file. This allows us to hold any button down but delay it enough that the player would fly through menus and the such. 
Reticlex = 3 # initial Reticle X-coordinate position. It speaks for itself really
Reticley = 3 # intial reticle  Y-coordinate position. it speaks for itself really
PhaseFocus = 0 # 0 for world movement, 1 for menu movement
CursorPoint = 0 # Initial position for the menu cursor for when navigating menus.
selectable_positions = [] # Makes an empty list. Later on, we can add coordinates to show where items can be used.
selected_Weapon = None # initialises a character's current weapon. Currently set as nothing.
GREEN = 0,255,0 # Green color definition. later used for our time gauge

pygame.display.set_caption("The World's Most Excellent Game") # changes the name of the game at the top of the screen

screen = pygame.display.set_mode((960,540)) # Defines screen resolution
clock = pygame.time.Clock() # Defines that clock is the framerate the game will be running at (pygame.time.Clock()).
prev_time = pygame.time.get_ticks()
quit = False # Shows that when the game boots up, it shouldn't quit ASAP

#---------------------------------------------------------------------------DRAWING AREA---------------------------------------------------------------------------------------

# Draw Collisions
def isPassable(x,y): #Definition for if something is able to be passed through that tile
	if Currently_Selected !=0: #If a character is already selected...
		for tile in map: #Looks at every single defined tile on the "map" named list
			if tile.x == x and tile.y == y: # If the tile positions are the same as isPassable positions(?)
				return tile.Passable # Then just post that this tile is passable

def DrawReticle(): # Definition for placing the reticle
	Px = 0 + Reticlex*50 #Shows that reticle's X-Coordinate will be its current value times 50
	Py = 20 + Reticley*50 #Shows that reticle's Y-Coordinate will be its current value times 50
	screen.blit(Reticle,(Px,Py)) #Posts reticle on screen with Px and Py with it being its coordinates




#def select_current_item(self): #Call this method when Z is pressed

# This is a list of weapon and item descriptions. The descriptions require name, icon, menu category, damage, critical hit chance, special ability, defense, offsets, and the drain of the activity bar used by the weapon respectively
# Weapon Descriptions
Scrimitar = Menu("Scrimitar","A",[Weapon("Scrimitar", 37,0.3,"",5, 1, [[0, 1], [0, -1], [-1, 0], [1, 0],[1, 1],[1, -1],[-1, 1],[-1, -1]])])
Thunder_Scroll = Menu("Thunder Scroll","U",[AOEItem("Thunder Scroll", [[0, 0]], [[-1, -3], [1, -3], [0, -2], [-1, -1], [1,-1], [0, 0], [-1, 1], [1, 1], [0, 2], [-1, 3], [1, 3]])])
Fire_Scroll = Menu("Fire Scroll","U",[Weapon("Fire Scroll",10,0.1,"After-Effect",0, 1, [[1, 0], [2, 0], [0, 1], [0, 2], [0, -1], [0, -2]])])
Dual_Masamune = Menu("Dual Masamune","N",[Weapon("Dual Masamune", 70,0.7,"",10, 1, [[1, 1], [-1, 1], [1, -1], [-1,-1]])])
Nevan = Menu("Nevan","y",[Weapon("Nevan", 70,0.3,"",40, 1, [[1, 0], [-1, 0], [-2, 1], [2, 1], [-2, -1], [2, -1], [0, 1], [0, -1]])])
Binding_Blade = Menu("Binding Blade","A",[Weapon("Binding Blade", 100,0.9,"",100, 1, [[-1, 0],[ 1, 0],[ 0, 1],[ 0,-1],[-2, 0],[ 2, 0],[ 0,-2],[ 0, 2],[-1, 1],[-1,-1],[ 1,-1],[ 1, 1]])])
potion = Menu("potion","E",[Item("Potion")])
Hi_potion = Menu("Hi-potion","E",[Item("Hi-potion")])
Level_Up_Point = Menu ("Level Up Point","E",[Item("Level Up Point")])
# Angelic_Robe = Menu("Angelic Robe","E",[Item("Angelic Robe")])
#Item Descriptions
smoke_screen = Menu("Smoke screen","i",[AOEItem("Smoke screen", [[0, 0]], [[0, 0], [-1, 0],[ 1, 0],[ 0, 1],[ 0,-1],[-2, 0],[ 2, 0],[ 0,-2],[ 0, 2],[-1, 1],[-1,-1],[ 1,-1],[ 1, 1]])])
Foutain_of_Youth = Menu("Foutain of youth","S",[AOEItem("Fountain of youth", [[0, 0]], [[0, 0], [-1, 0],[ 1, 0],[ 0, 1],[ 0,-1],[-2, 0],[ 2, 0],[ 0,-2],[ 0, 2],[-1, 1],[-1,-1],[ 1,-1],[ 1, 1]])])
Remedies = Menu("Items","E",[potion, Hi_potion, Level_Up_Point, smoke_screen, Foutain_of_Youth])
Attack = Menu("Arsenal","A",[ Scrimitar, Thunder_Scroll, Fire_Scroll, Dual_Masamune, Binding_Blade, Nevan])
End_Turn = Menu("End Turn","f",[EndTurn()])
Actions = Menu("Actions","A",[Attack,Remedies, End_Turn])
Fists = Weapon("Fists", 37,0.3,"",5)
Currently_Focused_Menu = Actions
Remedies.above = Actions
Attack.above = Actions
End_Turn.above = End_Turn


def get_positions_around_reticle(reticle, offsets):
		return [(reticle[0] + offset[0], reticle[1] + offset[1]) for offset in offsets]



map = [] # A list for what tiles will appear on the map
#Make Characters
chars = [
	Character("Marth",Fists,char1Idle,"Ally",4,4,15,100, 'Main_Char_1'),
	Character("Roy",Fists,char3Idle1,"Ally",4,2,10,100, 'Side_Char_3'),
	Character("Thanos",Fists,char4Idle1,"Ally",3,2,10,100, 'Side_Char_4'),
	Character("John Wick",Fists,char2Idle1,"Enemy",5,5,10,100, 'Side_Char_2'),
	Character("Chug Scar",Fists,char2Idle1,"Enemy",2,8,10,100, 'Side_Char_2'),
	Character("Snoop Dogg",Fists,char2Idle1,"Enemy",5,7,10,100, 'Side_Char_2'),
	Character("E",Fists,char2Idle1,"Enemy",7,2,10,100, 'Side_Char_2'),
	Character("Fortknight",Fists,char2Idle1,"Enemy",4,3,10,100, 'Side_Char_2')
]
entities = [] # ??????????????????????????????????????????

# Here, we define what levels will look like. We use the pre-described numbers in the Map file to "map out (no pun intended) a level."
# Guide: Different numbers cause different tiles to appear, slashes(\n) goes to the next row. An dit's simple as that
# For example, level 1 will look like this if we move everything into place:
#     111111111111111
# (\n)100000000033331
# (\n)133330000000001
# (\n)133330000033331
# (\n)133330000033331
# (\n)133330000033331
# (\n)133334444433331
# (\n)144444000444441
# (\n)100333333333001
# (\n)111111111111111\n
level_1 = Map("111111111111111\n100000000033331\n133330000000001\n133330000033331\n133330000033331\n133330000033331\n133334444433331\n144444000444441\n100333333333001\n111111111111111\n")


#CONTROLLER SETUP
joysticks = [] # Opens up a new list for the number of joysticks currently connected to the computer
for i in range(pygame.joystick.get_count()): # For every controller connected...
	joysticks = (pygame.joystick.Joystick(i)) # the term joysticks will mean every single joysrick connected
	joysticks.init() # initialise joysticsk so that multiple joysticks could be used

#MAIN LOOP		
while not quit: # you are either a 2 year old with an IQ of 8 or a game journalist if you don't understand what this says, seriously.

	if isPassable(Reticlex,Reticley) == False: # If the reticle positions aren't passable...
		Reticlex = 5 # Put them at x-coordiante 5
		Reticley = 5 # Put them at y-coordiante 5
		
# STAGE 1: CHECK IF QUIT	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit = True
	
	# If anything talks about qiutting the game, quit it.

# STAGE 2: CHECK IF KEYS PRESSED
			
	#If no character selected, currently selected = 0
	
	#Keys For Player Movement
	pressed = pygame.key.get_pressed() #If something is pressed...
	if IDO.get_key(pygame.K_RIGHT): #If the right arrow key is pressed down...
		if PhaseFocus == 0 or PhaseFocus == 2: #and If the current Phase is 0 or 2 
			Reticlex +=1 # Move the reticle to the right by 1 square value
		if Currently_Selected != 0 and Currently_Selected.Phase == 2:
			if Currently_Selected.x != Reticlex:
				Currently_Selected.x = Reticlex
			if Currently_Selected.x != Reticley:
				Currently_Selected.y = Reticley

	if IDO.get_key(pygame.K_LEFT):
		if PhaseFocus == 0 or PhaseFocus == 2:
			Reticlex -=1
		if Currently_Selected != 0 and Currently_Selected.Phase == 2:
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
			if Currently_Selected.x != Reticlex:
				Currently_Selected.x = Reticlex
			if Currently_Selected.x != Reticley:
				Currently_Selected.y = Reticley
		if PhaseFocus == 1 and Currently_Focused_Menu != 0 and Currently_Focused_Menu != None:
			Currently_Focused_Menu.move_cursor_down()
			
		
	if IBO.get_key(pygame.K_z):
		for c in chars:
			if Reticlex == c.x and Reticley == c.y and c.Phase == 1 and c.team == "Ally" and c.Phase!= 2 and Currently_Selected == 0 and c.Activity == c.Maxact:
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
							if char.team == "Enemy" and char.x == Reticlex and char.y == Reticley:
								print(selected_usable.__dict__)
								selected_usable.use(char, Currently_Selected)
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
				Currently_Selected.Activity = Currently_Selected.StoredActivity
				Currently_Selected = 0
				PhaseFocus = 0
			elif Currently_Selected.Phase == 4 or  Currently_Selected.Phase == 2:
				PhaseFocus = 1
				Currently_Selected.Phase = 3
			else:
				Currently_Selected.Phase = 3

			
		if PhaseFocus == 1 and isinstance(Currently_Selected, Character) and Currently_Selected.Phase == 3:
			Currently_Focused_Menu = Currently_Focused_Menu.above
			if Currently_Focused_Menu == None:
				Currently_Focused_Menu = Actions

	if pressed[pygame.K_ESCAPE]:
		screen.blit(SaveText, (200,200))
		pygame.display.flip()
		pygame.time.wait(420)
		for i in range(10, 210, 10):
			blit_alpha(screen, bLaCksCrEEn, (0,0), i)
			pygame.display.flip()
			pygame.time.wait(20)
		exit()

	# [NEW]
	for c in chars:
		# UNTESTED GREAT STUFF
		if c.Phase == 2:
			d = abs(Currently_Selected.StoredPositionx - Currently_Selected.x) + abs(Currently_Selected.StoredPositiony - Currently_Selected.y)
			move_energy = d * 10
			if c.Activity - move_energy < 0:
				c.Activity = 0
				Currently_Selected.Phase = 1
				PhaseFocus = 0
				Currently_Selected = 0
				Currently_Focused_Menu = Actions


		#Controls For Controller
	# axes = joystick.get_numaxes()
	# 	for i in range( axes ):
	# 	 	axis = joystick.get_axis( i )
	# 		if axis >= 1:
	# 			if PhaseFocus == 0 or PhaseFocus == 2:
	# 				Reticley -=1
	# 			if Currently_Selected != 0 and Currently_Selected.Phase == 2:
	# 				Currently_Selected.y =Reticley
	# 			if PhaseFocus == 1 and Currently_Focused_Menu != 0:
	# 				Currently_Focused_Menu.move_cursor_up()
	# 		if axis <= -1:
	# 			if PhaseFocus == 0 or PhaseFocus == 2:
	# 				Reticley +=1
	# 			if Currently_Selected != 0 and Currently_Selected.Phase == 2:
	# 				Currently_Selected.y =Reticley
	# 			if PhaseFocus == 1 and Currently_Focused_Menu != 0 and Currently_Focused_Menu != None:
	# 				Currently_Focused_Menu.move_cursor_down()

	if event.type == pygame.JOYBUTTONDOWN:
		if event.button == 0:
			for c in chars:
				if Reticlex == c.x and Reticley == c.y and c.Phase == 1 and c.team == "Ally" and c.Phase!= 2 and Currently_Selected == 0 and c.Activity == c.Maxact:
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
								if char.team == "Enemy" and char.x == Reticlex and char.y == Reticley:
									selected_usable.use(char)
									Currently_Focused_Menu = Actions
									if Currently_Selected.Phase == 4:
										Currently_Selected.Phase = 1
										Currently_Selected = 0
									selected_usable = None
									selectable_positions = []
					PhaseFocus = 0
		if event.button == 2:
			if Currently_Selected != 0:
				selectable_positions = []	
				if Currently_Selected.Phase == 3 and Currently_Focused_Menu == Actions:
					Currently_Selected.Phase = 1
					Currently_Selected.x = Currently_Selected.StoredPositionx
					Currently_Selected.y = Currently_Selected.StoredPositiony
					c.Activity = c.StoredActivity
					Currently_Selected = 0
					PhaseFocus = 0
				elif Currently_Selected.Phase == 4 or  Currently_Selected.Phase == 2:
					PhaseFocus = 1
					Currently_Selected.Phase = 3
				else:
					Currently_Selected.Phase = 3
			
			if PhaseFocus == 1 and isinstance(Currently_Selected, Character) and Currently_Selected.Phase == 3:
				Currently_Focused_Menu = Currently_Focused_Menu.above
				if Currently_Focused_Menu == None:
					Currently_Focused_Menu = Actions


# STAGE 3: MAKE COLLISION DETECTION
	if Currently_Selected != 0 and Reticlex >= 14 and Currently_Selected.x >= 14:
		Reticlex = 14
		Currently_Selected.x = Reticlex
	if Currently_Selected !=0 and Reticlex >= 14 and Currently_Selected.x >= 14 :
		Reticlex = 14
		Currently_Selected.x = Reticlex
	if  Reticley >= 9:
		Reticley = 9
	if  Reticlex >= 14:
		Reticlex = 14
	if Reticlex <= 0:
		Reticlex = 0
	if Reticley <= 0:
		Reticley = 0

#STAGE 4: MAKE MOVEMENT TIMER
	if Currently_Selected != 0 and Currently_Selected.Phase == 2:
		Currently_Selected.Activity -= 0.8
		if Currently_Selected.Activity <= 0:
			Currently_Selected.Activity = 0
	for c in chars:
		if c.Activity == 0:
			Currently_Selected != 0
			if Currently_Selected != 0:
				Currently_Selected.Phase = 3
				PhaseFocus = 1
				pos = (Currently_Selected.x, Currently_Selected.y)
				others = chars[:]
				others.remove(Currently_Selected)
			
				if pos in [(c.x, c.y) for c in others]:
					Currently_Selected.x = Currently_Selected.StoredPositionx
					Currently_Selected.y = Currently_Selected.StoredPositiony
					Currently_Selected.Activity = Currently_Selected.StoredActivity
					Reticlex = Currently_Selected.x
					Reticley = Currently_Selected.y
	
	if pygame.time.get_ticks() - prev_time > 2000:
		prev_time = pygame.time.get_ticks()
		for entity in entities:
				entity.update(chars)


# STAGE 5: DISPLAY OBJECTS
	screen.fill((0,0,0))

	level_1.render(screen)

	for entity in entities:
		entity.render(screen)
		if isinstance(entity, AOEItem):
			entity.renderAOE(screen)

	for character in chars:
		character.render(screen)


	DrawReticle()
	for pos in selectable_positions:
		Px = 0 + pos[0]*50
		Py = 20 + pos[1]*50
		blit_alpha(screen,Selectable_Reticle,(Px,Py),128)

#STAGE 6: Gameplay menu and help text
	if Currently_Focused_Menu != -1 and Currently_Selected != 0 and Currently_Selected.Phase == 3 and Currently_Focused_Menu != None:
		Currently_Focused_Menu.blit(screen)
		
	CommandStatusText = Menufont.render("Commands (TAB): ",False,(0,0,0))
	screen.blit(CommandStatusText,(50,10))
	
	MapStatusText = Menufont.render("Map(SHIFT): ",False,(0,0,0))
	screen.blit(MapStatusText,(300,10))
	
# Help Prompts

	# General Help Prompts
	HelpGoalText = Menufont.render("Defeat All Of The Enemies",False,(0,0,0))
	HelpItemsText = Menufont.render("Use An Item",False,(0,0,0))
	HelpAttackText = Menufont.render("Choose A Weapon To Attack A Nerby Foe",False,(0,0,0))
	HelpEnd_TurnText = Menufont.render("End The Actions Of The Current Character",False,(0,0,0))
	# Weapon Help Prompts
	HelpScrimitarText = Menufont.render("A Curved Weapon With Low Defense, But A Higher Critical Chance",False,(0,0,0))
	HelpBinding_BladeText = Menufont.render("The Ultimate Weapon, Unprecedented Attack And Defense Lies Within... ",False,(0,0,0))
	HelpScrimitarText = Menufont.render("A Curved Weapon With Low Defense, But A Higher Critical Chance",False,(0,0,0))
	HelpThunder_ScrollText = Menufont.render("An Overworld Attack That Stikes Down Lightning Periodically. Causes a stun effect.",False,(0,0,0))
	HelpFire_ScrollText = Menufont.render("An Overworld Attack That Spreads Around Until It Dies. Causes The Victims To Burn.",False,(0,0,0))
	HelpDual_MasamuneText = Menufont.render("An Extremenly Delicate Blade That Cuts Through Enemies Like Butter, But Has A Very Short Range.",False,(0,0,0))
	HelpNevanText = Menufont.render("An Electro Guitar That Can Send Lighting Shivers Down Enemy Spines.Has To Be Used Repeatedly To Do More Damage.",False,(0,0,0))
	# Item Help Prompts
	HelpPotionText = Menufont.render("Grants 10 HP to the selected character " +Character.Name+ " (" + str(Character.HP) + ") -> (" + str(Character.HP + 10) + ")",False,(0,0,0))
	HelpHi_PotionText = Menufont.render("Grants 30 HP to the selected character " +Character.Name+ " (" + str(Character.HP) + ") -> (" + str(Character.HP + 30) + ")",False,(0,0,0))
	HelpTextDictator =  HelpGoalText

	for c in chars:
		if c.Phase == 1 and c.Phase != 3:
			c.Activity += 0.2
			if c.Activity > c.Maxact:
				c.Activity = c.Maxact

	if Currently_Focused_Menu != None and isinstance(Currently_Focused_Menu, Menu) and Currently_Focused_Menu.items != None:
		Damien = Currently_Focused_Menu.items[Currently_Focused_Menu.CursorPoint]
		if Currently_Selected != 0 and Currently_Selected.Phase == 1:
			HelpTextDictator = HelpGoalText
			


		#Descriptions For Remedies:
		if Currently_Selected != 0 and Currently_Selected.Phase == 3 and Damien == Remedies:
			HelpTextDictator = HelpItemsText

		#Descriptions For Attack:
		if Currently_Selected != 0 and Currently_Selected.Phase == 3 and Damien == Attack:
			HelpTextDictator = HelpAttackText

		#Descriptions For End Turn:
		if Currently_Selected != 0 and Currently_Selected.Phase == 3 and Damien == End_Turn:
			HelpTextDictator = HelpEnd_TurnText

		# Descriptions For Scrimitar:
		if Currently_Selected != 0 and Currently_Selected.Phase == 3 and Damien == Scrimitar:
			HelpTextDictator = HelpScrimitarText

		#Descriptions For Thunder Scroll:
		if Currently_Selected != 0 and Currently_Selected.Phase == 3 and Damien == Thunder_Scroll:
			HelpTextDictator = HelpThunder_ScrollText


		#Descriptions For Binding Blade:	
		if Currently_Selected != 0 and Currently_Selected.Phase == 3 and Damien == Binding_Blade:
			HelpTextDictator = HelpBinding_BladeText

		#Descriptions For Fire Scroll:
		if Currently_Selected != 0 and Currently_Selected.Phase == 3 and Damien == Fire_Scroll:
			HelpTextDictator = HelpFire_ScrollText

		if Currently_Selected != 0 and Currently_Selected.Phase == 3 and Damien == Dual_Masamune:
			HelpTextDictator = HelpDual_MasamuneText

		#Descriptions For Nevan:
		if Currently_Selected != 0 and Currently_Selected.Phase == 3 and Damien == Nevan:
			HelpTextDictator = HelpNevanText

		#Descriptions For Potion:
		if Currently_Selected != 0 and Currently_Selected.Phase == 3 and Damien == potion:
			HelpTextDictator = HelpPotionText

		#Descriptions For Hi-Potion:
		if Currently_Selected != 0 and Currently_Selected.Phase == 3 and Damien == Hi_potion:
			HelpTextDictator = HelpHi_PotionText

		
	screen.blit(HelpTextDictator,(50,520))

# The Commands List
	screen.blit(CommandList,(750,30))
	
# The Minimap 
	screen.blit(Minimap,(750,370))

	# the thing on the right
	for i, char in enumerate(chars):
		if char.team == "Ally":
			text = "               " +char.Name +"        HP:  " + str(char.HP)
			screen.blit(char.Character_Tile, (760, 100 + i*40))
			screen.blit(Actvivtygaugesprite, (850, 120 + i*40))
			pygame.draw.rect(screen, GREEN, (850, 120 + i*40, char.Activity, 15))

			Character_Desctiptions = Menufont.render(text,False,(255,255,255))
			screen.blit(Character_Desctiptions,(760,100 + i*40))
	

#Player Weapon Descriptions:
	if isinstance(Currently_Selected, Character) and Currently_Selected.Phase == 4 and Currently_Selected != 0:
		if Currently_Focused_Menu not in [None, -1]:
			texttorenderto = [
				Currently_Selected.Weapon.name,
				"Str.:" + str(Currently_Selected.Weapon.Strength),
				"Crit.: " + str(Currently_Selected.Weapon.Crit),
				"Sp. Ability: ",
				Currently_Selected.Weapon.Sp_Ability,
				"Def.: " + str(Currently_Selected.Weapon.Defense)
			] 
			blit_alpha(screen, Currently_Focused_Menu.background_image, (Currently_Focused_Menu.x, 20), 128) # FIX
			for i in range(len(texttorenderto)):
				Weapon_Desctiptions = Menufont.render(texttorenderto[i],False,(255,255,255))
				screen.blit(Weapon_Desctiptions,(70,40 + i*50))

#  Enemy Weapon Descriptions:
	for char in chars:
		if char.team == "Enemy" and  isinstance(Currently_Selected, Character) and Currently_Selected.Phase == 4 and Currently_Selected != 0:
			if char.x == Reticlex and char.y == Reticley and Currently_Focused_Menu not in [None, -1]:
				enmtexttorenderto = [
					char.Weapon.name,
					"Str.:" + str(char.Weapon.Strength),
					"Crit.: " + str(char.Weapon.Crit),
					"Sp. Ability: " + char.Weapon.Sp_Ability,
					"Def.: " + str(char.Weapon.Defense)
				] 
				for i in range(len(enmtexttorenderto)):
					ENMWeapon_Desctiptions = Menufont.render(enmtexttorenderto[i],False,(255,255,255))
					screen.blit(ENMWeapon_Desctiptions,(170,40 + i*50))

	for char in chars:
		if char.Phase == 1 and Reticlex == char.x and Reticley == char.y:
			Characterbubblename = Menufont.render(char.Name,False,(255,255,255))
			CharacterBubblehealth = Menufont.render(str(char.HP),False,(255,255,255))
			screen.blit(Satus_Bubble,(char.x, char.y + 20))
			screen.blit(Characterbubblename,(char.x, char.y + 20))
			screen.blit(CharacterBubblehealth,(char.x + 70, char.y + 20))
		
# STAGE 9: A delay to stop it from going too fast and flip image buffer
	clock.tick(60)
	#flip the image buffer
	pygame.display.flip()

pygame.quit()
