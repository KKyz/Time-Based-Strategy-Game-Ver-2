import pygame
from Animation import *
# from FECD import Scrimitar, Nevan, Dual_Masamune

class Character:
	"""
	
	Phase 1 = Not Selected
	Phase 2 = Moving Character
	Phase 3 = Menu
	Phase 4 = Select Victim
	
	"""
	Name = ""
	Character_Tile = ""
	team = ""
	selected = False
	HP = 10
	Level = 1
	Phase = 1
	def __init__(self,nName,nWeapon,nCharacter_Tile,nteam,nx,ny,nHP,nActivity, nanimation_dir):
		self.Name = nName
		self.State = 0
		self.Character_Tile = nCharacter_Tile
		self.Weapon = nWeapon
		self.x = nx
		self.y = ny
		self.StoredPositionx = nx
		self.StoredPositiony = ny
		self.team = nteam
		self.HP = 2
		self.MAXHP = nHP
		self.Activity = nActivity
		self.StoredActivity = nActivity
		self.Maxact = nActivity
		self.PauseActivity = nActivity
		self.animation_dir = nanimation_dir
		self.State = 0xBABA
		
		

	def ChecknUpdate_State(self):
		if self.HP == 0:
			#self.Character_Tile = Dead_Grave
			self.State = 0xBABA
	
	def render(self, screen):
		screen.blit(self.Character_Tile, (self.x * 50, 20 + self.y * 50))

	def activity_gauge(self):
		if self.Phase == 2:
			self.Activity -= 1
		if self.Activity == 0 and self.Phase != 3:
			if self.Phase != 4:
				self.Activity += 100
			if self.Activity >= self.Maxact:
				self.Activity = self.Maxact

	
	
 