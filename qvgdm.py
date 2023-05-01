import tkinter
import tkinter.font
from tkinter import*

app= tkinter.Tk()
app.title='Qui veut gagner des milions'
app["bg"]= "#0059b3"
app.geometry("10000x10000")
police_écriture = tkinter.font.Font(family='Lora', size= 20)
police_écriture2 = tkinter.font.Font(family='Lora', size= 15)

#Partie Algorithme

noms=[]
with open('nsi.txt','r') as f :
 for ligne in f:
  ligne=ligne.replace("\n","")
  noms.append(ligne)
  print(noms)
  

#Partie Interface

Can = Canvas(app, width=5000, height= 2500, bg="#0059b3")
fond=PhotoImage(file="fond2.png")
Can.create_image(140,100, anchor=NW, image=fond)
Can.place(x=0, y=6)


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
    continuer.place(x=900, y=400)
    Question_suivante.place(anchor="center",x=1050, y=500)
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
             
    

    
Réponse_A = tkinter.Button(app, text="15 ans", bg="#0059b3",fg="white", activebackground="white", activeforeground="#0059b3", width=20, height=3, command=Mauvaise_réponse)
Réponse_B = tkinter.Button(app, text="30 ans", bg="#0059b3",fg="white", activebackground="white", activeforeground="#0059b3", width=20, height=3, command=Bonne_réponse)
Réponse_C = tkinter.Button(app, text="115 ans", bg="#0059b3",fg="white", activebackground="white", activeforeground="#0059b3", width=20, height=3, command=Mauvaise_réponse)
Réponse_D = tkinter.Button(app, text= noms[0], bg="#0059b3",fg="white", activebackground="white", activeforeground="#0059b3", width=20, height=3, command=Mauvaise_réponse)
Question_suivante = tkinter.Button(app, text="Question suivante", bg="#0059b3",fg="white", activebackground="white", activeforeground="#0059b3", width=40, height=3, command = BTNQuestion_suivante)

Réponse_A.place(anchor="center", x=428, y=348)
Réponse_B.place(anchor="center",x=878, y= 348)
Réponse_C.place(anchor="center", x=428, y=458)
Réponse_D.place(anchor="center", x=878, y=458)
Question_suivante.place_forget

TEXTE = "Quel age as tu ?"
texte = tkinter.Label(app, text=TEXTE, wraplength = 50000, justify = "center",bg="#0059b3",fg="white")
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

INCORRECTE="Mauvaise Réponse !"
incorrecte= tkinter.Label(app, text=INCORRECTE, wraplength = 50000, justify = "center",bg="#0059b3",fg="white")
incorrecte['font']=police_écriture
incorrecte.place_forget()

REPONSE="La réponse correcte était la réponse B : 30 ans"
reponse= tkinter.Label(app, text=REPONSE, wraplength = 50000, justify = "center",bg="#0059b3",fg="white")
reponse['font']=police_écriture2
reponse.place_forget()

logo= PhotoImage(file='logo2.png')
LOGO= Label(app, image=logo, background="#0059b3")
LOGO.place_forget()



app.mainloop()




