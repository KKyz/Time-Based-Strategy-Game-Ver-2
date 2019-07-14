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
		Level1_Tiles = [
			Tile("Grass1", True), # Tile 1
			Tile("Forst1", True), # Tile 2
			Tile("Grass2", False), # Tile 3
			Tile("Grass4", True), # Tile 4
			Tile("Lake1", False), # Tile 5
			Tile("Wall1", False), # Tile 6
			Tile("Grass3", False), # Tile 7
			Tile("BrokenPillar", False), # Tile 8
			Tile("CaveCorner", False) #Tile 9
		]

		Level2_Tiles = [
			Tile("FloorTile1", True), #Tile 0
			Tile("FloorTile2", True), #Tile 1
			Tile("Exit1", True), #Tile 2
			Tile("Exit2", True), #Tile 3
			Tile("Wall4", False), # Tile 4
			Tile("Wall3", False), # Tile 5
			Tile("Stairs1", True), # Tile 6
			Tile("Door1", True), # Tile 7
			Tile("Door2", True), # Tile 8
			Tile("Wall2", False) # Tile 9
		]

		Level3_Tiles = [
			
			Tile("Forst2", False), # Tile 0
			Tile("Forst3", False), # Tile 1
			Tile("Forst4", False), # Tile 2
			Tile("Gate1", False), # Tile 3
			Tile("Ground1", True), # Tile 4
			Tile("Ground2", True), # Tile 5
			Tile("Ground3", True), # Tile 6
			Tile("Ground4", True), # Tile 7
			Tile("Ground5", True), # Tile 8
			Tile("Wall2", False) # Tile 9


		]

		self.tiles = []
		lines = mapstr.split('\n')
		lines.pop()
		for j, line in enumerate(lines):
			for i in range(15):
				self.tiles.append(Level3_Tiles[ord(line[i])-48].copy_template(i, j))

	def load_images(self):
		self.images = {
			#Tiles For Level 1
			"Forst1":pygame.image.load("Images/Tiles/Level1/Forst1.png"),
			"Grass1":pygame.image.load("Images/Tiles/Level1/Grass1.png"),
			"Grass2":pygame.image.load("Images/Tiles/Level1/Grass2.png"),
			"Grass3":pygame.image.load("Images/Tiles/Level1/Grass3.png"),
			"Grass4":pygame.image.load("Images/Tiles/Level1/Grass4.png"),
			"Lake1":pygame.image.load("Images/Tiles/Level1/Lake1.png"),
			"Border":pygame.image.load("Images/UI/Border.png"),
			"Bridge1":pygame.image.load("Images/Tiles/Level1/Bridge 1.png"),
			"Wall1":pygame.image.load("Images/Tiles/Level1/Wall1.png"),
			"BrokenPillar":pygame.image.load("Images/Tiles/Level1/Broken Pillar.png"),
			"CaveCorner":pygame.image.load("Images/Tiles/Level1/CaveCorner.png"),
			#Tiles For Level 2
			"FloorTile1":pygame.image.load("Images/Tiles/Level2/FloorTile1.png"),
			"FloorTile2":pygame.image.load("Images/Tiles/Level2/FloorTile2.png"),
			"Exit1":pygame.image.load("Images/Tiles/Level2/Exit1.png"),
			"Exit2":pygame.image.load("Images/Tiles/Level2/Exit2.png"),
			"Wall4":pygame.image.load("Images/Tiles/Level2/Wall4.png"),
			"Wall3":pygame.image.load("Images/Tiles/Level2/Wall1.png"),
			"Stairs1":pygame.image.load("Images/Tiles/Level2/Stairs1.png"),
			"Door1":pygame.image.load("Images/Tiles/Level2/Door1.png"),
			"Door2":pygame.image.load("Images/Tiles/Level2/Door2.png"),
			"Wall2":pygame.image.load("Images/Tiles/Level2/Wall2.png"),
			#Tiles For Level 3
			"Forst2":pygame.image.load("Images/Tiles/Level3/Forst1.png"),
			"Forst3":pygame.image.load("Images/Tiles/Level3/Forst2.png"),
			"Forst4":pygame.image.load("Images/Tiles/Level3/Forst3.png"),
			"Gate1":pygame.image.load("Images/Tiles/Level3/Gate1.png"),
			"Ground1":pygame.image.load("Images/Tiles/Level3/Ground1.png"),
			"Ground2":pygame.image.load("Images/Tiles/Level3/Ground2.png"),
			"Ground3":pygame.image.load("Images/Tiles/Level3/Ground3.png"),
			"Ground4":pygame.image.load("Images/Tiles/Level3/Ground4.png"),
			"Ground5":pygame.image.load("Images/Tiles/Level3/Ground5.png"),


		}

	def render(self, screen):
		for tile in self.tiles:
			pygame.draw.rect(screen, (0,0,0), pygame.Rect(50 * tile.x, 20 + 50 * tile.y, 50, 50))
			screen.blit(self.images[tile.type], (50 * tile.x, 20 + 50 * tile.y))
		screen.blit(self.images["Border"], (0,0))

	