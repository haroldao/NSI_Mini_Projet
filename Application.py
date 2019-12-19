from tkinter import *
import sys, os

#FENETRE
window = Tk()
window.title("ARTHUR - HAROLD | NSI Mini-Projet 2019")
window.geometry("800x400")
window.eval('tk::PlaceWindow . center')

#MAIN Text
mainText= Label(window, text='Projet réalisé pour le Mini-Projet d\'NSI', font=('Nexa Light', 20))
mainText.grid()
mainText.config(anchor=SW)   


#Sub Text 1

TextOne= Label(window, text='Evolution 1', font=('Arial Bold', 20))
TextOne.grid()

def OpenFILE():
    os.system('python ./19a-Images_Tatouées\Programmes\Mini_Projet_Evolution_1.py')
OpenButton=Button(text="Button", command= OpenFILE())
OpenButton.grid()

# #RADIO Button

# selected = IntVar()
 
# rad1 = Radiobutton(window,text='Principale', value=1, variable=selected)
# rad1.grid(column=1, row=3)
 
# rad2 = Radiobutton(window,text='Evolution 1', value=2, variable=selected)
# rad2.grid(column=2, row=3)
 
# rad3 = Radiobutton(window,text='Evolution 2', value=3, variable=selected)
# rad3.grid(column=3, row=3)

# def clicked():
 
#    print(selected.get())
 
# btn = Button(window, text="Selectionner..", command=clicked)
# btn.grid(column=4, row=3)
 
window.mainloop()
