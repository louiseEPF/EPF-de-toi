# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 16:31:05 2020

@author: louis_000
"""

#tkinter est tres specifique donc je te mets
#plein de commentaires pour que tu comprennes bien 
#ce que j'ai fait



from tkinter import *
import random
#creation de la fenetre ou se deroule le jeu
fenetre = Tk()



###ELEMENTS ETAPE 1


#les label sont les equivalents de print pour tkinter
label = Label(fenetre, text="Choisis ton crush <3")
# .pack() sert à afficher l'element dans la fenetre sinon on ne voit pas
label.pack()

                 
                    
#DONNEES
                 
                 
###PHOTO POUR CHAQUE PERSO                
Photo1 = PhotoImage(file="Sasuke.png").zoom(35).subsample(32)

Photo2=PhotoImage(file="Sakura.png") .zoom(35).subsample(32)

#tableaux des caracteristiques visibles des persos
M="Homme"
F="Femme"

Sasuke=[Photo1,M,18,"ninja","Paraît distant mais a un grand coeur","Sasuke"]
Sakura=[Photo2,F,18,"ninja","Très gentille et empathique","Sakura"]


tab2tab=[Sasuke,Sakura]



def Choisir_Personnage():
    global sexe_choisi
    sexe_choisi=var_choix.get()
    
    frame_depart.destroy()
    
    w=IntVar()
    choix_crush=0
#    #les frames de la fenetre sont des blocs ou tu peux grouper du texte,des images,etc
#    #les frames sont independantes les unes des autres 
#    ###FRAME DES PERSONNAGES
    
    Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
#    #pour la position, padx et pady sont tres importants
#    #car il permettent de placer ton element
    Frame1.pack()
#    while w != 1:
#        a=Tirage()
#    #les canvas contiennent et animent les images
#    ###PHOTO PERSONNAGE (DANS LA FRAME)
#    
    canvas1 = Canvas(Frame1, width=100, height=100, background="#FFFFFF")
##  
    if choix_crush==0:
        if sexe_choisi=="Homme":
            var1=random.randint(0,1)
        elif sexe_choisi=="Femme":
            var1=random.randint(0,1)
        elif sexe_choisi=="Homme et Femme":
            var1=random.randint(0,1)
    #solution secours:
    #var1=random.randint(0,1)
##            
##    
        perso_propose=tab2tab[var1]
        Photo_visible=canvas1.create_image(50,290,image=perso_propose[0])
        canvas1.pack()
##
##    frame_perso=Frame(fenetre)
        Label(Frame1, text=perso_propose[4]).pack(padx=10, pady=10)
        Label(Frame1, text="Voulez-vous commencer à discuter avec "+perso_propose[5]+" ?").pack(padx=10, pady=10)
        bouton_oui = Radiobutton(Frame1, text="oui",variable=w,value=1)
        bouton_non = Radiobutton(Frame1, text="non",variable=w,value=0)
        bouton_valider2=Button(Frame1, text="Valider", font=("Tahoma", 12), bg="#BE2121", fg ="white" , width=20)

        bouton_oui.pack()
        bouton_non.pack()
        bouton_valider2.pack()
        choix_crush=w.get()
    if choix_crush==1:
        Frame1.destroy()
    
    
###DEPART
def Depart() : 
    global frame_depart
    frame_depart = Frame(fenetre, bg="#D83AA1")
    frame_depart.pack()
    global var_choix
    var_choix = StringVar()
    choix_femme = Radiobutton(frame_depart, text="Femme", variable=var_choix, value="Femme")
    choix_homme = Radiobutton(frame_depart, text="Homme", variable=var_choix, value="Homme")
    choix_les2 = Radiobutton(frame_depart, text="Peu importe", variable=var_choix, value="Homme et Femme")

    choix_femme.pack()
    choix_homme.pack()
    choix_les2.pack()
    
    
        
    bouton_valider = Button(frame_depart, text="Valider", font=("Tahoma", 12), bg="#BE2121", fg ="white" , width=20,command=Choisir_Personnage)
    bouton_valider.pack()
    
    



Commencer=Depart()


fenetre.mainloop()
               

               
               
               
               
