from tkinter import *
from user import User

mainWindow = Tk()
mainWindow.title("Simple Quiz Application")
user = User(Username="", FirstName="", LastName="", Class="")

instructions = Label(mainWindow, text="Welcome to the simple quiz application")
instructions.pack(padx=20, pady=20)


actionsFrame = Frame(mainWindow)

log_in_btn = Button(actionsFrame, text="Log In", command=user.login)
log_in_btn.pack(side=RIGHT, padx=20, pady=10)

register_btn = Button(actionsFrame, text="Register", command=user.registerUser)
register_btn.pack(side=LEFT, padx=20, pady=10)

actionsFrame.pack()

mainWindow.mainloop()
