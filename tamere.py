from guizero import *
from tkinter import *
import time
import csv
import random
from PIL import ImageTk, Image
from winsound import *
#### Message in the terminal ####



### End of the message ###

paliers = [0, 100, 200, 300, 500, 1000, 2000, 4000, 8000,
           16000, 32000, 64000, 125000, 250000, 500000, 1000000]
score = 0

# Il faut qu'on mette des dicos et qu'on mette les bons indices

n_questions_enfant = []
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


def click_button_adult():
    print("adult")


def choix_question_adult(a):
    pass


def randomtamere_adult():
    pass


def child_mode():
    frame_page_1.hide()
    frame_page_2.show()


# Affichage du tableau


#####################        Start App        ######################

app = App(title="My app",
          width=1050,
          height=700,
          bg=("#99ddff"))

frame_page_1 = Box(app,
                   width="fill",
                   height="fill")

frame_page_2 = Box(app,
                   width="fill",
                   height="fill",
                   )

frame_page_3 = Box(app,
                   width="fill",
                   height="fill",
                   )

frame_answer_good = Box(app, width="fill", height="fill")
frame_answer_bad = Box(app, width="fill", height="fill")

frame_page_2.hide()
frame_answer_good.hide()
frame_answer_bad.hide()
frame_page_3.hide()


################# PAGE 1 #################
empty_frame_page_1 = Box(frame_page_1,
                         layout="grid",
                         width=100,
                         height=75)

frame_text_page_1 = Box(frame_page_1,
                        layout="grid")

empty_frame_2_page_1 = Box(frame_page_1,
                           layout="grid",
                           width=100,
                           height=100)

frame_buttons_page_1 = Box(frame_page_1,
                           layout="grid")

text = Label(frame_text_page_1.tk,
             text="Qui veut gagner des millions ?",
             font=("Arial", 25),
             fg="black")

app.add_tk_widget(text)

empty_text_3 = Label(frame_text_page_1.tk,
                     text="",
                     font=("Arial", 15),
                     height=2)
app.add_tk_widget(empty_text_3)

img = ImageTk.PhotoImage(Image.open("fond2.png"))
image_label = Label(frame_text_page_1.tk, image=img)
app.add_tk_widget(image_label)

button_child = Button(frame_buttons_page_1.tk,
                      text="Mode Enfant",
                      cursor="hand2",
                      font=("Arial", 15),
                      fg="black",
                      padx=10,
                      relief="groove",
                      command=lambda:print("enfant"))

frame_buttons_page_1.add_tk_widget(button_child,
                                   grid=[0, 0])

empty_text = Label(frame_buttons_page_1.tk,
                   text="",
                   font=("Arial", 15))

frame_buttons_page_1.add_tk_widget(empty_text,
                                   grid=[1, 0],
                                   width=10)

button_adult = Button(frame_buttons_page_1.tk,
                      text="Mode Adulte",
                      cursor="hand2",
                      font=("Arial", 15),
                      fg="black",
                      padx=10,
                      relief="groove",
                      command=lambda:print("adult"))

frame_buttons_page_1.add_tk_widget(button_adult,
                                   grid=[2, 0])


app.display()
