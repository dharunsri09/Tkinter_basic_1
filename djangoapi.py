from tkinter import Tk,Label
window=Tk()
window.title("Django")
window.geometry("450x300")

window.configure(bg="steelblue")
label=Label(window,text="Hello",font={"Arial black",70,"bold"})
label.pack(pady=100)
window.mainloop()
