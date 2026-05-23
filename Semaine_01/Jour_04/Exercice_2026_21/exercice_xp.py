# Exercice 1 : Pets

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
class Siamese(Cat):

    def __init__(self, name, age, affectionate, faithful, talkative):
        super().__init__(name, age)

        self.a = affectionate
        self.f = faithful
        self.t = talkative

    def sing(self, sounds):
        return f'{sounds}'
    
    def attitude(self):
        a = self.a
        f = self.f
        t = self.t
        return f'{self.name} is very {a}, {f} and {t}'
    

Bengal_obj = Bengal('Milou', 5)
Chartreux_obj = Chartreux('Felix', 3)
Siamese_obj = Siamese('Luna', 2, True, True, True)

all_cats = [Bengal_obj, Chartreux_obj, Siamese_obj]

Sarah_pets = Pets(all_cats)

Sarah_pets.walk()

#Exercice 2 : Dogss

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} says: Woof!"

    def run_speed(self):

        return self.weight / self.age*10

    def fight(self, other_dog):
        
        if self.run_speed() > other_dog.run_speed():
            return f"{self.name} wins the fight!"
        else:
            return f"{other_dog.name} wins the fight!"


dog1 = Dog("Rex", 5, 30)
dog2 = Dog("Buddy", 3, 25)
dog3 = Dog("Max", 4, 45)

print(dog1.bark())
print(dog2.bark())
print(dog3.bark())

print(dog2.run_speed())
print(dog1.run_speed())
print(dog3.run_speed())

print(dog1.fight(dog2))
print(dog1.fight(dog3))
print(dog2.fight(dog3))


#Exercice 4 : Family and Person Classes

class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        return self.age >= 18


class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        new_person = Person(first_name, age)
        new_person.last_name = self.last_name
        self.members.append(new_person)

    def check_majority(self, first_name):
        for person in self.members:
            if person.first_name == first_name:

                if person.is_18():
                    print(
                        "You are over 18, your parents Jane and John accept that you will go out with your friends"
                    )
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return

        print("Person not found in the family.")

    def family_presentation(self):
        print(f"Family last name: {self.last_name}")

        for person in self.members:
            print(f"{person.first_name} is {person.age} years old")
