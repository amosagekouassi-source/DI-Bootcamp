#Exercise 1: Converting Lists into Dictionaries

# Listes de départ
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# Conversion en dictionnaire
result_dict = dict(zip(keys, values))

# Affichage du résultat
print(result_dict)

#Exercise 2: Cinemax #2

# Données de la famille
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

total_cost = 0

# Boucle à travers le dictionnaire
for name, age in family.items():
    # Application des règles de tarification
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
        
    # Affichage du prix par membre
    print(f"Ticket pour {name.capitalize()} ({age} ans) : {price}$")
    total_cost += price

# Affichage du coût total
print(f"\nCoût total pour la famille : {total_cost}$")

#Exercise 3: Zara

# 1. Création du dictionnaire brand avec les données fournies
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

# 2. Modification du nombre de magasins à 2
brand["number_stores"] = 2

# 3. Impression d'une phrase décrivant les clients de Zara
clients = ", ".join(brand["type_of_clothes"])
print(f"Zara s'adresse à différents types de clients : {clients}.")

# 4. Ajout de la clé country_creation avec la valeur Spain
brand["country_creation"] = "Spain"

# 5. Vérification et ajout de "Desigual" aux concurrents
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

# 6. Suppression de la clé creation_date
del brand["creation_date"]

# 7. Impression du dernier élément de international_competitors
print(f"Dernier concurrent de la liste : {brand['international_competitors'][-1]}")

# 8. Impression des couleurs majeures aux États-Unis (US)
print(f"Couleurs majeures aux USA : {brand['major_color']['US']}")

# 9. Impression du nombre de clés dans le dictionnaire
print(f"Nombre total de clés : {len(brand)}")

# 10. Impression de toutes les clés du dictionnaire
print(f"Liste des clés : {list(brand.keys())}")

#Exercise 4 : Some Geography

# Étape 1 & 2 : Définition de la fonction avec un paramètre par défaut
def describe_city(city, country="Unknown"):
    # Affichage du message formaté
    print(f"{city} is in {country}.")

# Étape 3 : Appels de la fonction
# Appel avec les deux arguments fournis
describe_city("Reykjavik", "Iceland")

# Appel sans le paramètre 'country' pour tester la valeur par défaut
describe_city("Paris")

#Exercise 5 : Random

# Étape 1 : Importer le module random
import random

# Étape 2 : Définir la fonction avec un paramètre
def compare_to_random(user_number):
    # Étape 3 : Générer un nombre aléatoire entre 1 et 100
    random_number = random.randint(1, 100)
    
    # Étape 4 : Comparer les deux nombres
    if user_number == random_number:
        print("Success!")
    else:
        print(f"Fail! Your number: {user_number}, Random number: {random_number}")

# Étape 5 : Appeler la fonction avec un nombre entre 1 et 100
compare_to_random(58)

#  Exercise 6 : Let’s create some personalized shirts !

# Étape 1, 2 & 4 : Définition de la fonction avec les valeurs par défaut
def make_shirt(size="large", text="I love Python"):
    # Affichage du message récapitulatif
    print(f"The size of the shirt is {size} and the text is {text}.")

# Étape 5 : Appels de la fonction avec valeurs par défaut et personnalisées

# T-shirt large avec le message par défaut
make_shirt()

# T-shirt médium avec le message par défaut
make_shirt(size="medium")

# T-shirt de n'importe quelle taille avec un message personnalisé
make_shirt("small", "Custom message.")

# Étape 6 (Bonus) : Appel en utilisant explicitement les arguments nommés (Keyword Arguments)
make_shirt(size="small", text="Hello!")

# Exercise 7 : Temperature Advice

import random

# Étape 1 & Étape 4 (Bonus) & Étape 5 (Bonus)
def get_random_temp(season):
    """Génère une température à virgule flottante selon la saison choisie."""
    if season == "hiver":
        return round(random.uniform(-10.0, 5.0), 1)
    elif season == "printemps":
        return round(random.uniform(5.0, 20.0), 1)
    elif season == "été":
        return round(random.uniform(20.0, 40.0), 1)
    else:  # automne
        return round(random.uniform(0.0, 15.0), 1)

# Étape 2, 3 & 5
def main():
    # Étape 5 (Bonus) : Demande du mois à l'utilisateur
    try:
        month = int(input("Entrez le numéro du mois actuel (1-12) : "))
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        return

    # Détermination de la saison en fonction du mois
    if month in [12, 1, 2]:
        season = "hiver"
    elif month in [3, 4, 5]:
        season = "printemps"
    elif month in [6, 7, 8]:
        season = "été"
    elif month in [9, 10, 11]:
        season = "automne"
    else:
        print("Mois invalide. Choix par défaut : été.")
        season = "été"

    # Appel de la fonction pour obtenir la température
    temperature = get_random_temp(season)
    
    # Étape 2 : Affichage de la température
    print(f"\nThe temperature right now is {temperature} degrees Celsius.")
    
    # Étape 3 : Conseils basés sur la température
    if temperature < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif 0 <= temperature < 16:
        print("Quite chilly! Don't forget your coat.")
    elif 16 <= temperature < 24:
        print("Nice weather.")
    elif 24 <= temperature < 32:
        print("A bit warm, stay hydrated.")
    else:
        print("It's really hot! Stay cool.")

# Exécution du programme principal
if __name__ == "__main__":
    main()

# Exercise 8: Pizza Toppings

# Initialisation des variables
toppings = []
base_price = 10.0
topping_price = 2.50

print("Entrez vos garnitures de pizza (tapez 'quit' pour terminer) :")

# Boucle interactive
while True:
    user_input = input("Garniture : ").strip()
    
    # Condition de sortie
    if user_input.lower() == 'quit':
        break
        
    # Ajout de la garniture et affichage du message
    toppings.append(user_input)
    print(f"Adding {user_input} to your pizza.")

# Calcul du coût total
total_cost = base_price + (len(toppings) * topping_price)

# Affichage du récapitulatif final
print("\n--- Votre commande ---")
if toppings:
    print(f"Garnitures choisies : {', '.join(toppings)}")
else:
    print("Aucune garniture (Pizza nature)")

print(f"Prix total : {total_cost:.2f}$")
