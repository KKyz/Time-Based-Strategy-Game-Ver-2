import pygame
import random
from resources import FountainOfYouthSprite, Selectable_Reticle, Recoverable_Reticle, HealthBar, Smoke_Reticle, Thunder_Reticle, CharUnderFog, PotionUseSound, ScrimitarClashSound
from Character import Character
from utils import blit_alpha



class AOEItem:
	def __init__(self, name, amount, placement_offsets, effect_offsets):
		self.offsets = placement_offsets
		self.amount = amount
		self.effect_offsets = effect_offsets
		self.position = (0, 0)
		self.name = name
		self.instance = False
		self.action_performed = False

	def use(self, position):
		self.amount -= 1
		if self.amount >= 1:
			newItem = AOEItem(self.name, self.amount, self.offsets, self.effect_offsets)
			newItem.position = position
			newItem.instance = True
			return newItem

	def update(self, chars):
		if self.name == "Fountain of youth":
			self.fountain_of_youth(chars)
		elif self.name == "Smoke screen":
			if self.action_performed is False:
				self.smoke_screen(chars)
	
	def fountain_of_youth(self, chars):
		for char in chars:
			positions = [[self.position[0] + offset[0], self.position[1] + offset[1]] for offset in self.effect_offsets]
			if [char.x, char.y] in positions:
				char.HP = min(char.HP + 4, char.MAXHP)

	def Thunder_Scroll(self, chars):
		for char in chars:
			positions = [[self.position[0] + offset[0], self.position[1] + offset[1]] for offset in self.effect_offsets]
			if [char.x, char.y] in positions:
				char.HP = min(char.HP - 8, char.HP)

	def smoke_screen(self, chars):
		charactersinrange = []
		for char in chars:
			positions = [[self.position[0] + offset[0], self.position[1] + offset[1]] for offset in self.effect_offsets]
			if [char.x, char.y] in positions:
				charactersinrange.append(char)
				char.Character_Tile = CharUnderFog

		character_positions = [[char.x, char.y] for char in charactersinrange]
		swapped_values = []
		for i in range(len(charactersinrange)):
			v = 0
			while True:
				v = random.randint(0, len(charactersinrange)-1)
				if v not in swapped_values:
					swapped_values.append(v)
					break
			charactersinrange[i].x = character_positions[v][0]
			charactersinrange[i].y = character_positions[v][1]
		
		self.action_performed = True
	


	def render(self, screen):
		screen.blit(FountainOfYouthSprite, (self.position[0] * 50, self.position[1] * 50 + 20))

	def renderAOE(self, screen):
		for offset in self.effect_offsets:
			pos = [(self.position[0] + offset[0]) * 50, (self.position[1] + offset[1]) * 50 + 20]
			if self.name == "Fountain of youth":
				blit_alpha(screen, Recoverable_Reticle, pos, 100)
			if self.name == "Smoke screen":
				blit_alpha(screen, Smoke_Reticle, pos, 300)
			if self.name == "Thunder Scroll":
				blit_alpha(screen, Thunder_Reticle, pos, 120)

			


class Item:
	def __init__(self, name, amount, offset):
		self.name = name
		self.amount = amount
		self.offsets = offset

	def use(self, target):
		self.amount -= 1
		if self.amount >= 1:
			if self.name == "Potion":
				self.potion(target)
			elif self.name == "Hi-potion":
				self.hi_potion(target)
			elif self.name == "Angelic Robe":
				self.angelic_robe(target)
		# print("Oh, I'm being used!")
		# activitygauge = 0

	def potion(self, target):
		pygame.mixer.Sound.play(PotionUseSound)
		pygame.mixer.music.stop()
		target.HP += 10
		if target.HP > target.MAXHP:
			target.HP = target.MAXHP
		print(self.name)

	def hi_potion(self, target):
		pygame.mixer.Sound.play(PotionUseSound)
		pygame.mixer.music.stop()
		target.HP += 30
		if target.HP > target.MAXHP:
			target.HP = target.MAXHP
		print(self.name)
	
	def angelic_robe(self, target):
		target.defense += 10
		print(self.name)


class Weapon:
	name="default"
	def __init__(self, name="wood", Strength=10, Crit=0.01, Sp_Ability="none", Defense = 2, ActivityDrain = 10, SFX = ScrimitarClashSound, offsets = [[-1,0], [1,0], [0,1], [0,-1]]):
		self.name = name
		self.Strength = Strength
		self.Crit = Crit
		self.Sp_Ability = Sp_Ability
		self.offsets = offsets
		self.Defense = Defense
		self.SFX = SFX
		self.ActivityDrain = ActivityDrain
	
	def use(self, target, Character):
		#blit_alpha(screen, HealthBar,(100,50),190)
		pygame.mixer.Sound.play(self.SFX)
		pygame.mixer.music.stop()
		defense = 0
		if target.Weapon != None:
			damage = self.Strength + self.Crit
			Character.Activity -= self.ActivityDrain
			target.HP -= self.Strength
			target.ChecknUpdate_State()
		if Character.Activity <= self.ActivityDrain:
			Currently_Focused_Menu = Weapon

		# activitygauge = 0

class EndTurn:
 	def use(self, target):
 		target.Phase = 1
 		target.StoredPositionx = target.x 
 		target.StoredPositiony = target.y
		
