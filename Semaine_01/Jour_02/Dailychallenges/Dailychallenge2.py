from datetime import datetime

# 1. Demander la date de naissance
date_input = input("Please enter your birthdate (DD/MM/YYYY): ")

# 2. Convertir la saisie en objet "date" pour extraire facilement le jour, mois, année
birthdate = datetime.strptime(date_input, "%d/%m/%Y").date() if "/" in date_input else datetime.now().date()

# (On extrait l'année pour le calcul)
year = birthdate.year

# 3. Calculer l'âge actuel (basé sur l'année actuelle 2026)
current_year = 2026
age = current_year - year

# 4. Trouver le dernier chiffre de l'âge (ex: 53 -> 3)
# Astuce : Le "Modulo 10" (% 10) donne toujours le reste, donc le dernier chiffre !
num_candles = age % 10

# 5. Vérifier si l'année est bissextile (Leap Year)
# Règle : divisible par 4 mais pas par 100, OU divisible par 400
is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# 6. Dessiner le gâteau dynamiquement selon le nombre de bougies
candles = "|" * num_candles
spaces = " " * ((11 - num_candles) // 2)  # Pour centrer les bougies sur le gâteau

cake_art = f"""
{spaces}{candles}

      |     |      
    ============   

   |  ~  ~  ~  ~ | 
   |             | 
  ================="""

# 7. Affichage final (Un ou deux gâteaux !)
print(f"\nYou are {age} years old. Your cake gets {num_candles} candle(s):")

if is_leap_year:
    print("\nBonus: You were born on a leap year! Here are TWO cakes!")
    print(cake_art)
    print(cake_art)
else:
    print(cake_art)
