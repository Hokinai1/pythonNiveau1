# ================================
# Mini Gestionnaire de Crédits Téléphoniques
# Projet pour débutants Python
# ================================

# --- Variables globales ---
solde = 0.0                    # Le crédit actuel de l'utilisateur
tarif_appel_minute = 25.0      # Prix d'une minute d'appel (FCFA)
tarif_sms = 25.0               # Prix d'un SMS (FCFA)
nom_utilisateur = ""           # Nom de l'utilisateur


# --- Fonctions ---

def demander_nom():
    """Demande le nom de l'utilisateur et l'enregistre"""
    global nom_utilisateur
    nom_utilisateur = input("Comment vous appelez-vous ? ")
    print(f"\nBienvenue {nom_utilisateur} dans votre gestionnaire de crédit Moov !\n")


def afficher_solde():
    """Affiche le solde actuel"""
    print(f"Bonjour {nom_utilisateur}, votre solde est de {solde} FCFA\n")


def acheter_credit():
    """Recharge du crédit"""
    global solde
    try:
        montant_recharge = float(input("Combien voulez-vous recharger (FCFA) ? "))
        if montant_recharge > 0:
            solde += montant_recharge
            print("\n✅ Recharge effectuée !")
            print(f"Votre nouveau solde est de {solde} FCFA\n")
        else:
            print("❌ Montant invalide !\n")
    except ValueError:
        print("❌ Entrée invalide, veuillez entrer un nombre.\n")


def passer_appel():
    """Simule un appel téléphonique"""
    global solde
    try:
        duree_appel = int(input("Durée de votre appel (minutes) ? "))
        if duree_appel > 0:
            cout = duree_appel * tarif_appel_minute
            print(f"\nCoût de l'appel : {duree_appel} minutes × {tarif_appel_minute} FCFA = {cout} FCFA")
            if solde >= cout:
                solde -= cout
                print("✅ Appel effectué !")
                print(f"Votre nouveau solde est de {solde} FCFA\n")
            else:
                manque = cout - solde
                print(f"❌ Crédit insuffisant ! Votre solde est de {solde} FCFA")
                print(f"Il vous manque {manque} FCFA\n")
        else:
            print("❌ Durée invalide !\n")
    except ValueError:
        print("❌ Entrée invalide, veuillez entrer un nombre.\n")


def envoyer_sms():
    """Simule l'envoi de SMS"""
    global solde
    try:
        nombre_sms = int(input("Combien de SMS voulez-vous envoyer ? "))
        if nombre_sms > 0:
            cout = nombre_sms * tarif_sms
            print(f"\nCoût des SMS : {nombre_sms} SMS × {tarif_sms} FCFA = {cout} FCFA")
            if solde >= cout:
                solde -= cout
                print("✅ SMS envoyés !")
                print(f"Votre nouveau solde est de {solde} FCFA\n")
            else:
                manque = cout - solde
                print(f"❌ Crédit insuffisant ! Votre solde est de {solde} FCFA")
                print(f"Il vous manque {manque} FCFA\n")
        else:
            print("❌ Nombre de SMS invalide !\n")
    except ValueError:
        print("❌ Entrée invalide, veuillez entrer un nombre.\n")


def afficher_menu():
    """Affiche le menu principal et retourne le choix de l'utilisateur"""
    print("=== MENU PRINCIPAL ===")
    afficher_solde()
    print("1. Acheter du crédit")
    print("2. Passer un appel")
    print("3. Envoyer des SMS")
    print("4. Voir mon solde")
    print("5. Quitter\n")

    choix = input("Votre choix : ")
    return choix


# --- Programme principal ---
print("=== GESTIONNAIRE DE CRÉDIT TÉLÉPHONIQUE ===\n")

demander_nom()

while True:
    choix = afficher_menu()

    if choix == "1":
        print("\n=== ACHAT DE CRÉDIT ===")
        acheter_credit()

    elif choix == "2":
        print("\n=== PASSER UN APPEL ===")
        passer_appel()

    elif choix == "3":
        print("\n=== ENVOYER DES SMS ===")
        envoyer_sms()

    elif choix == "4":
        afficher_solde()

    elif choix == "5":
        print(f"\nMerci d'avoir utilisé votre gestionnaire de crédit !")
        print(f"À bientôt {nom_utilisateur} 👋")
        break

    else:
        print("❌ Choix invalide, veuillez entrer un nombre entre 1 et 5.\n")
