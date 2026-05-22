class Farm:
    # Étape 2 : Implémenter la méthode __init__
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}  # Initialisation sous forme de dictionnaire vide

    # Étape 3 & Étape 8 (Bonus) : Mettre à jour la méthode add_animal
    # On utilise *args pour intercepter un appel classique (ex: 'cow', 5)
    # et **kwargs pour intercepter un appel par mots-clés (ex: cow=5, sheep=2)
    def add_animal(self, *args, **kwargs):
        # Cas 1 : Gestion de l'appel classique avec des arguments positionnels (*args)
        if args:
            animal_type = args[0]
            # Si le compte n'est pas fourni, sa valeur par défaut est 1
            count = args[1] if len(args) > 1 else 1
            
            # Injection dans le dictionnaire
            if animal_type in self.animals:
                self.animals[animal_type] += count
            else:
                self.animals[animal_type] = count
                
        # Cas 2 : Gestion du Bonus avec les mots-clés (**kwargs)
        for animal_type, count in kwargs.items():
            if animal_type in self.animals:
                self.animals[animal_type] += count
            else:
                self.animals[animal_type] = count

    # Étape 4 : Mettre en œuvre la méthode get_info
    def get_info(self):
        # En-tête de la chaîne
        info_str = f"{self.name}'s farm\n\n"
        
        # Parcours du dictionnaire pour lister les animaux
        for animal, count in self.animals.items():
            info_str += f"{animal} : {count}\n"
            
        # Ajout du slogan de fin
        info_str += f"\n    E-I-E-I-0!\n"
        return info_str

    # Étape 6 (Bonus) : Mettre en œuvre la méthode get_animal_types
    def get_animal_types(self):
        # Renvoie la liste des clés triée par ordre alphabétique
        return sorted(list(self.animals.keys()))

    # Étape 7 (Bonus) : Mettre en œuvre la méthode get_short_info
    def get_short_info(self):
        types_triés = self.get_animal_types()
        animaux_pluriel = []
        
        for animal in types_triés:
            # Si la quantité est supérieure à 1, on ajoute un "s" (en anglais)
            if self.animals[animal] > 1:
                animaux_pluriel.append(f"{animal}s")
            else:
                animaux_pluriel.append(animal)
        
        # Traduction syntaxique propre pour l'affichage en liste (ex: "vaches, chèvres et moutons")
        if len(animaux_pluriel) > 1:
            liste_formatee = ", ".join(animaux_pluriel[:-1]) + f" et {animaux_pluriel[-1]}"
        elif animaux_pluriel:
            liste_formatee = animaux_pluriel[0]
        else:
            liste_formatee = "aucun animal"
            
        return f"La ferme de {self.name} possède des {liste_formatee}."


# ==========================================
# ÉTAPE 5 : TEST DU CODE
# ==========================================

# 1. Création de l'objet de la ferme
macdonald = Farm("McDonald")

# 2. Ajout des animaux (Mélange de la méthode classique et du bonus **kwargs)
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')

# Test du Bonus Étape 8 : Ajout multiple via des variables nommées (Attention : pas de guillemets autour des clés dans les arguments !)
macdonald.add_animal(goat=12, duck=3) 

# 3. Affichage du résultat global (Étape 5)
print(macdonald.get_info())

# 4. Affichage des fonctionnalités Bonus (Étapes 6 & 7)
print("Types d'animaux présents (triés) :", macdonald.get_animal_types())
print(macdonald.get_short_info())
