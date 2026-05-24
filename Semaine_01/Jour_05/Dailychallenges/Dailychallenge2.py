# =========================================================
# CHALLENGE 1 : SORTING
# =========================================================

# Demande utilisateur
words = input("Enter words separated by commas: ")

# Transforme la chaîne en liste
# strip() enlève les espaces inutiles
word_list = [word.strip() for word in words.split(",")]

# Tri alphabétique
sorted_words = sorted(word_list)

# Reconvertit la liste en chaîne
result = ",".join(sorted_words)

# Affichage
print(result)

# =========================================================
# CHALLENGE 2 : LONGEST WORD
# =========================================================

def longest_word(sentence):

    # Découpe la phrase en mots
    words = sentence.split()

    # On suppose que le premier mot est le plus long
    longest = words[0]

    # Parcours des mots
    for word in words:

        # Si mot plus long
        if len(word) > len(longest):
            longest = word

    return longest


# =========================================================
# TESTS
# =========================================================

print(longest_word("Margaret's toy is a pretty doll."))
print(longest_word("A thing of beauty is a joy forever."))
print(longest_word("Forgetfulness is by all means powerless!"))