from Menu import Menu
from Weapons import *
from Items import *
from Scrolls import *
from End_Turn import End_Turn

Actions = Menu("Actions","A",[Attack, Scrolls, Remedies, End_Turn]) #Describes that the actions menu should contain the Attack, Scrolls, Remedies, and End_Turn sub-menus and option.
Currently_Focused_Menu = Actions # The action selection menu will always default to the Actions menu
Attack.above = Actions
End_Turn.above = Actions
Remedies.above = Actions
Scrolls.above = Actions