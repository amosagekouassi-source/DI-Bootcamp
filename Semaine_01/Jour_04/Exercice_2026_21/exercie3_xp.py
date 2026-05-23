#Chiens domestiqués
import random

from exercice_xp import Dog

class PetDog(Dog):
    def __init__(self, name, age, weight): 
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
         print(f"{self.name}, {', '.join(args)} are playing together")
        

    def do_a_trick(self): 
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            if self.trained:
                print(f"{self.name} {random.choice(tricks)}")


my_dog = PetDog("Fido", 2, 10)
my_dog.train()
my_dog.play("Buddy", "Max")
my_dog.do_a_trick()