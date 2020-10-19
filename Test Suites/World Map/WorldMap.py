import pygame

def createScreen(screen):
    Map = pygame.image.load("WorldMap.Png").convert()
    screen.fill((0, 0, 0))
    screen.blit(Map, (0, 0))

class cursor:
    def __init__(self, sprite, x, y):
         self.sprite = sprite
         self.x = x
         self.y = y
         self.markx = 0
         self.marky = 0
         self.markUpdated = False
         self.rect = self.sprite.get_rect()
    
    
    def render(self, screen):
        screen.blit(self.sprite, (self.x, self.y))
    
    def move_right(self):
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.x += 10
            if self.x > 830:
                self.x = 830

    def move_left(self):
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.x -= 10
            if self.x < 0:
                self.x = 0

    def move_up(self):
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.y -= 10
            if self.y < 0:
                self.y = 0

    def move_down(self):
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.y += 10
            if self.y > 360:
                self.y = 360

    def drop_mark(self, screen, cursorx, cursory, mark):
        if pygame.key.get_pressed()[pygame.K_z]:
            if self.markUpdated == False:
                self.markx = cursorx
                self.marky = cursory
                mark.x = self.markx
                mark.y = self.marky
                self.markUpdated = True
            screen.blit(mark.sprite, (self.markx, self.marky))
        else:
            self.markUpdated = False

class Character:
    def __init__(self, sprite, speed):
        self.sprite = sprite
        self.pos = pygame.Vector2()
        self.set_target((32, 30))
        self.speed = speed
        self.rect = self.sprite.get_rect()

    def render(self, screen):
        screen.blit(self.sprite, pygame.Vector2(self.pos))

    def set_target(self, pos):
        self.target = pygame.Vector2(pos)

    def move_to_target(self, idlesprite, movingsprite):
        move = self.target - self.pos
        move_length = move.length()

        if move_length < self.speed:
            self.sprite = idlesprite
            self.pos = self.target
        elif move_length != 0:
            self.sprite = movingsprite
            move.normalize_ip()
            move = move * self.speed
            self.pos += move
        else:
            self.target = self.pos

class marker:
    def __init__(self, sprite, x, y):
        self.sprite = sprite
        self.x = x
        self.y = y
        self.rect = self.sprite.get_rect()

class Entryway:
    def __init__(self, sprite, x, y):
        self.sprite = sprite
        self.pos = pygame.Vector2(x, y)
        self.rect = self.sprite.get_rect()

    def render(self, screen):
        screen.blit(self.sprite, pygame.Vector2(self.pos))

def main():
    screen = pygame.display.set_mode((848, 480))
    clock = pygame.time.Clock()

    CursorSprite = pygame.image.load("WorldMapReticle.png").convert_alpha()
    CharacterSprite = pygame.image.load("WorldMapCharacter.png").convert_alpha()
    CharacterMovingSprite = pygame.image.load("WorldMapCharacterMoving.png").convert_alpha()
    Mark = pygame.image.load("Pin.Png").convert_alpha()
    VenomEntry = pygame.image.load("Entry.Png").convert_alpha()
    MacbethEntry = pygame.image.load("Entry.Png").convert_alpha()
    MeteoEntry = pygame.image.load("Entry.Png").convert_alpha()

    VenomEnt = Entryway(VenomEntry, 95, 62)
    MacbethEnt = Entryway(MacbethEntry, 725, 281) 
    MeteoEnt = Entryway(MeteoEntry, 415, 190)

    WorldMapCursor = cursor(CursorSprite, 32, 64)
    MainChar = Character(CharacterSprite, 3.5)
    Marker = marker(Mark, 150, 250)
    MainChar.pos = pygame.Vector2(150, 250)

    LevelSet = 0

    while True:
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                return

        createScreen(screen)
        VenomEnt.render(screen)
        MacbethEnt.render(screen)
        MeteoEnt.render(screen)
        MainChar.render(screen)
        WorldMapCursor.render(screen)
        WorldMapCursor.move_right()
        WorldMapCursor.move_left()
        WorldMapCursor.move_down()
        WorldMapCursor.move_up()
        MainChar.set_target(MainChar.pos)
        WorldMapCursor.drop_mark(screen, WorldMapCursor.x, WorldMapCursor.y, Marker)
        MainChar.set_target((Marker.x, Marker.y))
        MainChar.move_to_target(CharacterSprite, CharacterMovingSprite)
        if MainChar.pos.x == VenomEnt.pos.x and MainChar.pos.y == VenomEnt.pos.y:
            LevelSet = 1
            print("LevelSet is", str(LevelSet))
        if MainChar.pos.x == MacbethEnt.pos.x and MainChar.pos.y == MacbethEnt.pos.y:
            LevelSet = 2
            print("LevelSet is", str(LevelSet))
        if MainChar.pos.x == MeteoEnt.pos.x and MainChar.pos.y == MeteoEnt.pos.y:
            LevelSet = 3
            print("LevelSet is", str(LevelSet))
        pygame.display.flip()
        clock.tick(60)




if __name__ == '__main__':
    main()