# =========================================================
# GOOGLE TRANSLATOR EXERCISE
# =========================================================

# Import du traducteur
from googletrans import Translator

# Liste des mots français
french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]

# Création de l'objet Translator
translator = Translator()

# Dictionnaire résultat
translated_dict = {}

# =========================================================
# Boucle sur chaque mot
# =========================================================

for word in french_words:

    # Traduction du mot vers l'anglais
    translation = translator.translate(word, src="fr", dest="en")

    # Stockage dans le dictionnaire
    translated_dict[word] = translation.text

# =========================================================
# Affichage résultat
# =========================================================

print(translated_dict)