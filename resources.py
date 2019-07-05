import pygame
screen = pygame.display.set_mode((960, 540))

pygame.init()
Menufont = pygame.font.Font('Fonts/AMT.otf', 20)
IconFont = pygame.font.Font('Fonts/Donjonikons.ttf', 20)
CommandListfont = pygame.font.Font('Fonts/Ace-Attorney.ttf', 20)

#Character Graphics LOAD AREA
Reticle = pygame.image.load("Images/Reticle.png").convert_alpha()
char1Idle = pygame.image.load("Images/Main_Char_1/Main Character Idle Animation 1.png").convert_alpha()
char2Idle1 = pygame.image.load("Images/Side Char 2.png").convert_alpha()
char3Idle1 = pygame.image.load("Images/Side_Char_3/Side Char 3.png").convert_alpha()
char4Idle1 = pygame.image.load("Images/Side_Char_4/Side Char 4.png").convert_alpha()
CharUnderFog = pygame.image.load("Images/Fog_Char.png").convert_alpha()


CommandsList = pygame.image.load ("Images/CommandList.png").convert()
#Other Graphics LOAD AREA
GameplayCursor = pygame.image.load("Images/cursor.png").convert_alpha()
HealthBar = pygame.image.load("Images/Health Bar.png").convert_alpha()
Selectable_Reticle = pygame.image.load("Images/Selectable Box.png").convert()
Recoverable_Reticle = pygame.image.load("Images/Selectable Recovery Box.png").convert()
Smoke_Reticle = pygame.image.load("Images/Smoke Box.png").convert_alpha()
Thunder_Reticle = pygame.image.load("Images/Thunder Box.png").convert()
Satus_Bubble = pygame.image.load("Images/Staus Text.png").convert_alpha()
CommandList = pygame.image.load("Images/CommandList.png").convert()
Minimap =  pygame.image.load("Images/MiniMAP 1.png").convert()
SaveText = pygame.image.load("Images/SaveText.png").convert()
bLaCksCrEEn = pygame.image.load("Images/BlackScreen.jpg").convert()
FountainOfYouthSprite = pygame.image.load("Images/Fountain of youth.png").convert_alpha()
Actvivtygaugesprite = pygame.image.load("Images/Activity_Gauge.png").convert_alpha()

#Sound Effects LOAD AREA
QuitSound = pygame.mixer.Sound("SFX/QuitSound.wav")
ScrimitarClashSound = pygame.mixer.Sound("SFX/Sword_Clash.wav")
DualMasamuneClashSound = pygame.mixer.Sound("SFX/Masamune_Clash.wav")
PotionUseSound = pygame.mixer.Sound("SFX/Potion_Use.wav")
BindingBladeClashSound = pygame.mixer.Sound("SFX/BindingBlade_Clash.wav")
NevanStrumSound = pygame.mixer.Sound("SFX/NevanStrumSound.wav")