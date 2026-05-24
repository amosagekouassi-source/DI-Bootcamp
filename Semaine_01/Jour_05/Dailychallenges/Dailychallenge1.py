# =========================================================
# CIRCLE CLASS
# =========================================================

import math


class Circle:

    # -----------------------------------------------------
    # CONSTRUCTOR
    # -----------------------------------------------------
    # Un cercle peut être créé avec :
    # - radius
    # OU
    # - diameter
    # -----------------------------------------------------
    def __init__(self, radius=None, diameter=None):

        # Si le rayon est donné
        if radius is not None:
            self.radius = radius

        # Sinon si le diamètre est donné
        elif diameter is not None:
            self.radius = diameter / 2

        # Valeur par défaut
        else:
            self.radius = 1

    # -----------------------------------------------------
    # PROPERTY : DIAMETER
    # -----------------------------------------------------
    # Le décorateur @property permet d'utiliser :
    # circle.diameter
    # au lieu de :
    # circle.diameter()
    # -----------------------------------------------------
    @property
    def diameter(self):
        return self.radius * 2

    # -----------------------------------------------------
    # AREA
    # -----------------------------------------------------
    def area(self):
        return math.pi * self.radius ** 2

    # -----------------------------------------------------
    # STRING REPRESENTATION
    # -----------------------------------------------------
    # Permet d'afficher l'objet proprement
    # -----------------------------------------------------
    def __str__(self):
        return (
            f"Circle(radius={self.radius}, "
            f"diameter={self.diameter})"
        )

    # -----------------------------------------------------
    # ADD TWO CIRCLES
    # -----------------------------------------------------
    # circle1 + circle2
    # -----------------------------------------------------
    def __add__(self, other):

        # Nouveau cercle avec somme des rayons
        new_radius = self.radius + other.radius

        return Circle(radius=new_radius)

    # -----------------------------------------------------
    # GREATER THAN
    # -----------------------------------------------------
    # circle1 > circle2
    # -----------------------------------------------------
    def __gt__(self, other):
        return self.radius > other.radius

    # -----------------------------------------------------
    # EQUAL
    # -----------------------------------------------------
    # circle1 == circle2
    # -----------------------------------------------------
    def __eq__(self, other):
        return self.radius == other.radius

    # -----------------------------------------------------
    # LESS THAN
    # -----------------------------------------------------
    # nécessaire pour sorted()
    # -----------------------------------------------------
    def __lt__(self, other):
        return self.radius < other.radius


# =========================================================
# TESTS
# =========================================================

# Création des cercles
c1 = Circle(radius=5)
c2 = Circle(diameter=10)
c3 = Circle(radius=2)

# ---------------------------------------------------------
# Affichage
# ---------------------------------------------------------
print(c1)
print(c2)

# ---------------------------------------------------------
# Aire
# ---------------------------------------------------------
print("Area c1:", c1.area())

# ---------------------------------------------------------
# Addition
# ---------------------------------------------------------
c4 = c1 + c3

print("New circle after addition:")
print(c4)

# ---------------------------------------------------------
# Comparaisons
# ---------------------------------------------------------
print("c1 > c3 :", c1 > c3)
print("c1 == c2 :", c1 == c2)

# ---------------------------------------------------------
# Sorting circles
# ---------------------------------------------------------
circles = [c1, c2, c3]

sorted_circles = sorted(circles)

print("\nSorted circles:")

for circle in sorted_circles:
    print(circle)