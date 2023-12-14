import forex_python.converter as converter
from forex_python.converter import CurrencyRates
#import mmap

historique = open("historique.txt", "a")
   
   
def afficher_devises_disponibles(): # Fonction pour afficher les devises disponibles   
    # Créer une instance de CurrencyRates
    currency = CurrencyRates() 
    # Obtenir les taux de change
    rates = currency.get_rates('USD')  # Obtenez les taux par rapport à l'USD (vous pouvez utiliser une autre devise de base si nécessaire)
    # Extraire les devises à partir des taux de change
    currencies = list(rates.keys())
    # Afficher les devises disponibles
    for currency_code in currencies:
        print(currency_code)

def convertisseur(): # Fonction pour convertir les devises
    global monnaie_de_depart
    global monnaie_d_arrivee
    global montant_converti
    global montant
    print("Bienvenue dans le convertisseur de monnaie !")
    print("Veuillez entrer la devise de départ :")
    monnaie_de_depart = input()
    print("Veuillez entrer la devise d'arrivée :")
    monnaie_d_arrivee = input()
    print("Veuillez entrer le montant à convertir :")
    montant = input()
    taux = converter.get_rate(monnaie_de_depart, monnaie_d_arrivee) # Obtenir le taux de change # .get_rate() est une fonction de forex_python.converter
    montant_converti = float(montant) * taux
    print("Le montant converti est de " + str(montant_converti) + " " + monnaie_d_arrivee)

def historique_convertisseur(): # Fonction pour enregistrer l'historique des conversions
    global monnaie_de_depart
    global monnaie_d_arrivee
    global montant_converti
    global montant
    historique.write("Devise de depart : " + monnaie_de_depart + "\n")
    historique.write("Devise d'arrivee : " + monnaie_d_arrivee + "\n")
    historique.write("Montant de depart : " + montant + " " + monnaie_de_depart +"\n")
    historique.write("Montant converti : " + str(montant_converti) + " " + monnaie_d_arrivee + "\n")
    historique.write("----------------------------------------------------\n")
    #historique.close()

def menu(): # Fonction pour afficher le menu
    print("1. afficher les devises disponibles")
    print("2. convertir")
    print("3. afficher l'historique")
    print("4. quitter")
    choix = input("Que voulez-vous faire ?")
    if choix == "1":
        afficher_devises_disponibles()
        menu()
    elif choix == "2":
        convertisseur()
        historique_convertisseur()
        menu()
    elif choix == "3":
        historique = open("historique.txt", "r")
        print(historique.read())
        #historique.close()
        menu()
    elif choix == "4":
        exit()
    else:
        print("Veuillez entrer un choix valide")

menu() 