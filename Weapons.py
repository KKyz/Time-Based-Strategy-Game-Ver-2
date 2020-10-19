from Menu import Menu
from usables import Weapon
from resources import ScrimitarClashSound, DualMasamuneClashSound, NevanStrumSound, BindingBladeClashSound

# This is a list of weapon and item descriptions. The descriptions require name, icon, menu category, damage, critical hit chance, special ability, defense, amount, offsets, and the drain of the activity bar used by the weapon respectively

Scrimitar = Menu("Scrimitar","A",[Weapon("Scrimitar", 100, 5,0.3,"",5, 10, 5, ScrimitarClashSound, [[0, 1], [0, -1], [-1, 0], [1, 0],[1, 1],[1, -1],[-1, 1],[-1, -1]])])
Basalt_Gauntlets = Menu("Basalt Gauntlets","N",[Weapon("Bas. Gauntlet", 275, 7,0.7,"",10, 25, 2, DualMasamuneClashSound, [[1, 1], [-1, 1], [1, -1], [-1,-1]])])
Nevan = Menu("Barettas","y",[Weapon("Barettas", 250, 3,0.2,"",3, 45, 9, NevanStrumSound, [[1, 0], [-1, 0], [-2, 1], [2, 1], [-2, -1], [2, -1], [0, 1], [0, -1]])])
Binding_Blade = Menu("Box O' Doom","A",[Weapon("Box O' Doom", 1000, 50,0.7,"",45, 55, 4, BindingBladeClashSound, [[-1, 0],[ 1, 0],[ 0, 1],[ 0,-1],[-2, 0],[ 2, 0],[ 0,-2],[ 0, 2],[-1, 1],[-1,-1],[ 1,-1],[ 1, 1]])])
Fists = Weapon("Fists", 0, 37,0.3,"",5)

Attack = Menu("Arsenal","A",[Scrimitar])

#Weapons=[Scrimitar, Basalt_Gauntlets, Nevan, Binding_Blade]
#for Weapon in Weapons:
#    if Weapon.amount >= 1:
#        Attack.items.append(Weapon)
#    if Weapon.amount <= 0:
#        Attack.items.remove(Weapon)
