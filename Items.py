from Menu import Menu
from usables import Item

#Item Ititializations
potion = Menu("potion","E",[Item("Potion", 5, 100, [[0, 0], [-1, 0], [ 1, 0], [ 0, 1],[ 0,-1],[-2, 0],[ 2, 0],[ 0,-2],[ 0, 2],[-1, 1],[-1,-1],[ 1,-1],[ 1, 1]])])
Hi_potion = Menu("Hi-potion", "E",[Item("Hi-potion", 3, 250, [[0, 0], [-1, 0], [ 1, 0],[ 0, 1],[ 0,-1],[-2, 0],[ 2, 0],[ 0,-2],[ 0, 2],[-1, 1],[-1,-1],[ 1,-1],[ 1, 1]])])

Remedies = Menu("Items","E",[potion, Hi_potion])