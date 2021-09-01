import pygame


pygame.init()
Menufont = pygame.font.Font('Fonts/AMT.otf', 20)
IconFont = pygame.font.Font('Fonts/Donjonikons.ttf', 20)
CommandListfont = pygame.font.Font('Fonts/Ace-Attorney.ttf', 20)

#Character Graphics LOAD AREA
Reticle = pygame.image.load("Images/Reticle.png")
char1Idle = pygame.image.load("Images/Main_Char_1/Main Character Idle Animation 1.png")
#char1NevanStrum = makeSprite("Images/Nevan- Rocking Sprite.gif", 3)
#char1SwordSwing = makeSprite("Images/Sword Attack Gif.gif", 4)
char2Idle1 = pygame.image.load("Images/Side Char 2.png")
char3Idle1 = pygame.image.load("Images/Side_Char_3/Side Char 3.png")
char4Idle1 = pygame.image.load("Images/Side_Char_4/Side Char 4.png")


CommandsList = pygame.image.load ("Images/CommandList.png")
#Other Graphics LOAD AREA
GameplayCursor = pygame.image.load("Images/cursor.png")
HealthBar = pygame.image.load("Images/Health Bar.png")
Selectable_Reticle = pygame.image.load("Images/Selectable Box.png")
Recoverable_Reticle = pygame.image.load("Images/Selectable Recovery Box.png")
Smoke_Reticle = pygame.image.load("Images/Smoke Box.png")
Thunder_Reticle = pygame.image.load("Images/Thunder Box.png")
Satus_Bubble = pygame.image.load("Images/Staus Text.png")
CommandList = pygame.image.load("Images/CommandList.png")
Minimap =  pygame.image.load("Images/MiniMAP 1.png")
SaveText = pygame.image.load("Images/SaveText.png")
bLaCksCrEEn = pygame.image.load("Images/BlackScreen.jpg")
FountainOfYouthSprite = pygame.image.load("Images/Fountain of youth.png")
Actvivtygaugesprite = pygame.image.load("Images/Activity_Gauge.png")