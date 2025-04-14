from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry("500x500")

equation_text = ""
equation_label = StringVar()

label = Label(window, textvariable=equation_label, 
              font=("consolas", 20), bg="white", 
              width=24, height=2, 
              )
label.pack()

window.mainloop()