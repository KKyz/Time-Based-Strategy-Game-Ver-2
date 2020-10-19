from Menu import Menu
from usables import AOEItem

# AOE Scrolls Initializations
Haste_Scroll = Menu("Haste Scroll","S",[AOEItem("Haste Scroll", 3, 380, [[0, 0]], [[0, 0], [-1, 0],[ 1, 0],[ 0, 1],[ 0,-1],[-2, 0],[ 2, 0],[ 0,-2],[ 0, 2],[-1, 1],[-1,-1],[ 1,-1],[ 1, 1]])])
Slow_Scroll= Menu("Slow Scroll","S",[AOEItem("Slow Scroll", 3, 380, [[0, 0]], [[0, 0], [-1, 0],[ 1, 0],[ 0, 1],[ 0,-1],[-2, 0],[ 2, 0],[ 0,-2],[ 0, 2],[-1, 1],[-1,-1],[ 1,-1],[ 1, 1]])])
Foutain_of_Youth = Menu("Regen. Scroll","S",[AOEItem("Foutain of youth", 3, 550, [[0, 0]], [[0, 0], [-1, 0],[ 1, 0],[ 0, 1],[ 0,-1],[-2, 0],[ 2, 0],[ 0,-2],[ 0, 2],[-1, 1],[-1,-1],[ 1,-1],[ 1, 1]])])
Thunder_Scroll = Menu("Thunder Scroll", "U",[AOEItem("Thunder Scroll", 6, 250, [[0, 0]], [[-1, -3], [1, -3], [0, -2], [-1, -1], [1,-1], [-1, 1], [1, 1], [0, 2], [-1, 3], [1, 3]])])
Fire_Scroll = Menu("Fire Scroll","U",[AOEItem("Fire Scroll", 3, 450, [[0, 0]], [[1, 0], [2, 0], [0, 1], [0, 2], [0, -1], [0, -2]])])

Scrolls = Menu("Mystic Scrolls", "U",[Thunder_Scroll, Fire_Scroll, Haste_Scroll, Slow_Scroll, Foutain_of_Youth])