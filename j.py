# importing everything from tkinter
from tkinter import *
 
# creating the tkinter window
Main_window = Tk()
 
# variable
my_text = "GeeksforGeeks updated !!!"
 
# function define for
# updating the my_label
# widget content
import tkinter
import tkinter.font
from tkinter import*
import csv
from PIL import ImageTk, Image



app= Tk()
app.title='Qui veut gagner des milions'
app["bg"]= "#0059b3"
app.geometry("10000x10000")
police_écriture = tkinter.font.Font(family='Lora', size= 20)
police_écriture2 = tkinter.font.Font(family='Lora', size= 15)

#Partie Algorithme

NSI = str('NSI.csv')

noms=[]
réponse_A=[]

with open('question.csv','r',newline='', encoding='utf-8-sig') as f :
 for ligne in f:
  ligne=ligne.replace("\n","")
  noms.append(ligne)

#Partie Interface

n=0

 

Can = Canvas(app, width=10000, height= 10000, bg="#0059b3")
fond=PhotoImage(file="fond2.png")
Can.create_image(140,100, anchor=NW, image=fond)
Can.place(x=150, y=0)


bonrep= 5+n*6

def Deux_Fonctions(*funcs):
    def Deux_Fonctions(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return Deux_Fonctions

def changeColor():  
    Réponse_A['bg'] = 'Red'

def Bonne_réponse():
    Réponse_A.place_forget()
    Réponse_B.place_forget()
    Réponse_C.place_forget()
    Réponse_D.place_forget()
    Can.place_forget()
    texte.pack_forget()
    correcte.place(x=530,y=100)
    LOGO.place(x=100, y=200)
    continuer.place(x=900, y=400)
    Question_suivante.place(anchor="center",x=1050, y=500)
    

def Mauvaise_réponse():
    Réponse_A.place_forget()
    Réponse_B.place_forget()
    Réponse_C.place_forget()
    Réponse_D.place_forget()
    Can.place_forget()
    texte.pack_forget()
    incorrecte.place(x=530,y=100)
    LOGO.place(x=100, y=200)
    quitter.place(x=900, y=400)
    Quitter.place(anchor="center",x=1050, y=500)
    reponse.place(x=450,y=200)
    
    
    
            

    
def BTNQuestion_suivante():
    Réponse_A.place(anchor="center", x=428, y=348)
    Réponse_B.place(anchor="center",x=878, y= 348)
    Réponse_C.place(anchor="center", x=428, y=458)
    Réponse_D.place(anchor="center", x=878, y=458)
    Question_suivante.place_forget()
    Can.place(x=0, y=6)
    texte.pack()
    correcte.place_forget()
    incorrecte.place_forget()
    LOGO.place_forget()
    continuer.place_forget()
    reponse.place_forget()
    


def BTNquitter():
 app.destroy()
    
REPONSEA=noms[1+n*6]
REPONSEB=noms[2+n*6]
REPONSEC=noms[3+n*6]
REPONSED=noms[4+n*6]

if REPONSEA==noms[bonrep]:
   pipou= Bonne_réponse
else:
   pipou= Mauvaise_réponse

if REPONSEB==noms[bonrep]:
   pipou1= Bonne_réponse
else:
   pipou1= Mauvaise_réponse

if REPONSEC==noms[bonrep]:
   pipou2= Bonne_réponse
else:
   pipou2= Mauvaise_réponse

if REPONSED==noms[bonrep]:
   pipou3= Bonne_réponse
else:
   pipou3= Mauvaise_réponse
    
Réponse_A = tkinter.Button(app, text=REPONSEA, bg="#0059b3",fg="white", activebackground="white", activeforeground="#0059b3", width=20, height=3, command=Deux_Fonctions(pipou, changeColor))
Réponse_B = tkinter.Button(app, text=REPONSEB, bg="#0059b3",fg="white", activebackground="white", activeforeground="#0059b3", width=20, height=3, command=pipou1)
Réponse_C = tkinter.Button(app, text=REPONSEC, bg="#0059b3",fg="white", activebackground="white", activeforeground="#0059b3", width=20, height=3, command=pipou2)
Réponse_D = tkinter.Button(app, text=REPONSED, bg="#0059b3",fg="white", activebackground="white", activeforeground="#0059b3", width=20, height=3, command=pipou3)
Question_suivante = tkinter.Button(app, text="Question suivante", bg="#0059b3",fg="white", activebackground="white", activeforeground="#0059b3", width=40, height=3, command = BTNQuestion_suivante)
Quitter=tkinter.Button(app, text="Quitter", bg="#0059b3",fg="white", activebackground="white", activeforeground="#0059b3", width=40, height=3, command = BTNquitter)


Réponse_A.place(anchor="center", x=550, y=348)
Réponse_B.place(anchor="center",x=1050, y= 348)
Réponse_C.place(anchor="center", x=550, y=458)
Réponse_D.place(anchor="center", x=1050, y=458)
Question_suivante.place_forget
Quitter.place_forget



texte = tkinter.Label(app, text=noms[0+n*6], wraplength = 50000, justify = "center",bg="#0059b3",fg="white")
texte['font']=police_écriture
texte.pack()

CORRECTE= "Bonne Réponse !"
correcte= tkinter.Label(app, text=CORRECTE, wraplength = 50000, justify = "center",bg="#0059b3",fg="white")
correcte['font']=police_écriture
correcte.place_forget()


CONTINUER= "Prêt(e) pour la question suivante ?"
continuer= tkinter.Label(app, text=CONTINUER, wraplength = 50000, justify = "center",bg="#0059b3",fg="white")
continuer['font']=police_écriture2
continuer.place_forget()

QUITTER= "Triste que vous nous quittiez déjà..."
quitter= tkinter.Label(app, text=QUITTER, wraplength = 50000, justify = "center",bg="#0059b3",fg="white")
quitter['font']=police_écriture2
quitter.place_forget()

INCORRECTE="Mauvaise Réponse !"
incorrecte= tkinter.Label(app, text=INCORRECTE, wraplength = 50000, justify = "center",bg="#0059b3",fg="white")
incorrecte['font']=police_écriture
incorrecte.place_forget()

REPONSE=f"La réponse correcte était la réponse {noms[bonrep]} "
reponse= tkinter.Label(app, text=REPONSE, wraplength = 50000, justify = "center",bg="#0059b3",fg="white")
reponse['font']=police_écriture2
reponse.place_forget()

logo= PhotoImage(file='logo2.png')
LOGO= Label(app, image=logo, background="#0059b3")
LOGO.place_forget()


print(noms[bonrep])


app.mainloop()








