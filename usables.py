import pygame
import random
from resources import FountainOfYouthSprite, Selectable_Reticle, Recoverable_Reticle, Haste_Reticle, Slow_Reticle, Thunder_Reticle, CharUnderFog, PotionUseSound, ScrimitarClashSound, Menu_EndTurnSFX
import Character
from utils import blit_alpha

SFXVolume = 0.7

class AOEItem:
	def __init__(self, name, amount, score, placement_offsets, effect_offsets):
		self.offsets = placement_offsets
		self.amount = amount
		self.effect_offsets = effect_offsets
		self.position = (0, 0)
		self.name = name
		self.instance = False
		self.action_performed = False
		self.score = score

	def use(self, position):
		self.amount -= 1
		if self.amount >= 1:
			newItem = AOEItem(self.name, self.amount, self.score, self.offsets, self.effect_offsets)
			newItem.position = position
			newItem.instance = True
			return newItem

	def update(self, chars):
		if self.name == "Fountain of youth":
			self.fountain_of_youth(chars)
		if self.name == "Thunder Scroll":
			self.Thunder_Scroll(chars)
		if self.name == "Fire Scroll":
			self.Fire_Scroll(chars)
		if self.name == "Haste Scroll":
			self.Haste_Scroll(chars)
		elif self.name == "Slow Scroll":
			if self.action_performed is False:
				self.Slow_Scroll(chars)
	
	def fountain_of_youth(self, chars):
		for char in chars:
			positions = [[self.position[0] + offset[0], self.position[1] + offset[1]] for offset in self.effect_offsets]
			if [char.x, char.y] in positions:
				char.HP = min(char.HP + 4, char.MAXHP)

	def Thunder_Scroll(self, chars):
		for char in chars:
			positions = [[self.position[0] + offset[0], self.position[1] + offset[1]] for offset in self.effect_offsets]
			if [char.x, char.y] in positions:
				char.HP = max(-1, char.HP - 8)

	def Fire_Scroll(self, chars):
		for char in chars:
			positions = [[self.position[0] + offset[0], self.position[1] + offset[1]] for offset in self.effect_offsets]
			if [char.x, char.y] in positions:
				char.HP = max(-1, char.HP - 12)
			for i in range (5):
				positions = [[self.position[0] + offset[i]] for offset in self.effect_offsets]

	def Haste_Scroll(self, chars):
		Haste_Speed = 0
		for char in chars:
			positions = [[self.position[0] + offset[0], self.position[1] + offset[1]] for offset in self.effect_offsets]
			if [char.x, char.y] in positions:
				char.speed = char.speed/Haste_Speed
				Haste_Speed += 0.0025
				if Haste_Speed >= 2:
					Haste_Speed = 2
				

	def Slow_Scroll(self, chars):
		Slow_Speed = 0
		for char in chars:
			positions = [[self.position[0] + offset[0], self.position[1] + offset[1]] for offset in self.effect_offsets]
			if [char.x, char.y] in positions:
				char.speed = char.speed*Slow_Speed
				Slow_Speed += 0.0025
				if Slow_Speed >= 2:
					Slow_Speed = 2
				


	def render(self, screen):
		screen.blit(FountainOfYouthSprite, (self.position[0] * 50, self.position[1] * 50 + 20))

	def renderAOE(self, screen):
		for offset in self.effect_offsets:
			pos = [(self.position[0] + offset[0]) * 50, (self.position[1] + offset[1]) * 50 + 20]
			if self.name == "Fountain of youth":
				blit_alpha(screen, Recoverable_Reticle, pos, 120)
			if self.name == "Thunder Scroll":
				blit_alpha(screen, Thunder_Reticle, pos, 120)
			if self.name == "Haste Scroll":
				blit_alpha(screen, Haste_Reticle, pos, 120)
			if self.name == "Slow Scroll":
				blit_alpha(screen, Slow_Reticle, pos, 120)

			


class Item:
	def __init__(self, name, amount, score, offset):
		self.name = name
		self.amount = amount
		self.score = score
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

	def potion(self, target):
		PotionUseSound.set_volume(SFXVolume)
		PotionUseSound.play()
		target.HP += 10
		if target.HP > target.MAXHP:
			target.HP = target.MAXHP

	def hi_potion(self, target):
		pygame.mixer.Channel(3).set_volume(SFXVolume)
		pygame.mixer.Channel(3).play(pygame.mixer.Sound(PotionUseSound))
		target.HP += 30
		if target.HP > target.MAXHP:
			target.HP = target.MAXHP
	
	def angelic_robe(self, target):
		target.defense += 10


class Weapon:
	name="default"
	def __init__(self, name="wood", score=0, Strength=10, Crit=0.01, Sp_Ability="none", Defense = 2, ActivityDrain = 10, Amount = 3, SFX = ScrimitarClashSound, offsets = [[-1,0], [1,0], [0,1], [0,-1]]):
		self.name = name
		self.score = score
		self.Strength = Strength
		self.Crit = Crit
		self.Sp_Ability = Sp_Ability
		self.offsets = offsets
		self.Defense = Defense
		self.SFX = SFX
		self.ActivityDrain = ActivityDrain
		self.amount = Amount
	
	def use(self, target, Character):
		#blit_alpha(screen, HealthBar,(100,50),190)
		self.amount = self.amount - 1
		if self.amount >= 1:
			pygame.mixer.Channel(2).set_volume(SFXVolume)
			pygame.mixer.Channel(2).play(pygame.mixer.Sound(self.SFX))
			defense = 0
			if target.Weapon != None:
				damage = self.Strength + self.Crit
				Character.Activity -= self.ActivityDrain
				target.HP -= self.Strength
				target.ChecknUpdate_State()
			if Character.Activity <= self.ActivityDrain:
				Currently_Focused_Menu = Weapon
		if self.amount < 0:
			self.amount = 0

			# activitygauge = 0

class EndTurn:
	def use(self, target):
		 pygame.mixer.Channel(1).set_volume(SFXVolume)
		 pygame.mixer.Channel(1).play(pygame.mixer.Sound(Menu_EndTurnSFX))
		 target.Phase = 1
		 target.StoredPositionx = target.x 
		 target.StoredPositiony = target.y
		
