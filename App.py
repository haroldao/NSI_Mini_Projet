#! Python 3.4
"""
Open a file dialog window in tkinter using the filedialog method.
Tkinter has a prebuilt dialog window to access files. 
This example is designed to show how you might use a file dialog askopenfilename
and use it in a program.
"""

from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename

root = Tk()

#This is where we lauch the file manager bar.
def OpenFile():
    name = askopenfilename(initialdir="C:\Users\Harold AO\Documents\Scolarité\Lycée\2.Première\NSI\MiniProjet\NSI_Mini_Projet\19b - Images Incrustées\Programmes",
                           filetypes =(("Text File", "*.txt"),("All Files","*.*")),
                           title = "Choisir un fichier."
                           )
    print (name)
    #Using try in case user types in unknown file or closes without choosing a file.
    try:
        with open(name,'r') as UseFile:
            print(UseFile.read())
    except:
        print("No file exists")


Title = root.title( "File Opener")
label = ttk.Label(root, text ="I'm BATMAN!!!",foreground="red",font=("Helvetica", 16))
label.pack()

#Menu Bar

menu = Menu(root)
root.config(menu=menu)

file = Menu(menu)

file.add_command(label = 'Open', command = OpenFile)
file.add_command(label = 'Exit', command = lambda:exit())

menu.add_cascade(label = 'File', menu = file)

root.mainloop()