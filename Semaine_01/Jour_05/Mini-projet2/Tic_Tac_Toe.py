# =========================================================
# TIC TAC TOE GAME
# =========================================================

# Le plateau sera une liste de 9 cases
# Chaque case contient :
# " " (vide)
# "X"
# "O"

board = [" " for _ in range(9)]


# =========================================================
# DISPLAY BOARD
# =========================================================

def display_board():

    print("\n")

    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")

    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")

    print(f" {board[6]} | {board[7]} | {board[8]} ")

    print("\n")


# =========================================================
# PLAYER INPUT
# =========================================================

def player_input(player):

    while True:

        try:
            # Demande une position
            position = int(
                input(f"Player {player}, choose position (1-9): ")
            )

            # Vérifie si la position est valide
            if position < 1 or position > 9:
                print("Position must be between 1 and 9")
                continue

            # Vérifie si la case est libre
            if board[position - 1] != " ":
                print("This position is already taken")
                continue

            # Retourne l'index correct
            return position - 1

        except ValueError:
            print("Please enter a number")


# =========================================================
# CHECK WIN
# =========================================================

def check_win(player):

    # Toutes les combinaisons gagnantes
    winning_combinations = [

        # lignes
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],

        # colonnes
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],

        # diagonales
        [0, 4, 8],
        [2, 4, 6]
    ]

    # Vérification de chaque combinaison
    for combo in winning_combinations:

        if (
            board[combo[0]] == player and
            board[combo[1]] == player and
            board[combo[2]] == player
        ):
            return True

    return False


# =========================================================
# CHECK DRAW
# =========================================================

def check_draw():

    # Si aucune case vide
    return " " not in board


# =========================================================
# PLAY GAME
# =========================================================

def play():

    # Joueur actuel
    current_player = "X"

    while True:

        # Affiche le plateau
        display_board()

        # Récupère position joueur
        position = player_input(current_player)

        # Place X ou O
        board[position] = current_player

        # Vérifie victoire
        if check_win(current_player):

            display_board()

            print(f"🎉 Player {current_player} wins!")
            break

        # Vérifie égalité
        if check_draw():

            display_board()

            print("🤝 It's a draw!")
            break

        # Changement de joueur
        if current_player == "X":
            current_player = "O"

        else:
            current_player = "X"


# =========================================================
# START GAME
# =========================================================

play()