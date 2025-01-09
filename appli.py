import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import matplotlib.pyplot as plt
import csv
import hashlib
from tkinter import *
from tkinter import messagebox 
from tkinter import simpledialog
import requests
import json
import os
import tkinter as tk
from tkinter import ttk
from tkinter import font
# Fonction pour hacher le mot de passe
def hash_mots_de_passe(mots_de_passe):
    hashe = hashlib.sha256(mots_de_passe.encode())
    return hashe.hexdigest()

# Fonction pour vérifier la connexion
def connexion(pseudo, mots_de_passe):
    mots_de_passe_hashe = hash_mots_de_passe(mots_de_passe)
    with open('utilisateur.csv', 'r', newline='') as fichier:
        verif = csv.reader(fichier)
        for ligne in verif:
            if ligne and ligne[0] == pseudo and ligne[2] == mots_de_passe_hashe:
                messagebox.showinfo("Réussite de la connexion", f"Bienvenue, {pseudo}!")
                return True
    messagebox.showerror("Échec de la connexion", "Pseudo ou mot de passe incorrect.")
    return False

# Fonction pour soumettre le formulaire de connexion
def soumettre_formulaire():
    pseudo = entre_pseudo.get()
    mots_de_passe = entre_mots_de_passe.get()
    if connexion(pseudo, mots_de_passe):
        root.destroy()
        menu_utilisateur(pseudo, mots_de_passe)

# Fonction pour créer le formulaire de connexion
def formulaire_connexion():
    global root, entre_pseudo, entre_mots_de_passe
    root = tk.Tk()
    root.title("Connexion")
    root.geometry("400x300")
    root.configure(bg="#1e1e2f")

    frame = tk.Frame(root, bg="#282a36", relief="ridge", bd=5)
    frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

    label_pseudo = tk.Label(frame, text="Pseudo", font=("Helvetica", 12), fg="white", bg="#282a36")
    label_pseudo.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    entre_pseudo = tk.Entry(frame, font=("Helvetica", 12), bg="#44475a", fg="white", insertbackground="white", relief="sunken", bd=3)
    entre_pseudo.grid(row=0, column=1, padx=10, pady=10)

    label_mots_de_passe = tk.Label(frame, text="Mot de passe :", font=("Helvetica", 12), fg="white", bg="#282a36")
    label_mots_de_passe.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    entre_mots_de_passe = tk.Entry(frame, show='*', font=("Helvetica", 12), bg="#44475a", fg="white", insertbackground="white", relief="sunken", bd=3)
    entre_mots_de_passe.grid(row=1, column=1, padx=10, pady=10)

    bouton_soumettre = tk.Button(frame, text="Soumettre", command=soumettre_formulaire, font=("Helvetica", 12), bg="#6272a4", fg="white", activebackground="#50fa7b", activeforeground="black", relief="raised", bd=5)
    bouton_soumettre.grid(row=2, column=1, padx=10, pady=20)

    root.mainloop()

def menu():
    root = tk.Tk()
    root.title("Gestionnaire de commande")
    root.geometry("1080x720")
    root.configure(bg="#1e1e2f")

    frame = tk.Frame(root, bg="#282a36", relief="ridge", bd=10)
    frame.pack(expand=True, fill=tk.BOTH, padx=40, pady=40)

    label = tk.Label(frame, text="Bienvenue sur le gestionnaire de commande", font=("Helvetica", 20, "bold"), fg="white", bg="#282a36", relief="flat")
    label.pack(pady=20)

    bouton_connexion = tk.Button(frame, text="Connexion", command=formulaire_connexion, font=("Helvetica", 14), bg="#6272a4", fg="white", activebackground="#50fa7b", activeforeground="black", relief="raised", bd=5, width=15)
    bouton_connexion.pack(pady=10)

    bouton_inscription = tk.Button(frame, text="Inscription", command=formulaire_inscription, font=("Helvetica", 14), bg="#6272a4", fg="white", activebackground="#50fa7b", activeforeground="black", relief="raised", bd=5, width=15)
    bouton_inscription.pack(pady=10)

    bouton_quitter = tk.Button(frame, text="Quitter", command=root.destroy, font=("Helvetica", 14), bg="#ff5555", fg="white", activebackground="#ff79c6", activeforeground="black", relief="raised", bd=5, width=15)
    bouton_quitter.pack(pady=10)

    root.mainloop()

def formulaire_inscription():
    global root, entre_pseudo, entre_mots_de_passe, entre_email
    root = tk.Tk()
    root.title("Inscription")
    root.geometry("400x400")
    root.configure(bg="#1e1e2f")

    frame = tk.Frame(root, bg="#282a36", relief="ridge", bd=5)
    frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

    label_pseudo = tk.Label(frame, text="Pseudo", font=("Helvetica", 12), fg="white", bg="#282a36")
    label_pseudo.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    entre_pseudo = tk.Entry(frame, font=("Helvetica", 12), bg="#44475a", fg="white", insertbackground="white", relief="sunken", bd=3)
    entre_pseudo.grid(row=0, column=1, padx=10, pady=10)

    label_mots_de_passe = tk.Label(frame, text="Mot de passe :", font=("Helvetica", 12), fg="white", bg="#282a36")
    label_mots_de_passe.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    entre_mots_de_passe = tk.Entry(frame, show='*', font=("Helvetica", 12), bg="#44475a", fg="white", insertbackground="white", relief="sunken", bd=3)
    entre_mots_de_passe.grid(row=1, column=1, padx=10, pady=10)

    label_email = tk.Label(frame, text="Email :", font=("Helvetica", 12), fg="white", bg="#282a36")
    label_email.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    entre_email = tk.Entry(frame, font=("Helvetica", 12), bg="#44475a", fg="white", insertbackground="white", relief="sunken", bd=3)
    entre_email.grid(row=2, column=1, padx=10, pady=10)

    bouton_soumettre = tk.Button(frame, text="Soumettre", command=soumettre_inscription, font=("Helvetica", 12), bg="#6272a4", fg="white", activebackground="#50fa7b", activeforeground="black", relief="raised", bd=5)
    bouton_soumettre.grid(row=3, column=1, padx=10, pady=20)

    root.mainloop()

# Fonction pour soumettre le formulaire d'inscription
def soumettre_inscription():
    pseudo = entre_pseudo.get()
    mots_de_passe = entre_mots_de_passe.get()
    email = entre_email.get()
    if inscription(pseudo, mots_de_passe, email):
        messagebox.showinfo("Inscription réussie", "Votre compte a été créé avec succès.")
        root.destroy()
        menu()
    else:
        messagebox.showerror("Échec de l'inscription", "Impossible de créer le compte.")
# Fonction pour inscrire un nouvel utilisateur
def inscription(pseudo, mots_de_passe, email):
    with open('utilisateur.csv', 'r', newline='') as fichier:
        lecteur = csv.reader(fichier)
        for ligne in lecteur:
            if ligne and ligne[0] == pseudo:
                messagebox.showerror("Erreur", f"Le pseudo '{pseudo}' existe déjà. Impossible de créer un nouveau compte.")
                return False
    with open('utilisateur.csv', 'a', newline='') as fichier:
        ecriture = csv.writer(fichier)
        ecriture.writerow([pseudo, email, hash_mots_de_passe(mots_de_passe)])
    return True

# Fonction pour créer le menu utilisateur
def menu_utilisateur(pseudo, mots_de_passe):
    root = Tk()
    root.title("Menu Utilisateur")
    root.geometry("1920x1080")
    root.config(background='#4351ee')
    frame = Frame(root, bg='#4351ee')
    label = Label(root, text=f"Bienvenue, {pseudo}", font=("Courrier", 40), bg='#4351ee')
    label.pack(expand=YES)
    bouton_afficher_liste = Button(frame, text="Afficher la liste des articles", font=("Courrier", 25), bg="white", fg="#4351ee", command=lambda: afficher_liste(root))
    bouton_ajouter_produit = Button(frame, text="Ajouter un produit", font=("Courrier", 25), bg="white", fg="#4351ee", command=lambda: formulaire_ajouter_produit(pseudo))
    bouton_supprimer_produit = Button(frame, text="Supprimer un produit", font=("Courrier", 25), bg="white", fg="#4351ee", command=lambda: formulaire_supprimer_produit(pseudo))
    bouton_modifier_produit = Button(frame, text="Modifier un produit", font=("Courrier", 25), bg="white", fg="#4351ee", command=lambda: formulaire_modifier_produit(pseudo))
    bouton_modifier_mdp = Button(frame, text="Modifier votre mot de passe", font=("Courrier", 25), bg="white", fg="#4351ee", command=lambda: formulaire_modifier_mdp(pseudo, mots_de_passe))
    bouton_trier_prix = Button(frame, text="Trier par prix", font=("Courrier", 25), bg="white", fg="#4351ee", command=lambda: tri_par_ordre_croissant_prix(root))
    bouton_trier_alphabetique = Button(frame, text="Trier par ordre alphabétique", font=("Courrier", 25), bg="white", fg="#4351ee", command=lambda: tri_par_ordre_alphabetique(root))
    bouton_trier_quantite = Button(frame, text="Trier par quantité", font=("Courrier", 25), bg="white", fg="#4351ee", command=lambda: tri_par_ordre_croissant_de_la_quantite(root))
    bouton_rechercher_produit = Button(frame, text="Rechercher un produit", font=("Courrier", 25), bg="white", fg="#4351ee", command=lambda: formulaire_recherche_produit())
    bouton_voir_stat = Button(frame, text="Stat", font=("Courrier", 25), bg="white", fg="#4351ee", command=lambda:afficher_stat(pseudo))
    bouton_quitter = Button(frame, text="Quitter", font=("Courrier", 25), bg="white", fg="#4351ee", command=root.destroy)
    bouton_afficher_liste.pack()
    bouton_ajouter_produit.pack()
    bouton_supprimer_produit.pack()
    bouton_modifier_produit.pack()
    bouton_modifier_mdp.pack()
    bouton_trier_prix.pack()
    bouton_trier_alphabetique.pack()
    bouton_trier_quantite.pack()
    bouton_rechercher_produit.pack()
    bouton_voir_stat.pack() 
    bouton_quitter.pack()
    frame.pack(expand=YES)
    root.mainloop()

# Fonction pour afficher la liste des articles
def afficher_liste(root):
    with open('produit.txt', 'r') as fichier:
        contenu = fichier.read()
    messagebox.showinfo("Liste des articles", contenu)

# Fonction pour créer le formulaire d'ajout de produit
def formulaire_ajouter_produit(pseudo):
    root = Tk()
    root.title("Ajouter un produit")
    label_nom = Label(root, text="Nom du produit")
    label_nom.grid(row=0, column=0, padx=10, pady=10)
    entre_nom = Entry(root)
    entre_nom.grid(row=0, column=1, padx=10, pady=10)
    label_quantite = Label(root, text="Quantité")
    label_quantite.grid(row=1, column=0, padx=10, pady=10)
    entre_quantite = Entry(root)
    entre_quantite.grid(row=1, column=1, padx=10, pady=10)
    label_prix = Label(root, text="Prix")
    label_prix.grid(row=2, column=0, padx=10, pady=10)
    entre_prix = Entry(root)
    entre_prix.grid(row=2, column=1, padx=10, pady=10)
    bouton_soumettre = Button(root, text="Soumettre", command=lambda: ajouter_produit(pseudo, entre_nom.get(), entre_quantite.get(), entre_prix.get(), root))
    bouton_soumettre.grid(row=3, column=1, padx=10, pady=10)
    root.mainloop()

# Fonction pour ajouter un produit
def ajouter_produit(pseudo, nom_du_produit, quantite, prix, root):
    with open('produit.txt', 'a') as fichier:
        fichier.write(f"{pseudo},{nom_du_produit},{quantite},{prix}\n")
    messagebox.showinfo("Produit ajouté", f"Le produit '{nom_du_produit}' a été ajouté avec succès.")
    root.destroy()

# Fonction pour créer le formulaire de suppression de produit
def formulaire_supprimer_produit(pseudo):
    root = Tk()
    root.title("Supprimer un produit")
    label_nom = Label(root, text="Nom du produit")
    label_nom.grid(row=0, column=0, padx=10, pady=10)
    entre_nom = Entry(root)
    entre_nom.grid(row=0, column=1, padx=10, pady=10)
    bouton_soumettre = Button(root, text="Soumettre", command=lambda: supprimer_produit(pseudo, entre_nom.get(), root))
    bouton_soumettre.grid(row=1, column=1, padx=10, pady=10)
    root.mainloop()

# Fonction pour supprimer un produit
def supprimer_produit(pseudo, nom_du_produit, root):
    with open("produit.txt", "r") as fichier:
        lignes = fichier.readlines()
        if lignes[0]==pseudo:
            with open("produit.txt", 'w') as fichier:
                for ligne in lignes:
                    parties = ligne.split(',')
                    if len(parties) >= 2 and (parties[0] != pseudo or parties[1] != nom_du_produit):
                        fichier.write(ligne)
            messagebox.showinfo("Produit supprimé", f"Le produit '{nom_du_produit}' a été supprimé avec succès.")
            root.destroy()
        else:
            messagebox.showerror("Error", f"Vous ne pouvez pas supprimer le produit de votre concurrent !")

# Fonction pour créer le formulaire de modification de produit
def formulaire_modifier_produit(pseudo):
    root = Tk()
    root.title("Modifier un produit")
    label_nom = Label(root, text="Nom du produit")
    label_nom.grid(row=0, column=0, padx=10, pady=10)
    entre_nom = Entry(root)
    entre_nom.grid(row=0, column=1, padx=10, pady=10)
    bouton_soumettre = Button(root, text="Soumettre", command=lambda: modifier_produit(pseudo, entre_nom.get(), root))
    bouton_soumettre.grid(row=1, column=1, padx=10, pady=10)
    root.mainloop()

# Fonction pour modifier un produit
def modifier_produit(pseudo, nom_du_produit, root):
    lst_a_modifier = []
    with open('produit.txt', 'r') as fichier:
        lignes = fichier.read()
    recup = extraire(lignes)
    recup_final = [[element.strip() for element in sous_liste] for sous_liste in recup]
    for i in recup_final:
        if i[0] == pseudo:
            lst_a_modifier.append(i)
    print(lst_a_modifier)

    def demander_choix():
        def soumettre_choix():
            choix = entre_choix.get()
            if choix == "nom":
                demander_nom()
            elif choix == "quantité":
                demander_quantite()
            elif choix == "prix":
                demander_prix()
            fenetre_choix.destroy()

        fenetre_choix = Toplevel(root)
        fenetre_choix.title("Modifier")
        label_choix = Label(fenetre_choix, text="Voulez-vous modifier le nom du produit, la quantité, le prix ?")
        label_choix.pack(pady=10)
        entre_choix = Entry(fenetre_choix)
        entre_choix.pack(pady=10)
        bouton_soumettre = Button(fenetre_choix, text="Soumettre", command=soumettre_choix)
        bouton_soumettre.pack(pady=10)

    def demander_nom():
        def soumettre_nom():
            choix2 = entre_nom.get()
            for i in lst_a_modifier:
                if i[1] == choix2:
                    demander_nouveau_nom(i)
            fenetre_nom.destroy()

        fenetre_nom = Toplevel(root)
        fenetre_nom.title("Modifier le nom")
        label_nom = Label(fenetre_nom, text="Voulez-vous modifier le nom de quel produit ?")
        label_nom.pack(pady=10)
        entre_nom = Entry(fenetre_nom)
        entre_nom.pack(pady=10)
        bouton_soumettre = Button(fenetre_nom, text="Soumettre", command=soumettre_nom)
        bouton_soumettre.pack(pady=10)

    def demander_nouveau_nom(produit):
        def soumettre_nouveau_nom():
            nouveau_nom = entre_nouveau_nom.get()
            produit[1] = nouveau_nom
            sauvegarder_modifications()
            fenetre_nouveau_nom.destroy()

        fenetre_nouveau_nom = Toplevel(root)
        fenetre_nouveau_nom.title("Nouveau nom")
        label_nouveau_nom = Label(fenetre_nouveau_nom, text="Par quel nom ?")
        label_nouveau_nom.pack(pady=10)
        entre_nouveau_nom = Entry(fenetre_nouveau_nom)
        entre_nouveau_nom.pack(pady=10)
        bouton_soumettre = Button(fenetre_nouveau_nom, text="Soumettre", command=soumettre_nouveau_nom)
        bouton_soumettre.pack(pady=10)

    def demander_quantite():
        def soumettre_quantite():
            choix2 = entre_quantite.get()
            for i in lst_a_modifier:
                if i[1] == choix2:
                    demander_nouvelle_quantite(i)
            fenetre_quantite.destroy()

        fenetre_quantite = Toplevel(root)
        fenetre_quantite.title("Modifier la quantité")
        label_quantite = Label(fenetre_quantite, text="Voulez-vous modifier la quantité de quel produit ?")
        label_quantite.pack(pady=10)
        entre_quantite = Entry(fenetre_quantite)
        entre_quantite.pack(pady=10)
        bouton_soumettre = Button(fenetre_quantite, text="Soumettre", command=soumettre_quantite)
        bouton_soumettre.pack(pady=10)

    def demander_nouvelle_quantite(produit):
        def soumettre_nouvelle_quantite():
            nouvelle_quantite = entre_nouvelle_quantite.get()
            produit[2] = nouvelle_quantite
            sauvegarder_modifications()
            fenetre_nouvelle_quantite.destroy()

        fenetre_nouvelle_quantite = Toplevel(root)
        fenetre_nouvelle_quantite.title("Nouvelle quantité")
        label_nouvelle_quantite = Label(fenetre_nouvelle_quantite, text="Quelle est la nouvelle quantité ?")
        label_nouvelle_quantite.pack(pady=10)
        entre_nouvelle_quantite = Entry(fenetre_nouvelle_quantite)
        entre_nouvelle_quantite.pack(pady=10)
        bouton_soumettre = Button(fenetre_nouvelle_quantite, text="Soumettre", command=soumettre_nouvelle_quantite)
        bouton_soumettre.pack(pady=10)

    def demander_prix():
        def soumettre_prix():
            choix2 = entre_prix.get()
            for i in lst_a_modifier:
                if i[1] == choix2:
                    demander_nouveau_prix(i)
            fenetre_prix.destroy()

        fenetre_prix = Toplevel(root)
        fenetre_prix.title("Modifier le prix")
        label_prix = Label(fenetre_prix, text="Voulez-vous modifier le prix de quel produit ?")
        label_prix.pack(pady=10)
        entre_prix = Entry(fenetre_prix)
        entre_prix.pack(pady=10)
        bouton_soumettre = Button(fenetre_prix, text="Soumettre", command=soumettre_prix)
        bouton_soumettre.pack(pady=10)

    def demander_nouveau_prix(produit):
        def soumettre_nouveau_prix():
            nouveau_prix = entre_nouveau_prix.get()
            produit[3] = nouveau_prix
            sauvegarder_modifications()
            fenetre_nouveau_prix.destroy()

        fenetre_nouveau_prix = Toplevel(root)
        fenetre_nouveau_prix.title("Nouveau prix")
        label_nouveau_prix = Label(fenetre_nouveau_prix, text="Quel est le nouveau prix ?")
        label_nouveau_prix.pack(pady=10)
        entre_nouveau_prix = Entry(fenetre_nouveau_prix)
        entre_nouveau_prix.pack(pady=10)
        bouton_soumettre = Button(fenetre_nouveau_prix, text="Soumettre", command=soumettre_nouveau_prix)
        bouton_soumettre.pack(pady=10)

    def sauvegarder_modifications():
        y = [','.join(i) for i in lst_a_modifier]
        t = [element + '\n' for element in y]
        resultat = ''.join(t)
        with open('produit.txt', 'w') as fichier:
            fichier.writelines(resultat)
        messagebox.showinfo("Produit modifié", f"Le produit '{nom_du_produit}' a été modifié avec succès.")
        root.destroy()

    demander_choix()

# Fonction pour créer le formulaire de modification de mot de passe
def formulaire_modifier_mdp(pseudo, mots_de_passe):
    root = Tk()
    root.title("Modifier le mot de passe")
    label_nouveau_mdp = Label(root, text="Nouveau mot de passe")
    label_nouveau_mdp.grid(row=0, column=0, padx=10, pady=10)
    entre_nouveau_mdp = Entry(root, show='*')
    entre_nouveau_mdp.grid(row=0, column=1, padx=10, pady=10)
    bouton_soumettre = Button(root, text="Soumettre", command=lambda: modifier_mdp(pseudo, mots_de_passe, entre_nouveau_mdp.get(), root))
    bouton_soumettre.grid(row=1, column=1, padx=10, pady=10)
    root.mainloop()

# Fonction pour modifier le mot de passe
def modifier_mdp(pseudo, mots_de_passe, nouveau_mdp, root):
    with open("utilisateur.csv", 'r', newline='') as fichier:
        lecture = csv.reader(fichier)
        liste = list(lecture)
    for i in range(len(liste)):
        if len(liste[i]) > 2 and liste[i][0] == pseudo and liste[i][2] == hash_mots_de_passe(mots_de_passe):
            liste[i][2] = hash_mots_de_passe(nouveau_mdp)
    with open("utilisateur.csv", 'w', newline='') as fichier:
        ecriture = csv.writer(fichier)
        ecriture.writerows(liste)
    messagebox.showinfo("Mot de passe modifié", "Votre mot de passe a été modifié avec succès.")
    root.destroy()

# Fonction pour trier les produits par ordre alphabétique
def tri_par_ordre_alphabetique(root):
    with open('produit.txt', 'r') as fichier:
        lignes = fichier.read()
    liste = extraire(lignes)
    lignes_triees = tri_a_bulles(liste)
    y = [','.join(i) for i in lignes_triees]
    result = '\n'.join(y)
    messagebox.showinfo("Produits triés par ordre alphabétique", result)

# Fonction pour trier les produits par ordre croissant des prix
def tri_par_ordre_croissant_prix(root):
    with open('produit.txt', 'r') as fichier:
        lignes = fichier.read()
    x = tri_rapide(lignes)
    y = [','.join(i) for i in x]
    result = '\n'.join(y)
    messagebox.showinfo("Produits triés par ordre croissant des prix", result)

# Fonction pour trier les produits par ordre croissant de la quantité
def tri_par_ordre_croissant_de_la_quantite(root):
    with open('produit.txt', 'r') as fichier:
        lignes = fichier.read()
    liste = extraire(lignes)
    for i in range(len(liste)):
        for j in range(len(liste) - i - 1):
            if len(liste[j]) > 2 and len(liste[j + 1]) > 2:
                if int(liste[j][2]) > int(liste[j + 1][2]):
                    liste[j], liste[j + 1] = liste[j + 1], liste[j]
    x = [','.join(i) for i in liste]
    result = '\n'.join(x)
    messagebox.showinfo("Produits triés par ordre croissant de la quantité", result)

# Fonction pour extraire les lignes d'un fichier CSV
def extraire(ligne):
    x = ligne.split('\n')
    liste_de_liste = []
    for i in x:
        liste_de_liste.append(i.split(','))
    return liste_de_liste

# Fonction pour trier les produits par ordre croissant des prix
def tri_rapide(lst):
    if not isinstance(lst, list):
        lst = extraire(lst)
    elif len(lst) <= 1:
        return lst
    pivot = lst[-1][-1]
    petit = []
    grand = []
    egal = []
    for i in lst:
        if i[-1] < pivot:
            petit.append(i)
        elif i[-1] == pivot:
            egal.append(i)
        elif i[-1] > pivot:
            grand.append(i)
    lst_final = tri_rapide(petit) + egal + tri_rapide(grand)
    return lst_final

# Fonction pour trier les produits par ordre alphabétique
def tri_a_bulles(lignes):
    n = len(lignes)
    for i in range(n):
        for j in range(n - i - 1):
            if len(lignes[j]) > 1 and len(lignes[j + 1]) > 1:
                if lignes[j][1] > lignes[j + 1][1]:
                    lignes[j], lignes[j + 1] = lignes[j + 1], lignes[j]
    return lignes

# Fonction pour vérifier si le mot de passe est compromis
def mots_de_passe_compromis(mots_de_passe):
    if len(mots_de_passe) < 12:
        messagebox.showerror("Mot de passe faible", "Le mot de passe est trop court. Il doit faire au moins 12 caractères.")
        return False
    if not any(char in "#@!§" for char in mots_de_passe):
        messagebox.showerror("Mot de passe faible", "Vous devez avoir au moins un caractère spécial.")
        return False
    if not any(char.isupper() for char in mots_de_passe):
        messagebox.showerror("Mot de passe faible", "Vous devez avoir au moins une lettre majuscule.")
        return False
    if not any(char.isdigit() for char in mots_de_passe):
        messagebox.showerror("Mot de passe faible", "Vous devez avoir au moins un chiffre.")
        return False
    return True

# Fonction pour vérifier si le mot de passe est dans la liste des mots de passe compromis
def alert_mdp(mots_de_passe):
    sha1_mots_de_passe = hashlib.sha1(mots_de_passe.encode('utf-8')).hexdigest().upper()
    prefix = sha1_mots_de_passe[:5]
    suffix = sha1_mots_de_passe[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    reponse = requests.get(url)
    if reponse.status_code == 200:
        hashes = (line.split(":")for line in reponse.text.splitlines())
        for h , count in hashes : 
            if h == suffix:
                return int(count)
    return 0

# Fonction pour envoyer un email d'alerte
def envoie_mail(pseudo, mots_de_passe):
    email_alert = "nidri@guardiaschool.fr"
    mdp_email_alert = "thdk thiu jxld soqj"
    mail_subject = "Faille de sécurité sur le gestionnaire de stock"
    contenu_du_mail = "Votre mot de passe est compromis. Veuillez le modifier."
    with open("utilisateur.csv", 'r', encoding='utf-8') as fichier:
        liste = fichier.read()
    recup = extraire(liste)
    if alert_mdp(mots_de_passe):
        for i in recup:
            if len(i) > 2 and i[2] == hash_mots_de_passe(mots_de_passe):
                mail_client = i[1]
                if 'yahoo' in mail_client:
                    SMTP_SERVER = 'smtp.mail.yahoo.com'
                    SMTP_PORT = 465
                elif 'gmail' in mail_client:
                    SMTP_SERVER = 'smtp.gmail.com'
                    SMTP_PORT = 587
                elif 'outlook' in mail_client:
                    SMTP_SERVER = 'smtp.office365.com'
                    SMTP_PORT = 587

                s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
                s.starttls()
                s.login(email_alert, mdp_email_alert)
                msg = MIMEMultipart()
                msg['From'] = email_alert
                msg['To'] = mail_client
                msg['Subject'] = mail_subject

                body = f"Bonjour {pseudo},\n\n{contenu_du_mail}"
                msg.attach(MIMEText(body, 'plain'))

                s.sendmail(email_alert, mail_client, msg.as_string())
                s.quit()

# Fonction pour rechercher un produit
def recherche_produit(nom_du_produit):
    t = tri_pour_recherche_dicho()
    if not t:
        messagebox.showinfo("Résultat de la recherche", "Aucun résultat trouvé.")
        return

    a = 0
    b = len(t) - 1  # b doit être len(t) - 1 pour être dans les limites de la liste

    while a <= b:
        m = (a + b) // 2
        if m >= len(t):
            print(f"Erreur: m={m} est en dehors des limites de la liste (len(t)={len(t)})")
            break  # Sortir de la boucle si m est en dehors des limites
        if t[m][1] > nom_du_produit:
            b = m - 1
        elif t[m][1] < nom_du_produit:
            a = m + 1
        else:
            resultat = t[m]
            y = [''.join(map(str, i)) for i in resultat]
            result = ';'.join(y)
            afficher_resultat(result)
            return

    # Vérifier les indices a et b après la boucle
    if a < len(t) and t[a][1] == nom_du_produit:
        resultat = t[a]
        y = [''.join(map(str, i)) for i in resultat]
        result = ';'.join(y)
        afficher_resultat(result)
    elif b < len(t) and t[b][1] == nom_du_produit:
        resultat = t[b]
        y = [','.join(map(str, i)) for i in resultat]
        result = ';'.join(y)
        afficher_resultat(result)
    else:
        messagebox.showinfo("Résultat de la recherche", "Aucun résultat trouvé.")


# Fonction pour afficher le résultat de la recherche
def afficher_resultat(resultat):
    root = Tk()
    root.title("Résultat de la recherche")
    label_resultat = Label(root, text=resultat, wraplength=400)
    label_resultat.pack(padx=20, pady=20)
    bouton_fermer = Button(root, text="Fermer", command=root.destroy)
    bouton_fermer.pack(pady=10)
    root.mainloop()

# Fonction pour trier les produits pour la recherche dichotomique
def tri_pour_recherche_dicho():
    with open('produit.txt', 'r') as fichier:
        lignes = fichier.read()
    liste = extraire(lignes)
    lignes_triees = tri_a_bulles(liste)
    return lignes_triees

# Fonction pour créer le formulaire de recherche de produit
def formulaire_recherche_produit():
    root = Tk()
    root.title("Rechercher un produit")
    label_nom = Label(root, text="Nom du produit")
    label_nom.grid(row=0, column=0, padx=10, pady=10)
    entre_nom = Entry(root)
    entre_nom.grid(row=0, column=1, padx=10, pady=10)
    bouton_soumettre = Button(root, text="Soumettre", command=lambda: recherche_produit(entre_nom.get()))
    bouton_soumettre.grid(row=1, column=1, padx=10, pady=10)
    root.mainloop()

#fonction pour la simulation de la partie client
def commande():
    nom_du_produit = input("Entrer le nom du produit : ")
    vendeur = input("entrer le nom du commerçant : ")
    quantite = input("Entrer la quantité : ")
    with open('produit.txt','r') as fichier : 
        liste = fichier.read()
        f = extraire(liste)
        for i in range(0,len(f)-1,1) :
            if f[i][0] == vendeur and f[i][1] == nom_du_produit and int(f[i][2]) > int(quantite) : 
                prix_unite = f[i][3]
                f[i][2] = str(int(f[i][2]) - int(quantite))
                
        
        y = [','.join(i) for i in f]
        t = [element + '\n' for element in y]
        resultat = ''.join(t)
        
        prix = str(int(quantite) * int(prix_unite))
        
        nouvelle_commande = {
            "Vendeur":vendeur,
            "nom du produit": nom_du_produit,
            "quantite":quantite,
            "prix":prix
        }
    
        if os.path.exists("index.json"):
            try:
                with open('index.json','r') as fichier :
                 commandes = json.load(fichier)
            except json.JSONDecodeError:
                commandes = []
        else:
            commandes = []
        
        commandes.append(nouvelle_commande)

        with open('index.json','w') as fichier:
            json.dump(commandes,fichier,indent=4)

        with open('produit.txt','w') as fichier :
            fichier.write(resultat)

### fonction qui permet d'afficher les stats des commandes 
def afficher_stat(pseudo):
    liste1 = []
    somme_dict = {}
    
    with open('index.json','r')as fichier :
        lecture = json.load(fichier)
    
    for i in range(0,len(lecture),1) : 
        if lecture[i]["Vendeur"]== pseudo and lecture[i]["nom du produit"] : 
            liste1.append([lecture[i]["nom du produit"],int(lecture[i]["quantite"])])
    print(liste1)

    for item in liste1 :
        key = item[0]
        value = item[1]

        if key in somme_dict:
            somme_dict[key] += value
        else:
            somme_dict[key] = value
    
    liste2 = list(somme_dict.keys())
    liste3 = list(somme_dict.values())

    
    plt.figure(figsize=(10, 6))
    plt.plot(liste2, liste3, marker='o', linestyle='-',color='b')

    plt.title('Stat des ventes')
    plt.xlabel('Produit')
    plt.ylabel('quantite commandé')

    plt.show()
# Script principal
menu()