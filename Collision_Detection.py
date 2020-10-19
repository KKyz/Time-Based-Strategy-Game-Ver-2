from FECD import Currently_Selected, Reticlex, Reticley

if Currently_Selected != 0 and Reticlex >= 18 and Currently_Selected.x >= 18:
    Reticlex = 18
if Currently_Selected !=0 and Reticlex >= 18 and Currently_Selected.x >= 18:
    Reticlex = 18
if  Reticley >= 9:
    Reticley = 9
    if Currently_Selected != 0:
        Currently_Selected.y = Reticley
if  Reticlex >= 18:
    Reticlex = 18
    if Currently_Selected != 0:
        Currently_Selected.x = Reticlex
if Reticlex <= 0:
    Reticlex = 0
    if Currently_Selected != 0:
        Currently_Selected.x = Reticlex
if Reticley <= 0:
    Reticley = 0
    if Currently_Selected != 0:
        Currently_Selected.y = Reticley