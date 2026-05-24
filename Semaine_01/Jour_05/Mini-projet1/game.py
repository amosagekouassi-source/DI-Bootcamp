# Import du module random pour permettre à l'ordinateur
# de choisir rock/paper/scissors au hasard
import random


# Création de la classe Game
class Game:

    # -----------------------------------------
    # Méthode pour demander le choix du joueur
    # -----------------------------------------
    def get_user_item(self):

        # Liste des choix autorisés
        valid_items = ["rock", "paper", "scissors"]

        while True:

            # Demande au joueur son choix
            user_choice = input(
                "Choose rock, paper or scissors: "
            ).lower()

            # Vérification que le choix est valide
            if user_choice in valid_items:
                return user_choice

            # Sinon on redemande
            print("Invalid choice, try again.")

    # -----------------------------------------
    # Méthode pour le choix aléatoire du PC
    # -----------------------------------------
    def get_computer_item(self):

        items = ["rock", "paper", "scissors"]

        # random.choice choisit un élément au hasard
        return random.choice(items)

    # -----------------------------------------
    # Déterminer le gagnant
    # -----------------------------------------
    def get_game_result(self, user_item, computer_item):

        # Cas d'égalité
        if user_item == computer_item:
            return "draw"

        # Cas où le joueur gagne
        elif (
            (user_item == "rock" and computer_item == "scissors")
            or
            (user_item == "paper" and computer_item == "rock")
            or
            (user_item == "scissors" and computer_item == "paper")
        ):
            return "win"

        # Sinon l'utilisateur perd
        else:
            return "loss"

    # -----------------------------------------
    # Jouer une partie complète
    # -----------------------------------------
    def play(self):

        # Récupération du choix utilisateur
        user_item = self.get_user_item()

        # Récupération du choix ordinateur
        computer_item = self.get_computer_item()

        # Détermination du résultat
        result = self.get_game_result(user_item, computer_item)

        # Affichage du résultat
        print(
            f"\nYou selected {user_item}."
            f"\nThe computer selected {computer_item}."
        )

        # Message selon le résultat
        if result == "win":
            print("You won!")

        elif result == "loss":
            print("You lost!")

        else:
            print("It's a draw!")

        # Retour du résultat
        return result