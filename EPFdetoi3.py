# -*- coding: utf-8 -*-
"""
Created on Mon May 11 09:15:47 2020

@author: louis_000
"""

# -*- coding: utf-8 -*-
"""
Created on Mon May 11 07:46:46 2020

@author: louis_000
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 16:31:05 2020
@author: Florane_000
"""

#tkinter est tres specifique donc je te mets
#plein de commentaires pour que tu comprennes bien 
#ce que j'ai fait



from tkinter import *
import random
import time

def CommandeChoixOui(FrameEtape1_2):
    #global PersonnagePropose
    FrameEtape1_2.destroy()
    Etape2_1(PersonnagePropose,var_quest,var_date,points)


def CommandeChoixNon(FrameEtape1_2, canvas1, ListePersonnagePossible, BoutonValider1_2_Non,PersonnagePropose):
    #global PersonnagePropose
    # Vérifier si il existe encore des  personnages
    if len(ListePersonnagePossible) != 0:
        ChoisirAleatoirementPersonnage(ListePersonnagePossible)
        AfficherPersonnage(FrameEtape1_2, canvas1, PersonnagePropose,Photo_visible)
    else:   
        Label(FrameEtape1_2, text="C'était le dernier choix !!!", bg="pink").place(x=0, y=180) 
        BoutonValider1_2_Non['state']=DISABLED
    
    
def ChoisirAleatoirementPersonnage(ListePersonnagePossible):
    #global PersonnagePropose
    # On choisit au hasard un indice de personnage dans la liste de ceux qui répondent aux critères
    IndicePersonnagePropose = random.choice(ListePersonnagePossible)
    # On supprime 'indice sélectionné de la liste de ceux qui répondent aux critères
    ListePersonnagePossible.remove(IndicePersonnagePropose)            
    # On récupère toutes les caractéristiques du personnage dans la variable PersonnagePropose 
    global PersonnagePropose
    PersonnagePropose=ListePersonnage[IndicePersonnagePropose]              
    
    
def AfficherPersonnage(FrameEtape1_2, canvas1, PersonnagePropose,Photo_visible):
    # Effacer la photo
    #global Photo_visible
    if Photo_visible!=0:
        canvas1.delete(Photo_visible)    
    # Afficher la photo
    Photo_visible=canvas1.create_image(50,290,image=PersonnagePropose[0])
    canvas1.place(x=0, y=0) 
    Label(FrameEtape1_2, text="                                                                                                               ", bg="pink").place(x=0, y=120)
    Label(FrameEtape1_2, text=PersonnagePropose[4], bg="pink").place(x=0, y=120)
    Label(FrameEtape1_2, text="                                                                                                               ", bg="pink").place(x=0, y=150)
    Label(FrameEtape1_2, text="Voulez-vous commencer à discuter avec "+ PersonnagePropose[5] +" ?", bg="pink").place(x=0, y=150)

 
def Etape2_1(PersonnagePropose,var_quest,var_date,points):    
   
    
    for c in root.winfo_children():
        c.pack_forget()
    
    score=Compteur(points, var_date,PersonnagePropose)
    
    Frame2= Frame(root, bg="pink", cursor = "heart")
    #Frame(fenetre)
    Frame2.pack()
    canvas2 = Canvas(Frame2, width=200, height=200, background="#FFFFFF")
    Photo_date=canvas2.create_image(30,290,image=PersonnagePropose[0])
    canvas2.pack()
    
  
    Frame_questions=Frame(root)
    Frame_questions.pack() 
    

    #for i in range(0,1):# le rang est le nombre de quests limite
    if score<1:
        quest=Questions(var_quest,Frame_questions,Frame2)
        
    if score==1:
        Frame_RDV=Frame(root,bg="pink", cursor = "heart")
        Frame_RDV.pack()
        RDV=Label(Frame_RDV, text= "Vous êtes très proches. Concluez! ♥ ", bg="pink")
        RDV.pack() 
        Date=Button(Frame2, text="Décrocher une date", width=10, bg='pink', fg='navy')
        Date.pack()
        
def Questions(var_quest,Frame_questions,Frame2) :      
    Frame_questions= Frame(root, bg="pink", cursor = "heart")
    
    Frame_questions.pack()    
        
    var_quest=var_quest+1
        
    nouvelle_question=open("question"+str(var_quest)+".txt","r", encoding="utf8")
    texte_question=nouvelle_question.readline()
    Label(Frame2, text=texte_question).pack(padx=10, pady=10)
        
    
    
        
    Reponse0=Radiobutton(Frame_questions, text=nouvelle_question.readline(), variable=var_date, value=0)
    Reponse1=Radiobutton(Frame_questions, text=nouvelle_question.readline(), variable=var_date, value=1)    
    Reponse2=Radiobutton(Frame_questions, text=nouvelle_question.readline(), variable=var_date, value=2)
    Reponse3=Radiobutton(Frame_questions, text=nouvelle_question.readline(), variable=var_date, value=3)
        
    Reponse0.pack()
    Reponse1.pack()
    Reponse2.pack()
    Reponse3.pack()
        
    Valider3=Button(Frame_questions, text="Valider", font=("Tahoma", 12), bg="#BE2121", fg ="white" , width=20, command=lambda: Etape2_1(PersonnagePropose,var_quest,var_date,points))
    Valider3.pack()
    
    
def Compteur(points, var_date,PersonnagePropose) :
    
    chance=var_date.get()
    humeur=2
    if PersonnagePropose[6][chance]==PersonnagePropose[6][humeur]:
        if 0.3<PersonnagePropose[6][chance]:
            points=1+points
    return points    

#def Etape3():
    
    
    
# Procédure pour déterminer le personnage
def Etape1_2(VarChoixSexe,FrameEtape1_1):
    
    sexe_choisi=VarChoixSexe.get()
    
    FrameEtape1_1.destroy()
    
    # Ouverture la fenêtre   
    FrameEtape1_2 = Frame(root, width=1200, height=600, bd=250, bg="pink", cursor = "heart")
    #FrameEtape1_2.pack(expand=YES)
    FrameEtape1_2.place(x=0, y=0)
   
    canvas1 = Canvas(FrameEtape1_2, width=100, height=100, background="pink")
    
    # La table ListePersonnagePossible va contenir tous les indices des personnages qui répondent aux critères 
    ListePersonnagePossible=[]
    for Indice in range(0, len(ListePersonnage)):
        if ListePersonnage[Indice][1]==sexe_choisi or sexe_choisi==X:
            ListePersonnagePossible.append(Indice)
    
    #PersonnagePropose=[]
    ChoisirAleatoirementPersonnage(ListePersonnagePossible)
    
    AfficherPersonnage(FrameEtape1_2, canvas1, PersonnagePropose,Photo_visible)

    # ATTENTION QUAND ON PASSE UNE COMMANDE AVEC DES ARGUMENTS PYTHON EXECUTE IMMEDIATEMENT LA COMMANDE. IL FAUT METTRE lambda:
    BoutonValider1_2_Oui = Button(FrameEtape1_2, text="Oui", width=10, bg='pink', fg='navy', command=lambda: CommandeChoixOui(FrameEtape1_2))
    BoutonValider1_2_Oui.place(x=0, y=230)
    
    BoutonValider1_2_Non = Button(FrameEtape1_2, text="Non", width=10, bg='pink', fg='navy', command=lambda: CommandeChoixNon(FrameEtape1_2, canvas1, ListePersonnagePossible, BoutonValider1_2_Non,PersonnagePropose))
    BoutonValider1_2_Non.place(x=100, y=230)
   
    
# Procédure pour déterminer le genre de la personne avec laquelle on veut échanger
def etape1_1():

    FrameEtape1_1 = Frame(root, bd=250, bg="pink", cursor = "heart")
    FrameEtape1_1.place(x=0, y=0)

    VarChoixSexe = StringVar()
    choix_femme = Radiobutton(FrameEtape1_1,anchor=E, text=F, bg="pink",variable=VarChoixSexe, value=F)
    choix_femme.place(x=25, y=30)
    choix_femme.select()

    choix_homme = Radiobutton(FrameEtape1_1, text=M, bg="pink",variable=VarChoixSexe, value=M)
    choix_homme.place(x=25, y=60)
    
    choix_les2 = Radiobutton(FrameEtape1_1, text=X, bg="pink", variable=VarChoixSexe, value=X)
    choix_les2.place(x=25, y=90)

    choix_sexe= Radiobutton(FrameEtape1_1, text="Sexe du personnage", bg="pink", variable=VarChoixSexe, value="Sexe") 
    BoutonValider1_1 = Button(FrameEtape1_1, text="Valider", width=10, bg='pink', fg='navy', command=lambda:Etape1_2(VarChoixSexe,FrameEtape1_1))
    BoutonValider1_1.place(x=25, y=130)  
    
    # Mettre un titre à la frame *** OBLIGER DE METTRE .pack() ET NON .place SINON N'AFFICHE RIEN !!! ***
    label=Label(FrameEtape1_1, text= "Choisis ton crush  ♥ ?", bg="pink")
    label.pack()
    
#----------------------------- Programme principal ---------------------------

ListePersonnagePossible=[]
points=0
var_quest=0



# création de la fenetre principale où se deroule le jeu
root = Tk()
root.title("♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥   Jeu EPF de toi  ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥") #, fg='navy')
# Définir la taille de la fenêtre
#global largeur_ecran
largeur_ecran=root.winfo_screenwidth()
#global hauteur_ecran
hauteur_ecran=root.winfo_screenheight()
#global pourcentage
pourcentage=0.6
root.geometry("%dx%d+0+0" %(largeur_ecran*pourcentage,hauteur_ecran*pourcentage))
root.configure(bg="pink")

# Variable globale utile pour effacer l'image  
Photo_visible=0
var_date=IntVar()
# Ajouter un bouton Quitter en bas de la fenêtre
#Bouton_quitter=Button(root, text="Fermer la fenêtre",bg='pink', fg='navy', command=root.destroy)
#Bouton_quitter.place(x=(largeur_ecran*pourcentage)-145, y=(hauteur_ecran*pourcentage)-50)

# Changer l'icône de la fenêtre (NE FONCTIONNE PAS !!!)
#icon=PhotoImage(file="coeur.png").zoom(35).subsample(32)
#root.iconbitmap('coeur.ico')
                 
###PHOTO POUR CHAQUE PERSO                
PhotoSasuke=PhotoImage(file="Sasuke.png").zoom(35).subsample(32)
PhotoSakura=PhotoImage(file="Sakura.png").zoom(35).subsample(32)
#PhotoFilleBLeue=PhotoImage(file="FilleBleue.png").zoom(35).subsample(32)

#tableaux des caracteristiques visibles des persos
M="Homme"
F="Femme"
X="Peu importe"

# Initialiser les personnages
Sasuke_caractere=[0.1,0.1,1,0.1]
Sakura_caractere=[0.1,0.1,1,0.1]
m3_caractere=[0.1,0.1,1,0.1]
m2_caractere=[0.1,0.1,1,0.1]
f2_caractere=[0.1,0.1,1,0.1]
f3_caractere=[0.1,0.1,1,0.1]


Sasuke=[PhotoSasuke,M,18,"ninja","Paraît distant mais a un grand coeur","Sasuke",Sasuke_caractere]
m2=[PhotoSasuke,M,36,"ninja","Paraît distant mais a un grand coeur","m2",m2_caractere]
m3=[PhotoSasuke,M,57,"ninja","Paraît distant mais a un grand coeur","m3",m3_caractere]
Sakura=[PhotoSakura,F,18,"ninja","Très gentille et empathique","Sakura",Sakura_caractere]
f2=[PhotoSakura,F,19,"ninja","Très gentille et empathique","f2",f2_caractere]
f3=[PhotoSakura,F,26,"ninja","Très gentille et empathique","f3",f3_caractere]

ListePersonnage=[Sasuke, m2, m3, Sakura, f2, f3]

etape1_1()

root.mainloop() 