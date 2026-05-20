#Challenge 1: Letter Index Dictionary

# 1. Saisie utilisateur (User Input)
word = input("Veuillez entrer un mot : ")

# Initialisation du dictionnaire vide
letter_indices = {}

# 2. Création du dictionnaire (Creating the Dictionary)
# 'index' stocke la position (0, 1, 2...) et 'char' stocke la lettre
for index, char in enumerate(word):
    
    # Si le caractère est déjà une clé dans le dictionnaire
    if char in letter_indices:
        letter_indices[char].append(index)
        
    # Si le caractère n'est pas encore une clé
    else:
        letter_indices[char] = [index]

# 3. Affichage du résultat (Expected Output)
print(letter_indices)

#Challenge 2: Affordable Items

# --- 1. DONNÉES DE DÉPART (Exemple 1 du test) ---
items_purchase = {
    "Water": "$1", 
    "Bread": "$3", 
    "TV": "$1,000", 
    "Fertilizer": "$20"
}
wallet_str = "$300"

# --- 2. NETTOYAGE DES DONNÉES (Data Cleaning) ---
# Nettoyage et conversion du montant du portefeuille
wallet = int(wallet_str.replace("$", "").replace(",", ""))

# Initialisation du panier
basket = []

# --- 3. DÉTERMINATION DES ARTICLES ACCESSIBLES ---
# Boucle à travers le dictionnaire dans l'ordre de priorité fourni
for item, price_str in items_purchase.items():
    # Nettoyage du prix de l'article (retrait du symbole $ et des virgules)
    price = int(price_str.replace("$", "").replace(",", ""))
    
    # Vérification du budget restant
    if wallet >= price:
        basket.append(item)  # Ajout au panier
        wallet -= price      # Mise à jour du portefeuille

# --- 4. AFFICHAGE DES RÉSULTATS (Expected Output) ---
if not basket:
    print("Nothing")
else:
    # Tri par ordre alphabétique de la liste finale
    basket_sorted = sorted(basket)
    print(basket_sorted)
