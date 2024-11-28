from tkinter import *
from tkinter import messagebox
import os


class User:

    def __init__(self, Username, FirstName, LastName, Class):
        self.Username = Username
        self.FirstName = FirstName
        self.LastName = LastName
        self.Class = Class

    def registerUser(self):
        mainWindow = Tk()
        mainWindow.title("User Registration")

        fnFrame = Frame(mainWindow)
        fnLabel = Label(fnFrame, text="First Name")
        fnEntry = Entry(fnFrame)

        fnLabel.pack(side=LEFT)
        fnEntry.pack(side=RIGHT)
        fnFrame.pack(padx=20, pady=10)

        lnFrame = Frame(mainWindow)
        lnLabel = Label(lnFrame, text="Last Name")
        lnEntry = Entry(lnFrame)

        lnLabel.pack(side=LEFT)
        lnEntry.pack(side=RIGHT)
        lnFrame.pack(padx=20, pady=10)

        # reg_btn = Button(mainWindow, text="REGISTER", command=register)
        # reg_btn.pack(padx=20, pady=10)

        def register():
            self.FirstName = fnEntry.get()
            self.LastName = lnEntry.get()
            userFile = open(f"{self.LastName}.txt", "w")
            userFile.close()
            messagebox.showinfo("Success", f"Welcome {self.LastName}!")

        reg_btn = Button(mainWindow, text="REGISTER", command=register)
        reg_btn.pack(padx=20, pady=10)

    def login(self):
        mainWindow = Tk()
        mainWindow.title("User Login")

        fnFrame = Frame(mainWindow)
        fnLabel = Label(fnFrame, text="First Name")
        fnEntry = Entry(fnFrame)

        fnLabel.pack(side=LEFT)
        fnEntry.pack(side=RIGHT)
        fnFrame.pack(padx=20, pady=10)

        lnFrame = Frame(mainWindow)
        lnLabel = Label(lnFrame, text="Last Name")
        lnEntry = Entry(lnFrame)

        lnLabel.pack(side=LEFT)
        lnEntry.pack(side=RIGHT)
        lnFrame.pack(padx=20, pady=10)

        def verify_login():
            self.FirstName = fnEntry.get()
            self.LastName = lnEntry.get()
            userFile = f"{self.LastName}.txt"

            if os.path.exists(userFile):
                messagebox.showinfo(
                    "Login Successful",
                    f"Welcome back, {self.FirstName}{self.LastName}!",
                )
            else:
                messagebox.showerror(
                    "Login Unsuccessful", "User not found. Please try again"
                )

        log_in_btn = Button(mainWindow, text="LOG IN", command=verify_login)
        log_in_btn.pack(padx=20, pady=10)
