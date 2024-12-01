from tkinter import *
from tkinter import messagebox
from quiz import Quiz
import json

mainWindow = Tk()
mainWindow.title("Quiz Application")

frame = Frame(mainWindow)

questions = StringVar()

radio_1 = Radiobutton(frame, text="", variable=questions, value="", tristatevalue="x")
radio_2 = Radiobutton(frame, text="", variable=questions, value="", tristatevalue="x")
radio_3 = Radiobutton(frame, text="", variable=questions, value="", tristatevalue="x")
radio_4 = Radiobutton(frame, text="", variable=questions, value="", tristatevalue="x")
radio_5 = Radiobutton(frame, text="", variable=questions, value="", tristatevalue="x")


btn = Button(frame, text="SUBMIT")

btn.pack(side=RIGHT, padx=5)
radio_1.pack(anchor="w")
radio_2.pack(anchor="w")
radio_3.pack(anchor="w")
radio_4.pack(anchor="w")
radio_5.pack(anchor="w")

frame.pack(padx=50, pady=50)
mainWindow.mainloop()
