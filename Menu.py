import pygame
import utils
from resources import *
from WavyText import WaveText
from usables import SFXVolume, Weapon,Item, EndTurn
class Menu:
	def __init__(self, name, icon, items):
		self.x = 50
		self.y = 100
		self.items = items
		self.name = name
		self.icon = icon
		self.CursorPoint = 0
		self.above = None
		self.background_image = pygame.image.load("Images/UI/Action Menu.png")
		self.background_image = pygame.transform.scale(self.background_image, (200, 302))

		self.wavys = []
		for itemid, item in enumerate(self.items):
			if isinstance(item, Menu):
				self.wavys.append(WaveText(item.name, (self.x - 40, self.y + 50 * itemid), 5, -0.3, 4, 1.5, Menufont))
		try:
			self.amount = item.amount
		except:
			self.amount = None

	def move_cursor_up(self):
		pygame.mixer.Channel(1).set_volume(SFXVolume)
		pygame.mixer.Channel(1).play(pygame.mixer.Sound(Menu_CursorMoveSFX))
		if self.CursorPoint -1 >= 0:
			self.CursorPoint -= 1
		else:
			self.CursorPoint = len(self.items) - 1

	def move_cursor_down(self):
		pygame.mixer.Channel(1).set_volume(SFXVolume)
		pygame.mixer.Channel(1).play(pygame.mixer.Sound(Menu_CursorMoveSFX))
		if self.CursorPoint +1 < len(self.items):
			self.CursorPoint += 1
		else:
			self.CursorPoint = 0

	def select(self, target):
		if len(self.items) == 0:
			return -1
		if len(self.items) == 1 and not isinstance(self.items[0],Menu):
			if isinstance(self.items[0], Weapon):
				return self.items[0]
			if isinstance(self.items[0], Item):
				# self.items[0].use(target)
				# return -3
				return self.items[0]
		return self.items[self.CursorPoint]

	def blit(self, screen):
		utils.blit_alpha(screen, self.background_image, (self.x - 55, 29), 230)
		i = 0
		for itemid, item in enumerate(self.items):
			if isinstance(item, Menu):
				Itemtext = Menufont.render(item.name, False, (255,255,255))
				Icontext = IconFont.render(item.icon, False, (255,255,255))
				ItemAmount = Menufont.render(str(item.amount), False, (255,255,255))
				
				if itemid == self.CursorPoint:
					utils.blit_alpha(screen, GameplayCursor, (self.x - 50, self.y + 50 * itemid), 200)
				if i == self.CursorPoint:
					self.wavys[i].update()
					self.wavys[i].draw(screen)
				else:
					screen.blit(Itemtext, (self.x - 35, self.y + 50 * itemid))
				i += 1
				screen.blit(Icontext, (self.x + 120, self.y + 50 * itemid))
				if item.amount != None:
					screen.blit(ItemAmount, (self.x + 90, self.y +50 * itemid))
				#For Blit Alpha: 0 = Completely Invisible, 200 = Completely Visible