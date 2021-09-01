import pygame
import random

# all of the importing from different files
from resources import *
from LevelLayouts import *
from utils import *
from Menu import *
from InputManager import *
from Character import *
from ActionsMenu import *
from Collision_Detection import *
#try:
#	from Configuration import BGVolume, BattleSpeed, Resolution
#except:
BGVolume = 0
BattleSpeed = 1
Resolution = (960,540)

pygame.init() # Initialinng pygame so that we can use its functions
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
RED = 255,0,0 # Red color definition
BLUE = 3,144,252
GRAY = 105,105,105


#Config
Timer = 99 # Timer
isFullscreen = 0 #pygame.FULLSCREEN
Sound_Output = 2
pygame.display.set_caption("The World's Most Excellent Game") # changes the name of the game at the top of the screen

pygame.mixer.init(frequency=22050, size=-16, channels=Sound_Output, buffer=4096)
FullScreen = pygame.display.set_mode((Resolution), isFullscreen)
screen = pygame.Surface((960,540)) # Defines screen resolution
clock = pygame.time.Clock() # Defines that clock is the framerate the game will be running at (pygame.time.Clock()).
prev_time = pygame.time.get_ticks()
pygame.mixer.set_num_channels(8)
Paused = True
quit = False # Shows that when the game boots up, it shouldn't quit ASAP

#---------------------------------------------------------------------------DRAWING AREA---------------------------------------------------------------------------------------

#Game Intro

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

def get_positions_around_reticle(reticle, offsets):
		return [(reticle[0] + offset[0], reticle[1] + offset[1]) for offset in offsets]

map = [] # A list for what tiles will appear on the map
#Makes a list of characters that will appear on the map
#Example: Character(Name,Default Weapon,Idle Animation, Ally or Enemy, Starting X Position, Starting Y Position, Maximum HP, Maximum Stamina, Animation Directory Name)
chars = [
	Character("Ally1",Fists,AllyIdle1,"Ally",4,4,15,100, 1, 'Side_Char_3'),
	Character("Ally2",Fists,AllyIdle1,"Ally",4,2,10,100, 2, 'Side_Char_3'),
	Character("Ally3",Fists,AllyIdle1,"Ally",3,2,10,100, 0.5, 'Side_Char_3'),
	Character("Ally4",Fists,AllyIdle1,"Ally",7,5,10,100, 1.5, 'Side_Char_3'),
	Character("Ally5",Fists,AllyIdle1,"Ally",10,5,10,100, 3, 'Side_Char_3'),
	Character("Ally5",Fists,AllyIdle1,"Ally",15,7,10,100, 2.5, 'Side_Char_3'),
	Character("Enemy1",Fists,EnemyIdle1,"Enemy",5,5,10,100, 1.25, 'Side_Char_2'),
	Character("Enemy2",Fists,EnemyIdle1,"Enemy",2,8,10,100, 1.5, 'Side_Char_2'),
	Character("Enemy3",Fists,EnemyIdle1,"Enemy",5,7,10,100, 0.25, 'Side_Char_2'),
	Character("Enemy4",Fists,EnemyIdle1,"Enemy",7,2,10,100, 1.2, 'Side_Char_2'),
	Character("Enemy5",Fists,EnemyIdle1,"Enemy",4,3,10,100, 1.5, 'Side_Char_2')
]
entities = [] # ??????????????????????????????????????????

pygame.mixer.music.load("SFX/LevelBGMusic.mid") 
pygame.mixer.music.set_volume(BGVolume)
pygame.mixer.music.play(-1)

Playerscore = 00000

#MAIN LOOP		
while not quit:

	if isPassable(Reticlex,Reticley) == False: # If the reticle positions aren't passable...
		Reticlex = 5 # Put them at x-coordiante 5
		Reticley = 5 # Put them at y-coordiante 5

	pygame.transform.scale(screen, (Resolution), FullScreen)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit = True

	#If no character selected, currently selected = 0
	#Keys For Player Movement
	pressed = pygame.key.get_pressed() #If something is pressed...
	if IDO.get_key(pygame.K_RIGHT): #If the right arrow key is pressed down...
		if PhaseFocus == 0 or PhaseFocus == 2: #and If the current Phase is 0 or 2 
			Reticle_SetTarget = 1
			Reticlex += Reticle_SetTarget
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
			Reticle_SetTarget = -1
			Reticlex += Reticle_SetTarget
		if Currently_Selected != 0 and Currently_Selected.Phase == 2:
			#Char_Animation()
			#Currently_Selected.animation_dir = RunLeftAnimation
			if Currently_Selected.x != Reticlex:
				Currently_Selected.x = Reticlex
			if Currently_Selected.x != Reticley:
				Currently_Selected.y = Reticley
		
	if IDO.get_key(pygame.K_UP):
		if PhaseFocus == 0 or PhaseFocus == 2:
			Reticle_SetTarget = -1
			Reticley += Reticle_SetTarget
		if Currently_Selected != 0 and Currently_Selected.Phase == 2:
			if Currently_Selected.x != Reticlex:
				Currently_Selected.x = Reticlex
			if Currently_Selected.x != Reticley:
				Currently_Selected.y = Reticley
		if PhaseFocus == 1 and Currently_Focused_Menu != 0:
			Currently_Focused_Menu.move_cursor_up()
		
	if IDO.get_key(pygame.K_DOWN):
		if PhaseFocus == 0 or PhaseFocus == 2:
			Reticle_SetTarget = 1
			Reticley += Reticle_SetTarget
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
				pygame.mixer.Channel(1).set_volume(SFXVolume)
				pygame.mixer.Channel(1).play(pygame.mixer.Sound(Menu_SelectSFX))
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
						Playerscore += selected_usable.score
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
								if isinstance(ret, Weapon):
									if selected_usable.ActivityDrain <= Currently_Selected.Activity: 
										Playerscore += selected_usable.score
										selected_usable.use(char, Currently_Selected)
								if isinstance(ret, Item):
									Playerscore += selected_usable.score
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
				Reticlex = Currently_Selected.x
				Reticley = Currently_Selected.y
			else:
				Currently_Selected.Phase = 3

			
		if PhaseFocus == 1 and isinstance(Currently_Selected, Character) and Currently_Selected.Phase == 3:
			pygame.mixer.Channel(1).set_volume(SFXVolume)
			pygame.mixer.Channel(1).play(pygame.mixer.Sound(Menu_CancelSFX))
			Currently_Focused_Menu = Currently_Focused_Menu.above
			if Currently_Focused_Menu == None:
				Currently_Focused_Menu = Actions

	if  IBO.get_key(pygame.K_ESCAPE):
		pygame.mixer.music.fadeout(1)
		pygame.mixer.Channel(1).set_volume(SFXVolume)
		pygame.mixer.Channel(1).play(pygame.mixer.Sound(QuitSound))
		screen.blit(SaveText, (200,200))
		pygame.display.flip()
		pygame.time.wait(420)
		for i in range(10, 210, 10):
			blit_alpha(screen, bLaCksCrEEn, (0,0), i)

			pygame.time.wait(20)
		exit()

	if Currently_Selected != 0 and Reticlex >= 18 and Currently_Selected.x >= 18:
		Reticlex = 18
	if Currently_Selected !=0 and Reticlex >= 18 and Currently_Selected.x >= 18:
		Reticlex = 18
	if  Reticley >= 9:
		Reticley = 9
		if Currently_Selected != 0 and Currently_Selected.Phase != 4:
			Currently_Selected.y = Reticley
	if  Reticlex >= 18:
		Reticlex = 18
		if Currently_Selected != 0 and Currently_Selected.Phase != 4:
			Currently_Selected.x = Reticlex
	if Reticlex <= 0:
		Reticlex = 0
		if Currently_Selected != 0 and Currently_Selected.Phase != 4:
			Currently_Selected.x = Reticlex
	if Reticley <= 0:
		Reticley = 0
		if Currently_Selected != 0 and Currently_Selected.Phase != 4:
			Currently_Selected.y = Reticley

#STAGE 4: MAKE MOVEMENT TIMER
	if Currently_Selected != 0 and Currently_Selected.Phase == 2:
		Currently_Selected.Activity -= 3.5
	if Currently_Selected !=0 and Currently_Selected.Activity <= 1 and Currently_Selected.Phase == 2:
		PhaseFocus = 1
		Currently_Selected.Phase = 3

	if Currently_Selected != 0 and Currently_Selected.Phase == 3:
		for char in chars:
			char.PauseActivity = char.Activity
			char.Activity = char.PauseActivity

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
		#pygame.mixer.Channel(1).set_volume(SFXVolume)
		#pygame.mixer.Channel(1).play(pygame.mixer.Sound(Menu_InitSFX), 1)
		Currently_Focused_Menu.blit(screen)

	# the thing at the top
	screen.blit(Border,(0,0))
	for i, char in enumerate(chars):
		screen.blit(HUDHpActivBarHolder, (char.x*50, char.y*50 + 70))
		pygame.draw.rect(screen, GREEN, (char.x*50 + 2, char.y*50 + 78, char.HP, 3))
		pygame.draw.rect(screen, BLUE, (char.x*50 + 2, char.y*50 + 72, char.Activity/2.1, 3))

		if char.team == "Ally":
			HUDText = "     "+char.Name +"             HP:  " + str(char.HP)
			HUDCharacter_Tile = pygame.transform.scale(char.Character_Tile,(20,25))
			HUDActivityGaugeBack = pygame.transform.smoothscale(Reticle,(105,10))
			screen.blit(HUDCharacter_Tile, (30 + i*150, 0))
			screen.blit(HUDActivityGaugeBack, (60 + i*150, 10))
			pygame.draw.rect(screen, BLUE, (60 + i*150, 11, char.Activity, 8))
			if char.Phase == 3:
				pygame.draw.rect(screen, RED, (850, 120 + i*40, Currently_Selected.Weapon.ActivityDrain, 15))

			Character_Desctiptions = HUDfont.render(HUDText,False,(255,255,255))
			screen.blit(Character_Desctiptions,(50 + i*150, 0))
	

#Player Weapon Descriptions:
	if isinstance(Currently_Selected, Character) and Currently_Selected.Phase == 4 and Currently_Selected != 0:
		if Currently_Focused_Menu not in [None, -1]:
			texttorenderto = [
				Currently_Selected.Weapon.name,
				"Str.:" + str(Currently_Selected.Weapon.Strength),
				"Crit.: " + str(Currently_Selected.Weapon.Crit),
				"# Use Left: " + str(Currently_Selected.Weapon.amount),
				"Sp. Ability: ",
				Currently_Selected.Weapon.Sp_Ability,
				"Def.: " + str(Currently_Selected.Weapon.Defense)
			] 
			blit_alpha(screen, Currently_Focused_Menu.background_image, (0, 25), 128)
			for i in range(len(texttorenderto)):
				Weapon_Desctiptions = Menufont.render(texttorenderto[i],False,(255,255,255))
				screen.blit(Weapon_Desctiptions,(20,40 + i*50))

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
					screen.blit(ENMWeapon_Desctiptions,(120,40 + i*50))

	for char in chars:
		if Currently_Selected != 1 and char.Phase == 1 and Reticlex == char.x and Reticley == char.y and char.State != "smoked" and char.Phase !=4:
				Characterbubblename = Menufont.render("  "+char.Name,False,(255,255,255))
				CharacterBubblehealth = Menufont.render("HP: " + str(char.HP),False,(255,255,255))
				CharacterBubbleweapon = Menufont.render("Weapon: " + str(char.Weapon.name),False,(255,255,255))
				screen.blit(Status_Bubble,(char.x*50 - 10, char.y*50 - 50))
				screen.blit(Characterbubblename,(char.x*50 - 5, char.y*50 - 45))
				screen.blit(CharacterBubblehealth,(char.x*50 + 90, char.y*50 - 45))
				screen.blit(CharacterBubbleweapon,(char.x*50 + 5, char.y*50 - 25))
	

#Timer
	Timer -= pygame.time.wait(1//-1)
	TimerText = Menufont.render(str(Timer),False,(255,255,255))
	screen.blit(TimerText,(450,520))
	if Timer <= 0:
		exit()
	
	ScoreText = Menufont.render("Score: " + str(Playerscore),False,(255,255,255))
	screen.blit(ScoreText,(700,520))
# STAGE 10: A delay to stop it from going too fast and flip image buffer
	clock.tick(60)
	#flip the image buffer
	pygame.display.flip()

pygame.quit()
