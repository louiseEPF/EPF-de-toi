# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 16:31:05 2020

@author: louis_000
"""




from tkinter import *
import random

#creation de la fenetre ou se deroule le jeu
fenetre = Tk()

fenetre.title("♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥   Jeu EPF de toi  ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥") #, fg='navy')

# Définir la taille de la fenêtre
global largeur_ecran
largeur_ecran=fenetre.winfo_screenwidth()
global hauteur_ecran
hauteur_ecran=fenetre.winfo_screenheight()
global pourcentage
pourcentage=0.8
fenetre.geometry("%dx%d+0+0" %(largeur_ecran*pourcentage,hauteur_ecran*pourcentage))

fenetre.configure(bg="pink")

# Ajouter un bouton Quitter en bas de la fenêtre
Bouton_quitter=Button(fenetre, text="Fermer la fenêtre",bg='pink', fg='navy', command=fenetre.destroy)
Bouton_quitter.place(x=(largeur_ecran-145)*pourcentage, y=(hauteur_ecran-50)*pourcentage)
#Bouton_quitter.grid(row=300, column=300)






#les label sont les equivalents de print pour tkinter
label = Label(fenetre, text="MYTHIC")
# .pack() sert à afficher l'element dans la fenetre sinon on ne voit pas
label.pack()

                 
                    
#DONNEES
                 
                 
###PHOTO POUR CHAQUE PERSO                
Photo1 = PhotoImage(file="Sasuke.png").zoom(35).subsample(32)

Photo2=PhotoImage(file="Sakura.png") .zoom(35).subsample(32)

#tableaux des caracteristiques visibles des persos
M="Homme"
F="Femme"
X="Homme et Femme"
Sasuke_caractere=[0.1,0.1,0.7,0.1]
Sakura_caractere=[0.1,0.1,0.7,0.1]

Sasuke=[Photo1,M,18,"ninja","Paraît distant mais a un grand coeur","Sasuke",Sasuke_caractere,0]
Sakura=[Photo2,F,18,"ninja","Très gentille et empathique","Sakura",Sakura_caractere,0]






tab2tab=[Sasuke,Sakura]



def Choisir_Personnage():
    
    sexe_choisi=var_choix.get()
    
    frame_depart.destroy()
    
    
    
#    #les frames de la fenetre sont des blocs ou tu peux grouper du texte,des images,etc
#    #les frames sont independantes les unes des autres 
#    ###FRAME DES PERSONNAGES
    global Frame1
    Frame1 = Frame(fenetre, bg="pink", cursor = "heart")
    #Frame(fenetre, borderwidth=2, relief=GROOVE)

    Frame1.pack()
#    while w != 1:
#        a=Tirage()
#    #les canvas contiennent et animent les images
#    ###PHOTO PERSONNAGE (DANS LA FRAME)
#    
    canvas1 = Canvas(Frame1, width=100, height=100, background="#FFFFFF")
##  
   # if choix_crush==0:
    if sexe_choisi=="Homme":
        var1=random.randint(0,1)
    elif sexe_choisi=="Femme":
        var1=random.randint(0,1)
    elif sexe_choisi=="Homme et Femme":
        var1=random.randint(0,1)
    #solution secours:
    #var1=random.randint(0,1)
##            
    global perso_propose  
    perso_propose=tab2tab[var1]
    Photo_visible=canvas1.create_image(50,290,image=perso_propose[0])
    canvas1.pack()
    
    global match
    match=IntVar()

    Label(Frame1, text=perso_propose[4]).pack(padx=10, pady=10)
    Label(Frame1, text="Voulez-vous commencer à discuter avec "+perso_propose[5]+" ?").pack(padx=10, pady=10)
    bouton_oui = Radiobutton(Frame1, text="oui",variable=match,value=1)
    bouton_non = Radiobutton(Frame1, text="non",variable=match,value=0)
    bouton_valider2=Button(Frame1, text="Valider", font=("Tahoma", 12), bg="#BE2121", fg ="white" , width=20,command=Suite)

    bouton_oui.pack()
    bouton_non.pack()
    bouton_valider2.pack()
    
        
      
            

def Suite() :
    
    choix_crush=match.get()
            
    if choix_crush==1:
        Frame1.destroy()
        passage=Etape2(perso_propose)

 
 
def Etape2(perso_propose):
    global Frame2
    Frame2= Frame(fenetre, bg="pink", cursor = "heart")
    #Frame(fenetre)
    Frame2.pack()
    canvas2 = Canvas(Frame2, width=200, height=200, background="#FFFFFF")
    Photo_date=canvas2.create_image(30,290,image=perso_propose[0])
    canvas2.pack()
    
    Label(Frame2, text="Salut!J'avais hâte de te parler. J'ai envie de mieux te connaître.").pack(padx=10, pady=10)
    
    
    var_quest=0
    
    global i
    i=0
    global Frame_questions
    Frame_questions=Frame(fenetre)
    Frame_questions.pack() 
    global points
    points=0

    for i in range(0,1):# le rang est le nombre de quests limite
        quest=Questions()
        
        
def Questions() :      
    Frame_questions= Frame(fenetre, bg="pink", cursor = "heart")
    #Frame(fenetre)
    Frame_questions.pack()    
        
    var_quest=random.randint(0,2)
        
    nouvelle_question=open("question"+str(var_quest)+".txt","r", encoding="utf8")
    texte_question=nouvelle_question.readline()
    Label(Frame2, text=texte_question).pack(padx=10, pady=10)
        
    global var_date
    var_date=IntVar()
        
    Reponse0=Radiobutton(Frame_questions, text=nouvelle_question.readline(), variable=var_date, value=0)
    Reponse1=Radiobutton(Frame_questions, text=nouvelle_question.readline(), variable=var_date, value=1)    
    Reponse2=Radiobutton(Frame_questions, text=nouvelle_question.readline(), variable=var_date, value=2)
    Reponse3=Radiobutton(Frame_questions, text=nouvelle_question.readline(), variable=var_date, value=3)
        
    Reponse0.pack()
    Reponse1.pack()
    Reponse2.pack()
    Reponse3.pack()
        
    Valider3=Button(Frame_questions, text="Valider", font=("Tahoma", 12), bg="#BE2121", fg ="white" , width=20)
    Valider3.pack()
                        
#def Compteur() :
#    Frame_questions.destroy()
#    
#    chance=var_date.get()
#    if chance==perso_propose[7]:
#        points=1+points
#    if points==5:
#        print(bon)
    

       
###DEPART
def Depart() : 
    global frame_depart
    
    
    frame_depart = Frame(fenetre, bg="pink", cursor = "heart")
    frame_depart.place(x=0, y=0)
    frame_depart.pack()
    
    
    Label(frame_depart, text="Qui vous intéresse ?").pack()
    
    
    global var_choix
    var_choix = StringVar()
    
    choix_femme = Radiobutton(frame_depart,anchor=E, text=F, bg="pink",variable=var_choix, value=F)
    choix_femme.place(x=50, y=50)
    choix_femme.select()
    
    choix_homme = Radiobutton(frame_depart, text=M, bg="pink",variable=var_choix, value=M)
    choix_homme.place(x=50, y=80)
    
    
    
    choix_les2 = Radiobutton(frame_depart, text=X, bg="pink", variable=var_choix, value=X)
    choix_les2.place(x=50, y=110)


    choix_femme.pack()
    choix_homme.pack()
    choix_les2.pack()
    
    bouton_valider = Button(frame_depart, text="Valider", font=("Tahoma", 12), bg="#BE2121", fg ="black" , width=20, command=Choisir_Personnage)
    bouton_valider.place(x=50, y=140)
        
    #bouton_valider = Button(frame_depart, text="Valider", font=("Tahoma", 12), bg="#BE2121", fg ="white" , width=20,command=Choisir_Personnage)
    bouton_valider.pack()
    
    



Commencer=Depart()


fenetre.mainloop()
               

               
               
               
               
