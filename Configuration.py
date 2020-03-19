import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox

ConfigWindow = tk.Tk()
ConfigWindow.title("Strategy Curcuit Configuration")
canvas = tk.Canvas(ConfigWindow, width=450, height=700)  # define the size
canvas.pack()

class Configuration:
    labels = []

    #Language Options

    #Language Select Initialization
    EngSelect = IntVar()
    JapSelect = IntVar()
    EngSelect.set(0)
    JapSelect.set(0)

    #Langauge Radio Buttons
    Langlabel = Label(ConfigWindow, textvariable="Languages")
    EngButton = Radiobutton(ConfigWindow, text = "English",variable = EngSelect, value = 1)
    JapButton = Radiobutton(ConfigWindow, text = "Japanese", variable = JapSelect, value = 1)
    labels.append(Langlabel)
    labels.append(EngButton)
    labels.append(JapButton)

    #Buton Placements
    Langlabel.place(x = 100,y = 80)
    EngButton.place(x = 100,y = 50)
    JapButton.place(x = 180,y = 50)
    Langlabel.pack()

    #Game Resolution Options
    Resolutions=("320 x 240","640 x 480","1920 x 1080")
    ResBox = Combobox(ConfigWindow, values=Resolutions)
    ResBox.place(x = 60, y = 150)

    #def ConfigImage(self):
        #Game Image
    #   TestImage = ImageTk.PhotoImage(Image.open("TestMap.png"))
    #  self.images.add(TestImage);
    # canvas.create_image(x = 100, y = 100, anchor=NW, image=TestImage) 
Configuration()
ConfigWindow.mainloop()
