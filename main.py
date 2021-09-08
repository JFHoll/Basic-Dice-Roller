#Roll the Dice!

import tkinter as tk
import random

def roll():

    faces = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    dice = random.choice(faces)
    lbl2 = tk.Label(text = dice, font = ("Arial", 100))
    lbl2.grid(row = 1)

window = tk.Tk()

lbl1 = tk.Label(text = "Roll the Dice!", font = ("Arial", 50))
lbl1.grid(row = 0)

btn1 = tk.Button(text = "Roll!", command = roll, font = ("Arial", 50))
btn1.grid(row = 2)

lbl2 = tk.Label()
window.mainloop()
