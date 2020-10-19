
import pygame
#CONTROLLER SETUP
joysticks = [] # Opens up a new list for the number of joysticks currently connected to the computer
for i in range(pygame.joystick.get_count()): # For every controller connected...
	joysticks = (pygame.joystick.Joystick(i)) # the term joysticks will mean every single joysrick connected
	joysticks.init() # initialise joysticsk so that multiple joysticks could be used	
   
#Controls For Controller
axes = joystick.get_numaxes()
for i in range( axes ):
    axis = joystick.get_axis( i )
    if axis >= 1:
        if PhaseFocus == 0 or PhaseFocus == 2:
            Reticley -=1
        if Currently_Selected != 0 and Currently_Selected.Phase == 2:
            Currently_Selected.y =Reticley
        if PhaseFocus == 1 and Currently_Focused_Menu != 0:
            Currently_Focused_Menu.move_cursor_up()
    if axis <= -1:
        if PhaseFocus == 0 or PhaseFocus == 2:
            Reticley +=1
        if Currently_Selected != 0 and Currently_Selected.Phase == 2:
            Currently_Selected.y =Reticley
        if PhaseFocus == 1 and Currently_Focused_Menu != 0 and Currently_Focused_Menu != None:
            Currently_Focused_Menu.move_cursor_down()

if event.type == pygame.JOYBUTTONDOWN:
    if event.button == 0:
        for c in chars:
            if Reticlex == c.x and Reticley == c.y and c.Phase == 1 and c.team == "Ally" and c.Phase!= 2 and Currently_Selected == 0 and c.Activity == c.Maxact:
                Currently_Selected = c
                Currently_Selected.StoredPositionx = Currently_Selected.x
                Currently_Selected.StoredPositiony = Currently_Selected.y
                c.StoredActivity = c.Activity
                c.Phase = 2

            if PhaseFocus == 1 and c.Phase == 3:
                ret = Currently_Focused_Menu.select(c)
                if ret != -1 and not isinstance(ret, Weapon) and not isinstance(ret, Item) and not isinstance(ret, AOEItem) and not isinstance(ret, EndTurn):# and ret != -3:
                    Currently_Focused_Menu = ret
                if isinstance(ret, Weapon) or isinstance(ret, Item) or isinstance(ret, AOEItem):
                    if isinstance(ret, Item):
                        ret.offset = utils.get_offset_of_all_units(chars, c)

                    selectable_positions = get_positions_around_reticle((c.x, c.y), ret.offsets)
                    c.Phase = 4
                    selected_usable = ret
                    PhaseFocus = 2
                if isinstance(ret, EndTurn):
                    ret.use(Currently_Selected)
                    PhaseFocus = 0
                    Currently_Selected = 0
                    Currently_Focused_Menu = Actions

            if c.Phase == 4:
                tile = (Reticlex, Reticley)
                if tile in selectable_positions:
                    if isinstance(ret, AOEItem):
                        # [PLANT USE ITEMS]
                        newentity = selected_usable.use((Reticlex, Reticley))
                        entities.append(newentity)
                        Currently_Focused_Menu = Actions
                        if Currently_Selected.Phase == 4:
                            Currently_Selected.Phase = 1
                            Currently_Selected = 0
                        selected_usable = None
                        selectable_positions = []
                    else:
                        # [SINGLE USE ITEMS]
                        for char in chars:
                            if char.team == "Enemy" and char.x == Reticlex and char.y == Reticley:
                                if selected_usable == Item:
                                    selected_usable.use(char)
                                if selected_usable == Weapon:
                                    print("Despacito")
                                    selected_usable.use(char, Currently_Selected)
                                Currently_Focused_Menu = Actions
                                if Currently_Selected.Phase == 4:
                                    Currently_Selected.Phase = 1
                                    Currently_Selected = 0
                                selected_usable = None
                                selectable_positions = []
                PhaseFocus = 0
    if event.button == 2:
        if Currently_Selected != 0:
            selectable_positions = []	
            if Currently_Selected.Phase == 3 and Currently_Focused_Menu == Actions:
                Currently_Selected.Phase = 1
                Currently_Selected.x = Currently_Selected.StoredPositionx
                Currently_Selected.y = Currently_Selected.StoredPositiony
                c.Activity = c.StoredActivity
                Currently_Selected = 0
                PhaseFocus = 0
            elif Currently_Selected.Phase == 4 or  Currently_Selected.Phase == 2:
                PhaseFocus = 1
                Currently_Selected.Phase = 3
            else:
                Currently_Selected.Phase = 3
        
        if PhaseFocus == 1 and isinstance(Currently_Selected, Character) and Currently_Selected.Phase == 3:
            Currently_Focused_Menu = Currently_Focused_Menu.above
            if Currently_Focused_Menu == None:
                Currently_Focused_Menu = Actions
