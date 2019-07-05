import pygame

class Tile:
	def __init__(self, ntype="", nPassable=True):
		self.id = 0
		self.type = ntype
		self.x = 0
		self.y = 0
		self.Passable = nPassable
	
	def copy_template(self, x, y):
		instance = Tile(self.type, self.Passable)
		instance.x = x
		instance.y = y
		return instance


class Map:
	def __init__(self, mapstr):
		self.load_images()
		tile_templates = [
			Tile("Grass1", True),
			Tile("Forst1", True),
			Tile("Hous1", False),
			Tile("Grass4", True),
			Tile("Lake1", False),
			Tile("Wall1", False)
		]
		self.tiles = []
		lines = mapstr.split('\n')
		lines.pop()
		for j, line in enumerate(lines):
			for i in range(15):
				self.tiles.append(tile_templates[ord(line[i])-48].copy_template(i, j))

	def load_images(self):
		self.images = {
			"Forst1":pygame.image.load("Images/Forst1.png"),
			"Grass1":pygame.image.load("Images/Grass1.png"),
			"Grass2":pygame.image.load("Images/Grass2.png"),
			"Grass3":pygame.image.load("Images/Grass3.png"),
			"Grass4":pygame.image.load("Images/Grass4.png"),
			"Hous1":pygame.image.load("Images/Hous1.png"),
			"Lake1":pygame.image.load("Images/Lake1.png"),
			"Border":pygame.image.load("Images/Border.png"),
			"Bridge1":pygame.image.load("Images/Bridge 1.png"),
			"Wall1":pygame.image.load("Images/Wall1.png")
		}

	def render(self, screen):
		for tile in self.tiles:
			pygame.draw.rect(screen, (0,0,0), pygame.Rect(50 * tile.x, 20 + 50 * tile.y, 50, 50))
			screen.blit(self.images[tile.type], (50 * tile.x, 20 + 50 * tile.y))
		screen.blit(self.images["Border"], (0,0))