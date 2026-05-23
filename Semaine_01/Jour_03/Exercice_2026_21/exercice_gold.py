# =========================================================
# EXERCICE 1 : GEOMETRY - CIRCLE
# =========================================================

import math
import random


class Circle:

    def __init__(self, radius=1.0):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2

    def definition(self):
        print("A circle is a shape where all points are equidistant from the center.")


# Test Circle
c = Circle(5)
print("Perimeter:", c.perimeter())
print("Area:", c.area())
c.definition()


# =========================================================
# EXERCICE 2 : CUSTOM LIST CLASS
# =========================================================

class MyList:

    def __init__(self, letters):
        self.letters = letters
        self.length = len(letters)

    def reverse_list(self):
        return list(reversed(self.letters))

    def sort_list(self):
        return sorted(self.letters)

    def random_numbers_list(self):
        return [random.randint(0, 100) for _ in self.letters]


# Test MyList
list1 = MyList(["f", "t", "q", "h", "x", "c", "m"])

print("\nReverse:", list1.reverse_list())
print("Sort:", list1.sort_list())
print("Random numbers:", list1.random_numbers_list())


# =========================================================
# EXERCICE 3 : RESTAURANT MENU MANAGER
# =========================================================

class MenuManager:

    def __init__(self):
        self.menu = [
            {"name": "Soup", "price": 10, "spice": "B", "gluten": False},
            {"name": "Hamburger", "price": 15, "spice": "A", "gluten": True},
            {"name": "Salad", "price": 18, "spice": "A", "gluten": False},
            {"name": "French Fries", "price": 5, "spice": "C", "gluten": False},
            {"name": "Beef bourguignon", "price": 25, "spice": "B", "gluten": True},
        ]

    def add_item(self, name, price, spice, gluten):
        self.menu.append({
            "name": name,
            "price": price,
            "spice": spice,
            "gluten": gluten
        })
        print(f"{name} added to menu")

    def update_item(self, name, price, spice, gluten):
        for dish in self.menu:
            if dish["name"] == name:
                dish["price"] = price
                dish["spice"] = spice
                dish["gluten"] = gluten
                print(f"{name} updated")
                return
        print(f"{name} is not in the menu")

    def remove_item(self, name):
        for dish in self.menu:
            if dish["name"] == name:
                self.menu.remove(dish)
                print(f"{name} removed")
                print("Updated menu:", self.menu)
                return
        print(f"{name} is not in the menu")


# Test MenuManager
menu = MenuManager()

menu.add_item("Pizza", 12, "B", True)
menu.update_item("Soup", 11, "A", False)
menu.remove_item("Salad")