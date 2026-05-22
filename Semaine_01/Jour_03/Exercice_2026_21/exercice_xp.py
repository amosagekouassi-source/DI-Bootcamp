# ==========================================
# EXERCICE 1 : LES CHATS
# ==========================================

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Étape 1 : Créer trois objets chat
cat1 = Cat("Félix", 3)
cat2 = Cat("Mistigri", 7)
cat3 = Cat("Garfield", 5)

# Étape 2 : Fonction pour trouver le chat le plus âgé
def find_oldest_cat(c1, c2, c3):
    # On met les chats dans une liste et on cherche celui qui a l'âge maximum
    liste_chats = [c1, c2, c3]
    le_plus_age = liste_chats[0]
    
    for chat in liste_chats:
        if chat.age > le_plus_age.age:
            le_plus_age = chat
            
    return le_plus_age

# Étape 3 : Imprimer les informations du chat le plus âgé
oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(f"Le chat le plus âgé est {oldest_cat.name}, et a {oldest_cat.age} ans.")


# ==========================================
# EXERCICE 2 : CHIENS
# ==========================================
# Étape 1 : Créer la classe Chien
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height  # Hauteur en cm
        
    def bark(self):
        print(f"{self.name} fait ouaf !")
        
    def jump(self):
        x = self.height * 2
        print(f"{self.name} saute {x} cm de haut !")

# Étape 2 : Créer des objets Chien
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Teckel", 20)

# Étape 3 : Imprimer les informations et appeler les méthodes
print(f"Chien de David : Nom = {davids_dog.name}, Taille = {davids_dog.height} cm")
davids_dog.bark()
davids_dog.jump()

print(f"Chien de Sarah : Nom = {sarahs_dog.name}, Taille = {sarahs_dog.height} cm")
sarahs_dog.bark()
sarahs_dog.jump()

# Étape 4 : Comparer la taille des chiens
if davids_dog.height > sarahs_dog.height:
    print(f"Le chien le plus grand est {davids_dog.name}.")
elif sarahs_dog.height > davids_dog.height:
    print(f"Le chien le plus grand est {sarahs_dog.name}.")
else:
    print("Les deux chiens ont la même taille !")


# ==========================================
# EXERCICE 3 : QUI EST LE PRODUCTEUR DE LA CHANSON ?
# ==========================================

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
        
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

# Test avec l'exemple fourni
stairway = Song([
    "There’s a lady who's sure", 
    "all that glitters is gold", 
    "and she’s buying a stairway to heaven"
])

stairway.sing_me_a_song()


# ==========================================
# EXERCICE 4 : APRÈS-MIDI AU ZOO
# ==========================================

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
        self.groups = {}  # Stockera le dictionnaire trié

    # BONUS : Gestion de plusieurs animaux séparés par des virgules ou via *args
    def add_animal(self, *new_animals):
        for animal_input in new_animals:
            # Gère les chaînes contenant des virgules (ex: "Lion, Tigre")
            sub_animals = [a.strip() for a in animal_input.split(",")]
            for animal in sub_animals:
                if animal not in self.animals and animal != "":
                    self.animals.append(animal)
                    print(f"{animal} a été ajouté au zoo.")
                elif animal in self.animals:
                    print(f"{animal} est déjà présent dans le zoo.")

    def get_animals(self):
        print(f"Animaux actuellement au zoo : {', '.join(self.animals)}")

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} a été vendu.")
        else:
            print(f"Impossible de vendre {animal_sold}, il n'est pas dans le zoo.")

    def sort_animals(self):
        # 1. Trier la liste principale par ordre alphabétique
        self.animals.sort()
        
        # 2. Vider et reconstruire le dictionnaire de groupes
        self.groups = {}
        for animal in self.animals:
            premiere_lettre = animal[0].upper()
            if premiere_lettre not in self.groups:
                self.groups[premiere_lettre] = []
            self.groups[premiere_lettre].append(animal)
        
        return self.groups

    def get_groups(self):
        print("\n--- Groupes d'animaux du Zoo ---")
        for lettre, liste_animaux in self.groups.items():
            print(f"{lettre}: {liste_animaux}")

# Étape 2 : Créer un objet Zoo
brooklyn_safari = Zoo("Brooklyn Safari")

# Étape 3 : Appel des méthodes pour tester
# Test du BONUS : On passe plusieurs animaux d'un coup, avec ou sans virgule
brooklyn_safari.add_animal("Giraffe", "Bear, Baboon")
brooklyn_safari.add_animal("Cougar", "Cat")
brooklyn_safari.add_animal("Zebra", "Lion")

print()
brooklyn_safari.get_animals()

print()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()

# Tri et affichage des groupes
brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()
