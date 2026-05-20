# Challenge 1

nombre = int(input("Entrez un nombre : "))
longueur = int(input("Entrez une longueur : "))

liste_multiples = []

for i in range(1, longueur + 1):
    multiple = nombre * i
    liste_multiples.append(multiple)  # Ajoute le multiple à la liste

print(liste_multiples)

# Challenge 2

texte_original = input("Entrez un texte : ")

texte_nettoye = ""

if texte_original:
    texte_nettoye += texte_original[0]

    for i in range(1, len(texte_original)):
        if texte_original[i] != texte_original[i - 1]:
            texte_nettoye += texte_original[i]

print(f"Résultat : {texte_nettoye}")

