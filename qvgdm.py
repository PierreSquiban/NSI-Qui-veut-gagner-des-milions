import random
import tkinter
import tkinter.font
from tkinter import *
import csv

paliers = [0, 100, 200, 300, 500, 1000, 2000, 4000, 8000,
           16000, 32000, 64000, 125000, 250000, 500000, 1000000]

score = 0

app = Tk()
app.title = "Qui veut gagner des milions"
app["bg"] = "#0059b3"
app.geometry("10000x10000")
police_écriture = tkinter.font.Font(family='Lora', size=20)
police_écriture2 = tkinter.font.Font(family='Lora', size=15)

# Partie Algorithme

question = []
reponseA = []
reponseB = []
reponseC = []
reponseD = []
bonneReponse = []


with open('question.csv', newline='', encoding='utf-8-sig') as csvfile:
    fichier = csv.reader(csvfile, delimiter=';')
    for ligne in fichier:
        question.append(ligne[0])
        reponseA.append(ligne[1])
        reponseB.append(ligne[2])
        reponseC.append(ligne[3])
        reponseD.append(ligne[4])
        bonneReponse.append(ligne[5])


# Partie Interface


Can = Canvas(app, width=10000, height=10000, bg="#0059b3")
fond = PhotoImage(file="fond2.png")
Can.create_image(140, 100, anchor=NW, image=fond)
Can.place(x=150, y=0)


def Bonne_réponse():
    global score
    score += 1
    if score == (len(paliers)-1):
        Réponse_A.place_forget()
        Réponse_B.place_forget()
        Réponse_C.place_forget()
        Réponse_D.place_forget()
        Can.place_forget()
        texte.pack_forget()
        correcte.place(x=530, y=100)
        LOGO.place(x=100, y=200)
        correcte.config(text=f"Bravo ! Vous avez gagné UN MILLION D'EUROS")
        Quitter.place(x=900, y=400)
    else:
        print(score)
        Réponse_A.place_forget()
        Réponse_B.place_forget()
        Réponse_C.place_forget()
        Réponse_D.place_forget()
        Can.place_forget()
        texte.pack_forget()
        correcte.place(x=530, y=100)
        LOGO.place(x=100, y=200)
        continuer.place(x=900, y=400)
        Question_suivante.place(anchor="center", x=1050, y=500)


def Mauvaise_réponse():
    global score
    Réponse_A.place_forget()
    Réponse_B.place_forget()
    Réponse_C.place_forget()
    Réponse_D.place_forget()
    Can.place_forget()
    texte.pack_forget()
    incorrecte.place(x=530, y=100)
    LOGO.place(x=100, y=200)
    quitter.place(x=900, y=400)
    Quitter.place(anchor="center", x=1050, y=500)
    reponse.place(x=450, y=200)
    incorrecte.config(text=f"Perdu ! vous repartez avec {paliers[score]} €")


def BTNQuestion_suivante():
    correcte.place_forget()
    incorrecte.place_forget()
    LOGO.place_forget()
    continuer.place_forget()
    reponse.place_forget()
    Réponse_A.place(anchor="center", x=428, y=348)
    Réponse_B.place(anchor="center", x=878, y=348)
    Réponse_C.place(anchor="center", x=428, y=458)
    Réponse_D.place(anchor="center", x=878, y=458)
    nouvelle_question = choix_question()
    texte.config(text=nouvelle_question[0])
    print(nouvelle_question[5], 'est la bonne réponse')
    Réponse_A.config(text=nouvelle_question[1], command=lambda: quand_clique(
        "A", nouvelle_question[5]))
    Réponse_B.config(text=nouvelle_question[2], command=lambda: quand_clique(
        "B", nouvelle_question[5]))
    Réponse_C.config(text=nouvelle_question[3], command=lambda: quand_clique(
        "C", nouvelle_question[5]))
    Réponse_D.config(text=nouvelle_question[4], command=lambda: quand_clique(
        "D", nouvelle_question[5]))
    Can.place(x=0, y=6)
    texte.pack()
    Question_suivante.place_forget()


def suppr(indice_suppr):
    question.pop(indice_suppr)
    reponseA.pop(indice_suppr)
    reponseB.pop(indice_suppr)
    reponseC.pop(indice_suppr)
    reponseD.pop(indice_suppr)
    bonneReponse.pop(indice_suppr)


def choix_question():
    indice = random.randint(0, len(question)-1)
    q = question[indice]
    rA = reponseA[indice]
    rB = reponseB[indice]
    rC = reponseC[indice]
    rD = reponseD[indice]
    bR = bonneReponse[indice]
    suppr(indice)
    return q, rA, rB, rC, rD, bR


def quand_clique(reponse_donnee, reponse_attendue):
    if reponse_donnee == reponse_attendue:
        Bonne_réponse()
    else:
        Mauvaise_réponse()


def BTNquitter():
    app.destroy()


question_texte = choix_question()

Réponse_A = tkinter.Button(app, text=question_texte[1], bg="#0059b3", fg="white", activebackground="white",
                           activeforeground="#0059b3", width=20, height=3, command=lambda: quand_clique("A", question_texte[5]))

Réponse_B = tkinter.Button(app, text=question_texte[2], bg="#0059b3", fg="white", activebackground="white",
                           activeforeground="#0059b3", width=20, height=3, command=lambda: quand_clique("B", question_texte[5]))

Réponse_C = tkinter.Button(app, text=question_texte[3], bg="#0059b3", fg="white", activebackground="white",
                           activeforeground="#0059b3", width=20, height=3, command=lambda: quand_clique("C", question_texte[5]))

Réponse_D = tkinter.Button(app, text=question_texte[4], bg="#0059b3", fg="white", activebackground="white",
                           activeforeground="#0059b3", width=20, height=3, command=lambda: quand_clique("D", question_texte[5]))

Question_suivante = tkinter.Button(app, text="Question suivante", bg="#0059b3", fg="white", activebackground="white",
                                   activeforeground="#0059b3", width=40, height=3, command=BTNQuestion_suivante)

Quitter = tkinter.Button(app, text="Quitter", bg="#0059b3", fg="white", activebackground="white",
                         activeforeground="#0059b3", width=40, height=3, command=BTNquitter)


Réponse_A.place(anchor="center", x=550, y=348)

Réponse_B.place(anchor="center", x=1050, y=348)

Réponse_C.place(anchor="center", x=550, y=458)

Réponse_D.place(anchor="center", x=1050, y=458)

Question_suivante.place_forget

Quitter.place_forget


texte = tkinter.Label(
    app, text=question_texte[0], wraplength=50000, justify="center", bg="#0059b3", fg="white")
texte['font'] = police_écriture
texte.pack()

CORRECTE = "Bonne Réponse !"
correcte = tkinter.Label(app, text=CORRECTE, wraplength=50000,
                         justify="center", bg="#0059b3", fg="white")
correcte['font'] = police_écriture
correcte.place_forget()


CONTINUER = "Prêt(e) pour la question suivante ?"
continuer = tkinter.Label(app, text=CONTINUER, wraplength=50000,
                          justify="center", bg="#0059b3", fg="white")
continuer['font'] = police_écriture2
continuer.place_forget()

QUITTER = "Triste que vous nous quittiez déjà..."
quitter = tkinter.Label(app, text=QUITTER, wraplength=50000,
                        justify="center", bg="#0059b3", fg="white")
quitter['font'] = police_écriture2
quitter.place_forget()

INCORRECTE = "Mauvaise Réponse !"
incorrecte = tkinter.Label(
    app, text=INCORRECTE, wraplength=50000, justify="center", bg="#0059b3", fg="white")
incorrecte['font'] = police_écriture
incorrecte.place_forget()

REPONSE = f"La réponse correcte était la réponse {question_texte[5]} "
reponse = tkinter.Label(app, text=REPONSE, wraplength=50000,
                        justify="center", bg="#0059b3", fg="white")
reponse['font'] = police_écriture2
reponse.place_forget()

logo = PhotoImage(file='logo2.png')
LOGO = Label(app, image=logo, background="#0059b3")
LOGO.place_forget()


app.mainloop()
