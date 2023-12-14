import forex_python.converter as converter

historique = open("historique.txt", "a")

def convertisseur():
    global monnaie_de_depart
    global monnaie_d_arrivee
    global montant_converti
    print("Bienvenue dans le convertisseur de monnaie !")
    print("Veuillez entrer la monnaie de départ :")
    monnaie_de_depart = input()
    print("Veuillez entrer la monnaie d'arrivée :")
    monnaie_d_arrivee = input()
    print("Veuillez entrer le montant à convertir :")
    montant = input()
    taux = converter.get_rate(monnaie_de_depart, monnaie_d_arrivee)
    montant_converti = float(montant) * taux
    print("Le montant converti est de " + str(montant_converti) + " " + monnaie_d_arrivee)

def historique_convertisseur():
    global monnaie_de_depart
    global monnaie_d_arrivee
    global montant_converti
    historique.write("Monnaie de depart : " + monnaie_de_depart + "\n")
    historique.write("Monnaie d'arrivee : " + monnaie_d_arrivee + "\n")
    historique.write("Montant converti : " + str(montant_converti) + "\n" "\n")
    historique.close()

convertisseur()
historique_convertisseur()