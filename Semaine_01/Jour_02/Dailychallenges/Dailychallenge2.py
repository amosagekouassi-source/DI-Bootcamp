#Daily challenge Gold : Solve the Matrix

import re

# 1. Définition de la chaîne Matrix d'origine
matrix_string = """711
Tsx
h%?
i #
sM 
$a 
#t%
^r!"""

# 2. Reproduction de la grille sous forme de liste 2D (Lignes et Colonnes)
# On sépare par ligne, puis chaque ligne est découpée en caractères
grid = [list(line) for line in matrix_string.split('\n') if line]

num_rows = len(grid)
num_cols = len(grid[0])

# 3. Lecture colonne par colonne (du haut vers le bas)
decoded_chars = []
for col in range(num_cols):
    for row in range(num_rows):
        decoded_chars.append(grid[row][col])

# On fusionne tous les caractères pour obtenir la chaîne brute
raw_message = "".join(decoded_chars)

# 4. Nettoyage du message secret avec des expressions régulières (Regex)
# Ce motif remplace les symboles situés UNIQUEMENT entre des caractères alphanumériques par un espace
secret_message = re.sub(r'(?<=\w)[^\w]+(?=\w)', ' ', raw_message)

# Affichage du résultat final
print(secret_message)
