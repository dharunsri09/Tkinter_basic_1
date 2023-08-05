from tkinter import Tk,Label
from datetime import datetime
import tkinter.font as tkFont
window=Tk()
window.title("Django")
window.geometry("600x300")

def clock():
    time=datetime.now().strftime("%H:%M:%S")
    label.configure(text=time)
    label.after(500,clock)


window.configure(bg="steelblue")
font_style = tkFont.Font(family="Arial Black", size=70)
label=Label(window,font=font_style,bg="steelblue",fg="white")
label.pack(pady=100)

clock()
window.mainloop()
