# =========================================================
# ROCK PAPER SCISSORS - MINI PROJECT
# =========================================================

# Import du module random
# Il permet à l'ordinateur de choisir au hasard
import random


# =========================================================
# CLASS GAME
# =========================================================

class Game:

    # -----------------------------------------------------
    # Demande le choix du joueur
    # -----------------------------------------------------
    def get_user_item(self):

        # Liste des choix possibles
        valid_choices = ["rock", "paper", "scissors"]

        while True:

            # Demande utilisateur
            user_choice = input(
                "\nChoose rock, paper or scissors: "
            ).lower()

            # Vérification
            if user_choice in valid_choices:
                return user_choice

            print("Invalid choice. Try again.")

    # -----------------------------------------------------
    # Choix aléatoire de l'ordinateur
    # -----------------------------------------------------
    def get_computer_item(self):

        # Liste des choix possibles
        choices = ["rock", "paper", "scissors"]

        # random.choice choisit un élément au hasard
        return random.choice(choices)

    # -----------------------------------------------------
    # Déterminer le résultat
    # -----------------------------------------------------
    def get_game_result(self, user_item, computer_item):

        # Cas égalité
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

        # Sinon le joueur perd
        else:
            return "loss"

    # -----------------------------------------------------
    # Jouer une partie complète
    # -----------------------------------------------------
    def play(self):

        # Choix utilisateur
        user_item = self.get_user_item()

        # Choix ordinateur
        computer_item = self.get_computer_item()

        # Résultat
        result = self.get_game_result(
            user_item,
            computer_item
        )

        # Affichage des choix
        print(f"\nYou selected: {user_item}")
        print(f"Computer selected: {computer_item}")

        # Affichage résultat
        if result == "win":
            print("🎉 You won!")

        elif result == "loss":
            print("❌ You lost!")

        else:
            print("🤝 It's a draw!")

        # Retour du résultat
        return result


# =========================================================
# MENU FUNCTION
# =========================================================

def get_user_menu_choice():

    print("\n========================")
    print(" ROCK PAPER SCISSORS ")
    print("========================")

    print("P - Play a new game")
    print("S - Show scores")
    print("Q - Quit")

    choice = input("\nEnter your choice: ").lower()

    # Validation
    while choice not in ["p", "s", "q"]:
        choice = input("Invalid choice. Try again: ").lower()

    return choice


# =========================================================
# PRINT RESULTS
# =========================================================

def print_results(results):

    print("\n========================")
    print(" FINAL RESULTS ")
    print("========================")

    print(f"Wins  : {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws : {results['draw']}")

    print("\nThanks for playing! 👋")


# =========================================================
# MAIN FUNCTION
# =========================================================

def main():

    # Dictionnaire des scores
    results = {
        "win": 0,
        "loss": 0,
        "draw": 0
    }

    # Boucle principale
    while True:

        # Menu utilisateur
        choice = get_user_menu_choice()

        # -------------------------------------------------
        # Jouer une partie
        # -------------------------------------------------
        if choice == "p":

            # Création objet Game
            game = Game()

            # Lancer une partie
            result = game.play()

            # Mise à jour score
            results[result] += 1

        # -------------------------------------------------
        # Afficher scores
        # -------------------------------------------------
        elif choice == "s":

            print_results(results)

        # -------------------------------------------------
        # Quitter
        # -------------------------------------------------
        elif choice == "q":

            print_results(results)

            print("\nProgram closed.")
            break


# =========================================================
# START PROGRAM
# =========================================================

main()
