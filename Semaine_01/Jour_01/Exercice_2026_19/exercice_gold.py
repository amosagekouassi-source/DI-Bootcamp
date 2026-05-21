#Exercise 1: What is the Season?

# On met un texte vide au début (index 0) pour que Janvier devienne le numéro 1 !

noms_mois = ["", "January", "February", "March", "April", "May", "June", 
             "July", "August", "September", "October", "November", "December"]

# Demander le numéro du mois à l'utilisateur

numero = int(input("Entrez le numéro du mois (1-12) : "))

# Récupérer le nom correspondant dans la liste

mois_choisi = noms_mois[numero]

Saison = ""

if numero in range(3, 5):
    saison = "Spring"
elif numero in range(6, 8):
    saison = "Summer"
elif numero in range(9, 11):
    saison = "Autumn"
else:
    saison = "Winter"
print(f"Le mois que vous avez choisi est {mois_choisi} et la saison correspondante est {saison}.")

#Exercise 2: For Loop

Number = range(1, 21)
for i in Number:
    print(i)

for j in range(1, 21):
    if j % 2 == 0:
        print(j)

#xercise 3: While Loop

mon_nom = "Amos"

while True:
    saisie = input("Entrez votre nom : ")
    
    if saisie == mon_nom:
        print("Félicitations, vous avez trouvé mon nom !")
        break 

#Exercise 4: Check the index

# 1. Notre liste de noms (avec des doublons pour l'exemple)
liste_noms = ["Jean", "Amos", "Marie", "Amos", "Lucas"]

# 2. Demander le nom à l'utilisateur
nom_recherche = input("Entrez votre nom : ")

# 3. Vérifier si le nom est dans la liste
if nom_recherche in liste_noms:
    # .index() trouve automatiquement l'indice de la PREMIÈRE fois où le nom apparaît
    indice = liste_noms.index(nom_recherche)
    print(f"Votre nom est dans la liste ! Sa première occurrence (apparition) est à l'indice : {indice}")
else:
    print("Votre nom ne figure pas dans la liste.")

#Exercise 5: Greatest Number

liste_nombres = []

# La boucle tourne exactement 3 fois (de 1 à 3)
for i in range(1, 4):
    nombre = int(input(f"Entrez le nombre n°{i} : "))
    liste_nombres.append(nombre)

# Affichage du résultat final
print(f"Le plus grand nombre est : {max(liste_nombres)}")


#Exercise 6: Random number

import random

# Initialisation des compteurs pour le Bonus 2
victoires = 0
defaites = 0

print("--- JEU DU NOMBRE MYSTÈRE ---")

# Boucle pour permettre de rejouer (Bonus 1)
while True:
    # 1. Demander un nombre à l'utilisateur
    saisie = input("\nDevinez un nombre entre 1 et 9 (ou tapez 'quit' pour quitter) : ")
    
    # Condition de sortie de la boucle
    if saisie.lower() == 'quit':
        break
        
    # Conversion de la saisie en nombre entier
    choix_utilisateur = int(saisie)
    
    # 2. Générer un nombre aléatoire entre 1 et 9 inclus
    nombre_mystere = random.randint(1, 9)
    
    print(f"Le nombre mystère était : {nombre_mystere}")
    
    # 3. Vérification du résultat
    if choix_utilisateur == nombre_mystere:
        print("“Winner”")
        victoires += 1  # Ajoute 1 victoire
    else:
        print("“Better luck next time.”")
        defaites += 1  # Ajoute 1 défaite

# 4. Affichage du bilan à la sortie de la boucle (Bonus 2)
print("\n--- FIN DE LA PARTIE ---")
print(f"Total de parties gagnées : {victoires}")
print(f"Total de parties perdues : {defaites}")
print("Merci d'avoir joué !")

