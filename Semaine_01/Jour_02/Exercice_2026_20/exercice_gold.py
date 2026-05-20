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
