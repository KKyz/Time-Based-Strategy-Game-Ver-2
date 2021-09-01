import pygame
import utils
from resources import *
from usables import *
from WavyText import WaveText

class Menu:
	def __init__(self, name, icon, items):
		self.name = name
		self.icon = icon
		self.items = items
		self.CursorPoint = 0
		self.x = 50
		self.y = 100
		self.above = None
		self.background_image = pygame.image.load("Images/Action Menu.png")
		self.background_image = pygame.transform.scale(self.background_image, (200, 300))

		self.wavys = []
		for itemid, item in enumerate(self.items):
			if isinstance(item, Menu):
				self.wavys.append(WaveText(item.name, (self.x + 10, self.y + 50 * itemid), 6, 5, 1.5, 2.5, Menufont))

	def move_cursor_up(self):
		if self.CursorPoint -1 >= 0:
			self.CursorPoint -= 1
		else:
			self.CursorPoint = len(self.items) - 1

	def move_cursor_down(self):
		if self.CursorPoint +1 < len(self.items) :
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
		utils.blit_alpha(screen, self.background_image, (self.x, 20), 128)
		i = 0
		for itemid, item in enumerate(self.items):
			if isinstance(item, Menu):
				Itemtext = Menufont.render(item.name, False, (255,255,255))
				Icontext = IconFont.render(item.icon, False, (255,255,255))
				
				if i == self.CursorPoint:
					self.wavys[i].update()
					self.wavys[i].draw(screen)
				else:
					screen.blit(Itemtext, (self.x + 10, self.y + 50 * itemid))
				i += 1
				screen.blit(Icontext, (self.x + 135, self.y + 50 * itemid))
				if itemid == self.CursorPoint:
					utils.blit_alpha(screen, GameplayCursor, (self.x + 10, self.y + 50 * itemid), 200)
					#For Blit Alpha: 0 = Completely Invisible, 200 = Completely Visible
	