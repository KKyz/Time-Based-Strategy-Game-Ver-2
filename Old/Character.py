import pygame
import Animation


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
	def __init__(self,nName,nWeapon,nCharacter_Tile,nteam,nx,ny,nHP,nActivity, animation_dir):
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
		self.animation_dir = animation_dir

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

	# Animation List
	#self.SwordAttack = Animation(animation_dir + "SwordAttack", 4)
	#self.GuitarStrum = Animation(animation_dir + "Guitar Strum", 3)
	#self.ClawSlash = Animation(animation_dir + "ClawSlash", 3)
	

"""
0												85	 100
+-Activity-Gauge--------------------------------+-----+
|===============================================|     |


- depletion of the activity gauge when in phase 2
- depletion of the gauge when moving
- depletion of the gauge when attacking
- Only be able to play when it's full (so we switch to phase 2 at this point)
"""
