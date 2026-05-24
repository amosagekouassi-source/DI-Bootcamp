# Import de la classe Game depuis game.py
from game import Game


# -------------------------------------------------
# Fonction affichant le menu utilisateur
# -------------------------------------------------
def get_user_menu_choice():

    print("\n----- MENU -----")
    print("(P) Play a new game")
    print("(S) Show scores")
    print("(Q) Quit")

    choice = input("Enter your choice: ").lower()

    # Validation du choix
    while choice not in ["p", "s", "q"]:
        choice = input("Invalid choice. Try again: ").lower()

    return choice


# -------------------------------------------------
# Affichage des résultats
# -------------------------------------------------
def print_results(results):

    print("\n----- GAME RESULTS -----")

    print(f"Wins : {results['win']}")
    print(f"Losses : {results['loss']}")
    print(f"Draws : {results['draw']}")

    print("\nThanks for playing!")


# -------------------------------------------------
# Fonction principale
# -------------------------------------------------
def main():

    # Dictionnaire des scores
    results = {
        "win": 0,
        "loss": 0,
        "draw": 0
    }

    # Boucle principale du programme
    while True:

        # Affichage menu
        choice = get_user_menu_choice()

        # -----------------------------
        # Jouer une partie
        # -----------------------------
        if choice == "p":

            # Création d'une nouvelle partie
            game = Game()

            # Lancement du jeu
            result = game.play()

            # Mise à jour des scores
            results[result] += 1

        # -----------------------------
        # Afficher les scores
        # -----------------------------
        elif choice == "s":

            print_results(results)

        # -----------------------------
        # Quitter le jeu
        # -----------------------------
        elif choice == "q":

            print_results(results)
            break


# Lancement du programme
main()