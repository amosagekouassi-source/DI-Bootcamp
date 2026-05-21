import string

# ==========================================
# EXERCISE 1 : OUTPUTS (PREDICTIONS)
# ==========================================

# >>> 3 <= 3 < 9
# Prédiction : True (Car 3 est égal à 3, et 3 est plus petit que 9)
print(3 <= 3 < 9)

# >>> 3 == 3 == 3
# Prédiction : True (Toutes les valeurs sont égales entre elles)
print(3 == 3 == 3)

# >>> bool(0)
# Prédiction : False (En informatique, le chiffre 0 est toujours considéré comme faux)
print(bool(0))

# >>> bool(5 == "5")
# Prédiction : False (Un chiffre entier n'est pas égal à une chaîne de caractères)
print(bool(5 == "5"))

# >>> bool(4 == 4) == bool("4" == "4")
# Prédiction : True (Car True == True est vrai)
print(bool(4 == 4) == bool("4" == "4"))

# >>> bool(bool(None))
# Prédiction : False (None est vide, donc bool(None) vaut False, et bool(False) reste False)
print(bool(bool(None)))

x = (1 == True)   # True (En Python, True a mathématiquement la valeur 1)
y = (1 == False)  # False (False a la valeur 0)
a = True + 4      # 5 (True vaut 1, donc 1 + 4 = 5)
b = False + 10    # 10 (False vaut 0, donc 0 + 10 = 10)

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)


# ==========================================
# EXERCISE 2 : LONGEST WORD WITHOUT 'A'
# ==========================================

record_longueur = 0

while True:
    phrase = input("Entrez la plus longue phrase possible SANS la lettre 'A' (ou 'quit' pour stopper) : ")
    
    if phrase.lower().strip() == "quit":
        break
        
    # Vérifier si la lettre 'A' (majuscule ou minuscule) est dans la phrase
    if "a" in phrase.lower():
        print("Dommage ! Cette phrase contient la lettre 'A'. Essayez encore.")
    else:
        longueur_actuelle = len(phrase)
        # Vérifier si l'utilisateur bat son propre record
        if longueur_actuelle > record_longueur:
            record_longueur = longueur_actuelle
            print(f"Félicitations ! Nouveau record établi avec {record_longueur} caractères !")
        else:
            print(f"C'est correct (sans 'A'), mais trop court pour battre votre record de {record_longueur} caractères.")



# EXERCISE 3 : WORKING ON A PARAGRAPH

# Paragraphe choisi : Description de la programmation informatique
paragraphe = (
    "Programming is the process of creating a set of instructions that tells a computer how to perform a task. "
    "It can be done using a variety of computer programming languages, such as Python, Java, and C++. "
    "Learning to code opens up many job opportunities. Anyone can start today."
)

# 1. Nombre total de caractères
total_caracteres = len(paragraphe)

# 2. Nombre de phrases (on compte le nombre de points '.', d'interrogations '?' ou d'exclamations '!')
# Dans notre paragraphe simple, on compte les points terminant les phrases.
total_phrases = paragraphe.count(".") + paragraphe.count("?") + paragraphe.count("!")

# Préparation pour l'analyse des mots : on nettoie la ponctuation et on met en minuscules
texte_nettoye = paragraphe.translate(str.maketrans("", "", string.punctuation)).lower()
mots = texte_nettoye.split()

# 3. Nombre de mots
total_mots = len(mots)

# 4. Nombre de mots uniques
mots_uniques = set(mots)
total_mots_uniques = len(mots_uniques)

# BONUS 1 : Caractères sans les espaces
caracteres_sans_espace = len(paragraphe.replace(" ", ""))

# BONUS 2 : Moyenne de mots par phrase
moyenne_mots_phrase = total_mots / total_phrases if total_phrases > 0 else 0

# BONUS 3 : Nombre de mots qui apparaissent plus d'une fois
total_mots_doublons = total_mots - total_mots_uniques

# Affichage des résultats formatés
print(f"Paragraph analyzed:\n\"{paragraphe}\"\n")
print(f"-> Total characters: {total_caracteres}")
print(f"-> Total sentences: {total_phrases}")
print(f"-> Total words: {total_mots}")
print(f"-> Unique words: {total_mots_uniques}")
print(f"-> Bonus - Non-whitespace characters: {caracteres_sans_espace}")
print(f"-> Bonus - Average words per sentence: {moyenne_mots_phrase:.2f}")
print(f"-> Bonus - Non-unique words in paragraph: {total_mots_doublons}")
