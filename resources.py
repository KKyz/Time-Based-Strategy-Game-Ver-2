import pygame
from Animation import *
import Character
pygame.init()


screen = pygame.display.set_mode((960,540))
Menufont = pygame.font.Font('Fonts/AMT.otf', 20)
HUDfont = pygame.font.Font('Fonts/AMT.otf', 15)
IconFont = pygame.font.Font('Fonts/Donjonikons.ttf', 20)
#Character Graphics LOAD AREA
Reticle = pygame.image.load("Images/Tiles/ITEMS AND SELECTABLES/Reticle.png").convert_alpha()
EnemyIdle1 = pygame.image.load("Images/Characters/EnemyChar/Side Char 2.png").convert_alpha()
AllyIdle1 = pygame.image.load("Images/Characters/Side_Char_3/Side Char 3.png").convert_alpha()

#Special Character Graphics LOAD AREA
CharUnderFog = pygame.image.load("Images/Characters/SpecialEffectsChar/Fog_Char.png").convert_alpha()



#Other Graphics LOAD AREA
Border = pygame.image.load("Images/UI/Border.png")
HUDHpActivBarHolder = pygame.image.load("Images/UI/CharacterHPActivBarHolder.png")
GameplayCursor = pygame.image.load("Images/UI/cursor.png").convert_alpha()
Selectable_Reticle = pygame.image.load("Images/Tiles/ITEMS AND SELECTABLES/Selectable Box.png").convert()
Recoverable_Reticle = pygame.image.load("Images/Tiles/ITEMS AND SELECTABLES/Selectable Recovery Box.png").convert()
Haste_Reticle = pygame.image.load("Images/Tiles/ITEMS AND SELECTABLES/Selectable Haste Box.png").convert()
Slow_Reticle = pygame.image.load("Images/Tiles/ITEMS AND SELECTABLES/Selectable Slow Box.png").convert()
Thunder_Reticle = pygame.image.load("Images/Tiles/ITEMS AND SELECTABLES/Thunder Box.png").convert()
Status_Bubble = pygame.image.load("Images/UI/Staus Text.png").convert_alpha()
SaveText = pygame.image.load("Images/UI/SaveText.png").convert()
bLaCksCrEEn = pygame.image.load("Images/BlackScreen.bmp").convert()
FountainOfYouthSprite = pygame.image.load("Images/Tiles/ITEMS AND SELECTABLES/Fountain of youth.png").convert_alpha()

#Sound Effects LOAD AREA
QuitSound = pygame.mixer.Sound("SFX/QuitSound.wav")
ScrimitarClashSound = pygame.mixer.Sound("SFX/Sword_Clash.wav")
DualMasamuneClashSound = pygame.mixer.Sound("SFX/Masamune_Clash.wav")
PotionUseSound = pygame.mixer.Sound("SFX/Potion_Use.wav")
BindingBladeClashSound = pygame.mixer.Sound("SFX/BindingBlade_Clash.wav")
NevanStrumSound = pygame.mixer.Sound("SFX/NevanStrumSound.wav")

Menu_CursorMoveSFX = pygame.mixer.Sound("SFX/Menu_CursorMove.wav")
Menu_SelectSFX = pygame.mixer.Sound("SFX/Menu_Select.wav")
Menu_EndTurnSFX = pygame.mixer.Sound("SFX/Menu_EndTurn.wav")
Menu_CancelSFX = pygame.mixer.Sound("SFX/Menu_Cancel.wav")
Menu_InitSFX = pygame.mixer.Sound("SFX/Menu_Initilize.wav")
# #Character Animations LOAD AREA
# #MovementAnimations
# RunLeftAnimation = Animation(char.animation_dir + "RunLeft", 3)
# RunDownAnimation = Animation(char.animation_dir + "RunDown", 3)
# RunRightAnimation = Animation(char.animation_dir + "RunRight", 3)
# #AttackAnimations
# ScrimitarAttackAnimation = Animation(char.animation_dir + "SwordAttack", 4)
# ClawSlashAnimation = Animation(char.animation_dir + "ClawSlash", 3)
# NevanStrumAnimation = Animation(char.animation_dir + "Guitar Strum", 3)


