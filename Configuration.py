import tkinter as tk
import tkinter.font as  tkFont
from tkinter import OptionMenu, Scale, HORIZONTAL, colorchooser, Button, BooleanVar, Checkbutton
window = tk.Tk()
window.title("FECD Setup")
window.geometry("320x580")
window.resizable(False, False)
ConfigFont = tkFont.Font(family="Ancient Modern Tales", size=15)


# Settings Label
Settings_lbl = tk.Label(text="Settings", fg="black", font=ConfigFont, compound="center")
Settings_lbl.pack(anchor=tk.CENTER)

#Resolution Label
Resolutions_lbl = tk.Label(text="Resolutions", fg="black", width=15, height=1, font=ConfigFont)
Resolutions_lbl.pack(anchor=tk.W)

#Resolution Dropdown
Resolution = tk.IntVar()
Resolution.set((848, 480))
Resolutions_Drpdwn = OptionMenu(window, Resolution, (848, 480), (1280,720), (1920,1080), (2560,1440), (3840,2160))
Resolutions_Drpdwn.pack(anchor=tk.W)

#FullScreen Checkbox
FullScreen_state = tk.IntVar()
FullScreen_state.set(False) #set check state
chk = Checkbutton(window, text='Fullscreen', var=FullScreen_state)

#Volume Label
Volume_lbl = tk.Label(text="Volume", fg="black", width=15, height=1, font=ConfigFont)
Volume_lbl.pack(anchor=tk.W)

#Background Music Volume Label
BGMVolume_lbl = tk.Label(text="Background Music Volume", fg="black", width=25, height=1, font=ConfigFont)
BGMVolume_lbl.pack(anchor=tk.W)

#Background Music Volume Slider
BGMVol_Slider = Scale(window, from_=0, to=100, orient=HORIZONTAL, font=ConfigFont)
BGMVol_Slider.set(50)
BGMVol_Slider.pack(anchor=tk.W)

BGVolume = BGMVol_Slider.get()/10

#Sound Effects Volume Label
SFXVolume_lbl = tk.Label(text="Sound Effects Volume", fg="black", width=25, height=1, font=ConfigFont)
SFXVolume_lbl.pack(anchor=tk.W)

#Sound Effects Volume Slider
SFXVol_Slider = Scale(window, from_=0, to=100, orient=HORIZONTAL, font=ConfigFont)
SFXVol_Slider.set(50)
SFXVol_Slider.pack(anchor=tk.W)

Sound_Output = tk.IntVar()
Sound_Output.set(2)

#Mono Sound Radiobutton
Mono_Sound_Rb = tk.Radiobutton(window, text="Mono", fg="black", padx=20, variable=Sound_Output, value=1, font=ConfigFont)
Mono_Sound_Rb.pack(anchor=tk.W)

#Stereo Sound Radiobutton
Stereo_Sound_Rb = tk.Radiobutton(window, text="Stereo", fg="black", padx=20, variable=tk.IntVar(), value=2, font=ConfigFont)
Stereo_Sound_Rb.pack(anchor=tk.W)

#Gameplay Settings Label
Gameplay_Settings_lbl = tk.Label(text="Gameplay Options", fg="black", width=15, height=1, font=ConfigFont)
Gameplay_Settings_lbl.pack(anchor=tk.W)

#Color Settings Label
Color_Settings_lbl = tk.Label(text="Menu Box Color", fg="black", width=20, height=1, font=ConfigFont)
Color_Settings_lbl.pack(anchor=tk.W)

#Color Chooser Button
def choose_color():
    clr = colorchooser.askcolor(title="Select Color")
    print(clr)
Color_Chooser_btn = Button(window, command=choose_color, text="choose color", borderwidth=1, font=ConfigFont)
Color_Chooser_btn.pack(anchor=tk.W)

#Battle Speed Label
Battle_Speed_lbl = tk.Label(text="Battle Speed", fg="black", width=20, height=1, font=ConfigFont)
Battle_Speed_lbl.pack(anchor=tk.W)

#Battle Speed Volume Slider
Battle_SPD_Slider = Scale(window, from_=0, to=200, orient=HORIZONTAL, font=ConfigFont)
Battle_SPD_Slider.set(100)
Battle_SPD_Slider.pack(anchor=tk.W)

BattleSpeed = Battle_SPD_Slider.get()/200

#Game Start Button
def OpenServer():
    exec(open("FECD.py").read())

Game_Start_btn = Button(window, text="Start Game", command=OpenServer, borderwidth=2, relief=tk.GROOVE, font=ConfigFont)
Game_Start_btn.pack(anchor=tk.W)

window.mainloop()