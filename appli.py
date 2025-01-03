import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv
import hashlib

def menu():
    print("1-Connexion")
    print("2-Inscription")
    print("3-Au revoir")
    choix = input("Faites un choix : ")

    if choix == "1":
        pseudo = input("Entrer votre pseudo : ")
        mots_de_passe = input("Entrer votre mot de passe : ")
        if connexion(pseudo, mots_de_passe):
            envoie_mail(pseudo, mots_de_passe)
            menu_utilisateur(pseudo, mots_de_passe)

    elif choix == "2":
        pseudo = input("Ajouter un pseudo : ")
        mots_de_passe = input("Ajouter un mot de passe : ")
        email = input("Ajouter un email : ")
        if mots_de_passe_compromis(mots_de_passe):
            inscription(pseudo, mots_de_passe, email)
            menu()
        else:
            menu()

    elif choix == "3":
        print("Au revoir !")
    else:
        print("Choix invalide. Veuillez réessayer.")
        menu()

def hash_mots_de_passe(mots_de_passe):
    hashe = hashlib.sha256(mots_de_passe.encode())
    return hashe.hexdigest()

def inscription(pseudo, mots_de_passe, email):
    with open('utilisateur.csv', 'r', newline='') as fichier:
        lecteur = csv.reader(fichier)
        for ligne in lecteur:
            if ligne and ligne[0] == pseudo:
                print(f"Le pseudo '{pseudo}' existe déjà. Impossible de créer un nouveau compte.")
                return
    with open('utilisateur.csv', 'a', newline='') as fichier:
        ecriture = csv.writer(fichier)
        ecriture.writerow([pseudo, email, hash_mots_de_passe(mots_de_passe)])

def connexion(pseudo, mots_de_passe):
    mots_de_passe_hashe = hash_mots_de_passe(mots_de_passe)
    with open('utilisateur.csv', 'r', newline='') as fichier:
        verif = csv.reader(fichier)
        for ligne in verif:
            if ligne and ligne[0] == pseudo and ligne[2] == mots_de_passe_hashe:
                print("Connexion réussie à l'utilisateur:", pseudo)
                return True
    print("Échec de la connexion. Vérifiez votre pseudo et mot de passe.")
    return False

def menu_utilisateur(pseudo, mots_de_passe):
    print("1-Afficher la liste des articles")
    print("2-Ajouter un produit")
    print("3-Supprimer un produit")
    print("4-Modifier un produit")
    print("5-Modifier votre mot de passe")
    print("7-Trier les produits par ordre croissant des prix")
    print("8-Trier les produits par ordre alphabétique")
    print("9-Trier les produits par ordre croissant de la quantité")
    print("10-Quitter")
    choix = input("Faites un choix : ")
    if choix == "1":
        afficher_liste()
        menu_utilisateur(pseudo, mots_de_passe)
    elif choix == "2":
        nom_du_produit = input("Entrer le nom de votre produit : ")
        quantite = input("Entrer la quantité : ")
        prix = input("Entrer le prix du produit : ")
        ajouter_produit(pseudo, nom_du_produit, quantite, prix)
        menu_utilisateur(pseudo, mots_de_passe)
    elif choix == "3":
        nom_du_produit = input("Entrer le nom du produit : ")
        supprimer_produit(pseudo, nom_du_produit)
        menu_utilisateur(pseudo, mots_de_passe)
    elif choix == "4":
        modifier_produit(pseudo)
        menu_utilisateur(pseudo, mots_de_passe)
    elif choix == "5":
        modifier_mdp(pseudo, mots_de_passe)
        menu_utilisateur(pseudo, mots_de_passe)
    elif choix == "6":
        tri_par_ordre_croissant_prix()
        menu_utilisateur(pseudo, mots_de_passe)
    elif choix == "7":
        tri_par_ordre_alphabetique()
        menu_utilisateur(pseudo, mots_de_passe)
    elif choix == "8":
        tri_par_ordre_croissant_de_la_quantite()
        menu_utilisateur(pseudo, mots_de_passe)
    elif choix == "9":
        nom_du_produit = input("Vous chercher quel produit : ")
        print(recherche_produit(nom_du_produit))
        menu_utilisateur(pseudo,mots_de_passe)
    else:
        print("Choix invalide. Veuillez réessayer.")
        menu_utilisateur(pseudo, mots_de_passe)


def afficher_liste():
    with open('produit.txt', 'r') as fichier:
        contenu = fichier.read()
    print(contenu)

def ajouter_produit(pseudo, nom_du_produit, quantite, prix):
    with open('produit.txt', 'a') as fichier:
        fichier.write(f"{pseudo},{nom_du_produit},{quantite},{prix}\n")

def supprimer_produit(pseudo, nom_du_produit):
    with open("produit.txt", "r") as fichier:
        lignes = fichier.readlines()
    with open("produit.txt", 'w') as fichier:
        for ligne in lignes:
            parties = ligne.split(',')
            if len(parties) >= 2 and (parties[0] != pseudo or parties[1] != nom_du_produit):
                fichier.write(ligne)

def modifier_produit(pseudo):
    lst_a_modifier = []
    with open('produit.txt', 'r') as fichier:
        lignes = fichier.read()
    recup = recup_csv(lignes)
    recup_final = [[element.strip() for element in sous_liste] for sous_liste in recup]
    for i in recup_final:
        if i[0] == pseudo:
            lst_a_modifier.append(i)
    print(lst_a_modifier)
    choix = input("Voulez-vous modifier le nom du produit, la quantité, le prix ? ")
    if choix == "nom":
        choix2 = input("Voulez-vous modifier le nom de quel produit ? ")
        for i in lst_a_modifier:
            if i[1] == choix2:
                choix3 = input("Par quel nom ? ")
                i[1] = choix3
    elif choix == "quantité":
        choix2 = input("Voulez-vous modifier la quantité de quel produit ? ")
        for i in lst_a_modifier:
            if i[1] == choix2:
                choix3 = input("Quelle est la nouvelle quantité ? ")
                i[2] = choix3
    elif choix == "prix":
        choix2 = input("Voulez-vous modifier le prix de quel produit ? ")
        for i in lst_a_modifier:
            if i[1] == choix2:
                choix3 = input("Quel est le nouveau prix ? ")
                i[3] = choix3
    print(lst_a_modifier)
    y = [','.join(i) for i in lst_a_modifier]
    t = [element + '\n' for element in y]
    resultat = ''.join(t)
    with open('produit.txt', 'w') as fichier:
        fichier.writelines(resultat)

def afficher_ma_liste(pseudo):
    with open('produit.txt', 'r') as fichier:
        lignes = fichier.read()
    recup = extraire(lignes)
    recup_final = [[element.strip() for element in sous_liste] for sous_liste in recup]
    for i in recup_final:
        if i[0] == pseudo:
            resultat = ','.join(i)
            print(resultat)

def tri_a_bulles(lignes):
    n = len(lignes)
    for i in range(n):
        for j in range(n-i-1):
            if len(lignes[j]) > 1 and len(lignes[j + 1]) > 1:
                if lignes[j][1] > lignes[j + 1][1]:
                    lignes[j], lignes[j + 1] = lignes[j + 1], lignes[j]
    return lignes

def tri_par_ordre_alphabetique():
    with open('produit.txt', 'r') as fichier:
        lignes = fichier.read()
    liste = extraire(lignes)
    lignes_triees = tri_a_bulles(liste)
    y = [','.join(i) for i in lignes_triees]
    result = '\n'.join(y)
    print(result)

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

def extraire(ligne):
    x = ligne.split('\n')
    liste_de_liste = []
    for i in x:
        liste_de_liste.append(i.split(','))
    return liste_de_liste


def tri_par_ordre_croissant_prix():
    with open('produit.txt', 'r') as fichier:
        lignes = fichier.read()
    x = tri_rapide(lignes)
    y = [','.join(i) for i in x]
    result = '\n'.join(y)
    print(result)

def tri_par_ordre_croissant_de_la_quantite():
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
    print(result)

def tri_pour_recherche_dicho():
    with open('produit.txt', 'r') as fichier:
        lignes = fichier.read()
    liste = extraire(lignes)
    lignes_triees = tri_a_bulles(liste)
    return lignes_triees

def recherche_produit(nom_du_produit):
    t = tri_pour_recherche_dicho()
    a = 0
    b = len(t)
    if b == 0:
        return "Aucun résultat"
    while b > a + 1:
        m = (a + b) // 2
        if t[m][1] > nom_du_produit:
            b = m
        else:
            a = m
    if t[a][1] == nom_du_produit:
        resultat = t[a]
        y = [','.join(i) for i in resultat]
        result = ';'.join(y)
        print(result)
    elif t[b][1] == nom_du_produit:
        resultat = t[b]
        y = [','.join(i) for i in resultat]
        result = ''.join(y)
        print(result)

def mots_de_passe_compromis(mots_de_passe):
    if len(mots_de_passe) < 12:
        print("Le mot de passe est trop court. Il doit faire au moins 12 caractères.")
        return False
    if not any(char in "#@!§" for char in mots_de_passe):
        print("Vous devez avoir au moins un caractère spécial.")
        return False
    if not any(char.isupper() for char in mots_de_passe):
        print("Vous devez avoir au moins une lettre majuscule.")
        return False
    if not any(char.isdigit() for char in mots_de_passe):
        print("Vous devez avoir au moins un chiffre.")
        return False
    return True

def alert(mots_de_passe):
    with open('rockyou.txt', 'r') as fichier:
        lignes = fichier.read()
    return mots_de_passe in lignes

def recup_csv(fichier):
    x = fichier.split('\n')
    liste_de_liste = []
    for i in x:
        liste_de_liste.append(i.split(','))
    return liste_de_liste
def envoie_mail(pseudo, mots_de_passe):
    email_alert = "nidri@guardiaschool.fr"
    mdp_email_alert = "thdk thiu jxld soqj"
    mail_subject = "Faille de sécurité sur le gestionnaire de stock"
    contenu_du_mail = "Votre mot de passe est compromis. Veuillez le modifier."
    with open("utilisateur.csv", 'r', encoding='utf-8') as fichier:
        liste = fichier.read()
    recup = recup_csv(liste)
    if alert(mots_de_passe):
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


def modifier_mdp(pseudo, mots_de_passe):
    nouveau_mdp = input("Entrer le nouveau mot de passe : ")
    with open("utilisateur.csv", 'r', newline='') as fichier:
        lecture = csv.reader(fichier)
        liste = list(lecture)
    for i in range(len(liste)):
        if len(liste[i]) > 2 and liste[i][0] == pseudo and liste[i][2] == hash_mots_de_passe(mots_de_passe):
            liste[i][2] = hash_mots_de_passe(nouveau_mdp)
    with open("utilisateur.csv", 'w', newline='') as fichier:
        ecriture = csv.writer(fichier)
        ecriture.writerows(liste)

    print("Mot de passe modifié avec succès.")

### Script principal ###
menu()
