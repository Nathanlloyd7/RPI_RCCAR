import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sys

class RCMenuBar(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)
        fileMenu = tk.Menu(self, tearoff=0)
        self.add_cascade(label="File",underline=0, menu=fileMenu)
        fileMenu.add_command(label="Control Settings",underline=0, command = self.controlSetting)
        fileMenu.add_command(label="Motor Settings",underline=0, command = self.motorSetting)
        fileMenu.add_command(label="Password Settings",underline=0, command = self.passSetting)
        fileMenu.add_command(label="Fun Settings",underline=0, command = self.funSetting)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", underline=1, command=self.quit)
        helpMenu = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Help", menu = helpMenu, underline=0)
        helpMenu.add_command(label="About", underline=0, command = self.about)
        #keyboard shortcuts
        self.bind_all("<Control-a>", self.about)
        self.bind_all("<Control-c>", self.controlSetting)
        self.bind_all("<Control-m>", self.motorSetting)

# ------------------------ Quit Menu Item ------------------------

    def quit(self):
        print("Exit")
        try:
            #self.parent.destroy() #destroys the menu not all windows, need to sort this
            sys.exit(0)
        except:
            print(sys.exc_info()[0])


# ------------------------ About Menu Item ------------------------
    def about(self):
        messagebox.showinfo("About", """Hello, welcome to this RC application\n
        This application will function as a minature version of a real full size car, giving the user the ability to control it using GUI or keyboard inputs as well as toggle assistive driving technologies:\n
        If you have any questions please contact N Lloyd here:\n P16187037@my365.dmu.ac.uk""")

# ------------------------ Vehicle Control Menu Item's and Methods ------------------------
    def controlSetting(self):  #will allow customization
        controlSet = Toplevel()
        controlSet.title("Control Panel")
        controlSet.minsize(300,300)
        Label(controlSet, text="This is the Control Page\n Here you can switch between kyboard, UI, controller perhaps").grid(row=0, column=1, padx=10, pady=2)
        controlSet.mainloop()


# ------------------------ Password Change Menu Item's and Methods ------------------------

    def passSetting(self):  #will allow customization
        global passSet #so it can be destroyed
        passSet = Toplevel()
        passSet.title("Control Panel")
        passSet.minsize(300,300)

        passSetsFile = open("/Settings/passSetting.txt", "r")
        loadedPass = passSetsFile.readline()
        print(loadedPass)
        print(type(loadedPass))

        passSettingFrame = Frame(passSet, width=200, height=10, borderwidth=1)
        passSettingFrame.grid(row=1, column=0, padx=10, pady=2)
        Label(passSet, text="This is the password Page\n here you can change password settins and logon").grid(row=0, column=0, padx=10, pady=2)
        pwNum1 = Button(passSettingFrame, text="1", command = lambda : self.addtoPW(str(1))).grid(row=0, column=0, padx=10, pady=2)
        pwNum2 = Button(passSettingFrame, text="2", command = lambda : self.addtoPW(str(2))).grid(row=0, column=1, padx=10, pady=2)
        pwNum3 = Button(passSettingFrame, text="3", command = lambda : self.addtoPW(str(3))).grid(row=0, column=2, padx=10, pady=2)
        pwNum4 = Button(passSettingFrame, text="4", command = lambda : self.addtoPW(str(4))).grid(row=0, column=3, padx=10, pady=2)
        global newPWLog
        newPWLog = Text(passSet, width = 20, height = 2, takefocus=0)
        newPWLog.grid(row=4, column=0, padx=10, pady=2)
        #newPWLog.insert(0.0,"Enter Password: ")
        Label(passSet, text="Enter Password").grid(row=3, column=0, padx=10, pady=2)
        passSetFinal = Frame(passSet, width=200, height=10, borderwidth=1)
        passSetFinal.grid(row=5, column=0, padx=10, pady=2)
        clearPW = Button(passSetFinal, text="Clear", command = self.clearPW).grid(row=0, column=0, padx=10, pady=2)
        submitPW = Button(passSetFinal, text="Submit", command = self.savePass).grid(row=0, column=1, padx=10, pady=2)

        passSetsFile.close()
        passSet.mainloop()


    def savePass(self):
        passSetsFile = open("/Settings/passSetting.txt", "w")
        #newPin = str(1113)
        newPin = newPWLog.get(0.0,END)


        passSetsFile.write(str(newPin))
        print(newPin)
        passSetsFile.close()
        passSet.destroy()

    def addtoPW(self, pwNum):
        newPWLog.insert(END, pwNum)
        print(pwNum)

    def clearPW(self):
        newPWLog.delete(0.0,END)







# ------------------------ Fun Settings Menu Item's and Methods ------------------------
    def funSetting(self):  #will allow customization
        funSet = Toplevel()
        funSet.title("Control Panel")
        funSet.minsize(300,300)
        Label(funSet, text="This is the Fun Page\n here you can change fun effects for the vehicle").grid(row=0, column=1, padx=10, pady=2)
        funSet.mainloop()


# ------------------------ Motor Speed Lock Menu Item and Methods ------------------------
    def loadMotSettings(self):
        motorSetsFile = open("/Settings/motorSetting.txt", "r") #current setup lets you save to a doc but not show in a log or print in??
        loadedVar = motorSetsFile.read(1)
        return loadedVar
        motorSetsFile.close()


    def saveMotor(self, ):
        motorSetsFile = open("/Settings/motorSetting.txt", "w")
        if selected.get() == 1:
            print("You have selected : "+ str(selected.get()) + ": Manual speed is ON")
            motorSetsFile.write(str(selected.get()))
            motorSetsFile.close()
            motorSet.destroy()
        elif selected.get() == 0:
            print("You have selected : "+ str(selected.get()) + ": Manual speed is OFF")
            motorSetsFile.write(str(selected.get()))
            motorSetsFile.close()
            motorSet.destroy()
        else:
            print("Something went wrong")
            motorSetsFile.close()
            motorSet.destroy()


    def motorSetting(self):                             #enables user to lock speed.
        loadedVar = self.loadMotSettings()
        global motorSet # so it can be destroyed
        motorSet = Toplevel()
        motorSet.title("Motor Control Panel")
        motorSet.minsize(300,300)
        Label(motorSet, text="Here you can toggle whether manual speed control is active").grid(row=0, column=0, padx=10, pady=2)
        Label(motorSet, text=" ").grid(row=1, column=1, padx=10, pady=2)
        Label(motorSet, text="Would you like to toggle manual speed?:").grid(row=2, column=0, padx=10, pady=2) #replace 'off' with a loaded in var %
        motorFrame = Frame(motorSet, width=200, height=10, borderwidth=1)
        motorFrame.grid(row=3, column=0, padx=10, pady=2)
        global selected
        selected = IntVar()
        radioOn = Radiobutton(motorFrame, text="On", value=1, variable=selected).grid(row=0, column=0, padx=10, pady=2)
        radioOff = Radiobutton(motorFrame, text="Off",value=0, variable=selected).grid(row=0, column=1, padx=10, pady=2)
        saveLock = Button(motorSet, text="Save", command = self.saveMotor).grid(row=4, column=0, padx=10, pady=2)
        stateLog = Text(motorSet, width = 20, height = 2, takefocus=0)
        stateLog.grid(row=5, column=0, padx=10, pady=2)
        stateLog.insert(0.0,"1 is On, 0 is Off\nCurrent state: " + loadedVar)
        motorSet.mainloop()

    def noSpeed(self):
        print("Speed Toggle Disabled\n Modify in Motor Settings")