import random

# ==========================================
# EXERCISE 1 & 2 : BIRTHDAYS LOOK-UP (ADVANCED)
# ==========================================

# Création du dictionnaire avec les dates de naissance
birthdays = {
    "Amos": "2002/04/15",
    "Marie": "1998/11/23",
    "Jean": "2000/01/05",
    "Lucas": "1995/07/19",
    "Sarah": "2001/12/30"
}

# Message d'accueil
print("Welcome to the birthday lookup system!")
print("You can look up the birthdays of the people in the list!")

# Exercice 2 : Affichage de tous les noms disponibles en premier
print("\nHere are the people we know:")
for name in birthdays.keys():
    print(f"- {name}")

# Demande du nom à l'utilisateur
search_name = input("\nGive me a person's name: ").strip()

# Vérification de la présence du nom (Exercice 2)
if search_name in birthdays:
    # Récupération et affichage de la date (Exercice 1)
    date_naissance = birthdays[search_name]
    print(f"Nicely-formatted message: {search_name}'s birthday is on {date_naissance}.")
else:
    # Message d'erreur si pas trouvé (Exercice 2)
    print(f"Sorry, we don’t have the birthday information for {search_name}.")


# ==========================================
# EXERCISE 3 : CHECK THE INDEX
# ==========================================

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

# Demande du nom à l'utilisateur
user_name = input("Enter your name to check its index: ").strip()

# Si le nom est dans la liste, on donne l'index de sa première occurrence
if user_name in names:
    first_index = names.index(user_name)
    print(f"The index of the first occurrence of '{user_name}' is {first_index}.")
else:
    print(f"'{user_name}' is not in the list.")


# ==========================================
# EXERCISE 4 : DOUBLE DICE
# ==========================================

# 1. Fonction qui simule le jet d'un dé (1 à 6)
def throw_dice():
    return random.randint(1, 6)

# 2. Fonction qui lance deux dés jusqu'à obtenir un double
def throw_until_doubles():
    throws_count = 0
    while True:
        dice1 = throw_dice()
        dice2 = throw_dice()
        throws_count += 1
        
        # Si on obtient un double, on s'arrête et on renvoie le nombre de lancers
        if dice1 == dice2:
            return throws_count

# 3. Fonction principale (Main)
def main():
    # On choisit une LISTE comme collection car on veut stocker 
    # et conserver tous les nombres de lancers un par un (doublons acceptés)
    results_collection = []
    
    # On appelle la fonction 100 fois pour obtenir 100 doubles
    for _ in range(100):
        total_throws_for_one_double = throw_until_doubles()
        results_collection.append(total_throws_for_one_double)
        
    # Calcul des statistiques finales
    total_throws = sum(results_collection)
    average_throws = total_throws / 100
    
    # Affichage des résultats demandés
    print(f"Total throws to reach 100 doubles: {total_throws}")
    print(f"Average throws to reach doubles: {average_throws:.2f}")

# Lancement de l'exercice des dés
main()
