import random
import tkinter.font
from tkinter import *
import csv
from guizero import *
from PIL import ImageTk, Image

################# FONCTIONS #################

question_tab_enfant = []
reponseA_tab_enfant = []
reponseB_tab_enfant = []
reponseC_tab_enfant = []
reponseD_tab_enfant = []
bonneReponse_tab_enfant = []


with open('questions.csv', newline='', encoding='utf-8-sig') as csvfile:
    # ici, le séparateur est précisé grâce à "delimiter"
    fichier = csv.reader(csvfile, delimiter=';')
    # pour remplir notre tableau, une boucle for parcourant chaque ligne du fichier csv sera utilisée
    for ligne in fichier:
        # la première colonne du fichier csv est la colonne des questions
        question_tab_enfant.append(ligne[0])
        # la deuxième colonne du fichier csv est la colonne de la reponse a
        reponseA_tab_enfant.append(ligne[1])
        # la deuxième colonne du fichier csv est la colonne de la reponse b
        reponseB_tab_enfant.append(ligne[2])
        # la deuxième colonne du fichier csv est la colonne de la reponse c
        reponseC_tab_enfant.append(ligne[3])
        # la deuxième colonne du fichier csv est la colonne de la reponse d
        reponseD_tab_enfant.append(ligne[4])
        # la deuxième colonne du fichier csv est la colonne de la bonne reponse
        bonneReponse_tab_enfant.append(ligne[5])

indice = random.randint(0, len(question_tab_enfant) - 1)

def nouvelle_question():
    indice = random.randint(0, len(question_tab_enfant) - 1)
    question = question_tab_enfant[indice]
    reponseA = reponseA_tab_enfant[indice]
    reponseB = reponseB_tab_enfant[indice]
    reponseC = reponseC_tab_enfant[indice]
    reponseD = reponseD_tab_enfant[indice]
    bonneReponse = bonneReponse_tab_enfant[indice]
    supp_tableau(indice)
    return question, reponseA, reponseB, reponseC, reponseD, bonneReponse

def supp_tableau(indice):
    question_tab_enfant.pop(indice)
    reponseA_tab_enfant.pop(indice)
    reponseB_tab_enfant.pop(indice)
    reponseC_tab_enfant.pop(indice)
    reponseD_tab_enfant.pop(indice)
    bonneReponse_tab_enfant.pop(indice)

# def next_question():
#     question, reponseA, reponseB, reponseC, reponseD, bonneReponse = nouvelle_question()
#     question_depart.config = question
#     boutonA.value = reponseA
#     boutonB.value = reponseB
#     boutonC.value = reponseC
#     boutonD.value = reponseD

################# INITIALISATION #################

app = App(title="My app",
          width=1050,
          height=700,
          bg=("#99ddff"))

page1 = Box(app,
            width="fill",
            height="fill",
            layout="grid")

page2 = Box(app,
            width="fill",
            height="fill",
            )

page3 = Box(app,
            width="fill",
            height="fill",
            )

page2.hide()
page3.hide()

################# PAGE 1 #################

question_depart = nouvelle_question()

empty_box = Box(page1, width=250, height=75, grid=[0, 0])
boutons_gauche = Box(page1, layout="grid", grid=[1, 0])
middle = Box(page1, layout="grid", grid=[2, 0])
boutons_droite = Box(page1, layout="grid", grid=[3, 0])


texte = Label(middle.tk, text=question_depart[0], font=("Arial", 25), fg="black")
middle.add_tk_widget(texte, grid=[2, 0])

img = ImageTk.PhotoImage(Image.open("logo2.png"))
image_label = Label(middle.tk, image=img)
middle.add_tk_widget(image_label, grid=[2, 1])

Réponse_A = Button(boutons_gauche.tk, text=question_depart[1], bg="#0059b3", fg="white", activebackground="white",
                   activeforeground="#0059b3", width=20, height=3, command=lambda: print("Bonne réponse"))
boutons_gauche.add_tk_widget(Réponse_A, grid=[0, 0])

Réponse_B = Button(boutons_droite.tk, text=question_depart[2], bg="#0059b3", fg="white", activebackground="white",
                   activeforeground="#0059b3", width=20, height=3, command=lambda: print("Bonne réponse"))
boutons_droite.add_tk_widget(Réponse_B, grid=[0, 0])

Réponse_C = Button(boutons_gauche.tk, text=question_depart[3], bg="#0059b3", fg="white", activebackground="white",
                   activeforeground="#0059b3", width=20, height=3, command=lambda: print("Bonne réponse"))
boutons_gauche.add_tk_widget(Réponse_C, grid=[0, 1])

Réponse_D = Button(boutons_droite.tk, text=question_depart[4], bg="#0059b3", fg="white", activebackground="white",
                   activeforeground="#0059b3", width=20, height=3, command=lambda: print("Bonne réponse"))
boutons_droite.add_tk_widget(Réponse_D, grid=[0, 1])

Question_suivante = Button(middle.tk, text="Question suivante", bg="#0059b3", fg="white", activebackground="white",
                           activeforeground="#0059b3", width=40, height=3, command=next_question)
middle.add_tk_widget(Question_suivante, grid=[2, 3])


# fond=PhotoImage(file="fond2.png")
# Can.create_image(140,100, anchor=NW, image=fond)
# app.add_tk_widget(Can)

# def Bonne_réponse():
#     Réponse_A.place_forget()
#     Réponse_B.place_forget()
#     Réponse_C.place_forget()
#     Réponse_D.place_forget()
#     Can.place_forget()
#     texte.pack_forget()
#     correcte.place(x=530,y=100)
#     LOGO.place(x=100, y=200)
#     continuer.place(x=900, y=400)
#     Question_suivante.place(anchor="center",x=1050, y=500)


# def Mauvaise_réponse():
#     Réponse_A.place_forget()
#     Réponse_B.place_forget()
#     Réponse_C.place_forget()
#     Réponse_D.place_forget()
#     Can.place_forget()
#     texte.pack_forget()
#     incorrecte.place(x=530,y=100)
#     LOGO.place(x=100, y=200)
#     continuer.place(x=900, y=400)
#     Question_suivante.place(anchor="center",x=1050, y=500)
#     reponse.place(x=450,y=200)


# def BTNQuestion_suivante():
#     Réponse_A.place(anchor="center", x=428, y=348)
#     Réponse_B.place(anchor="center",x=878, y= 348)
#     Réponse_C.place(anchor="center", x=428, y=458)
#     Réponse_D.place(anchor="center", x=878, y=458)
#     Question_suivante.place_forget()
#     Can.place(x=0, y=6)
#     texte.pack()
#     correcte.place_forget()
#     incorrecte.place_forget()
#     LOGO.place_forget()
#     continuer.place_forget()
#     reponse.place_forget()


# Réponse_A.place(anchor="center", x=428, y=348)
# Réponse_B.place(anchor="center",x=878, y= 348)
# Réponse_C.place(anchor="center", x=428, y=458)
# Réponse_D.place(anchor="center", x=878, y=458)
# Question_suivante.place_forget

# TEXTE = "Quel age as tu ?"
# texte = tkinter.Label(app, text=TEXTE, wraplength = 50000, justify = "center",bg="#0059b3",fg="white")
# texte.pack()

# CORRECTE= "Bonne Réponse !"
# correcte= tkinter.Label(app, text=CORRECTE, wraplength = 50000, justify = "center",bg="#0059b3",fg="white")
# correcte.place_forget()

# CONTINUER= "Prêt(e) pour la question suivante ?"
# continuer= tkinter.Label(app, text=CONTINUER, wraplength = 50000, justify = "center",bg="#0059b3",fg="white")
# continuer.place_forget()

# INCORRECTE="Mauvaise Réponse !"
# incorrecte= tkinter.Label(app, text=INCORRECTE, wraplength = 50000, justify = "center",bg="#0059b3",fg="white")
# incorrecte.place_forget()

# REPONSE="La réponse correcte était la réponse B : 30 ans"
# reponse= tkinter.Label(app, text=REPONSE, wraplength = 50000, justify = "center",bg="#0059b3",fg="white")
# reponse.place_forget()

# logo= PhotoImage(file='logo2.png')
# LOGO= Label(app, image=logo, background="#0059b3")
# LOGO.place_forget()


app.display()
