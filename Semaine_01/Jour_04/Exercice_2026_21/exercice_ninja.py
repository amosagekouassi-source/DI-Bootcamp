# =========================================================
# CONWAY'S GAME OF LIFE
# =========================================================

import random
import time


class GameOfLife:

    # -----------------------------------------------------
    # CONSTRUCTOR
    # -----------------------------------------------------
    def __init__(self, rows, cols):

        self.rows = rows
        self.cols = cols

        # Création grille aléatoire
        self.grid = [
            [random.randint(0, 1) for _ in range(cols)]
            for _ in range(rows)
        ]

    # -----------------------------------------------------
    # DISPLAY GRID
    # -----------------------------------------------------
    def display_grid(self):

        print("\n")

        for row in self.grid:

            for cell in row:

                # 1 = vivant
                if cell == 1:
                    print("⬛", end=" ")

                # 0 = mort
                else:
                    print("⬜", end=" ")

            print()

    # -----------------------------------------------------
    # COUNT NEIGHBORS
    # -----------------------------------------------------
    def count_neighbors(self, row, col):

        neighbors = 0

        # Toutes les directions possibles
        directions = [

            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        # Vérifie chaque voisin
        for dr, dc in directions:

            new_row = row + dr
            new_col = col + dc

            # Vérifie les bordures
            if (
                0 <= new_row < self.rows
                and
                0 <= new_col < self.cols
            ):

                neighbors += self.grid[new_row][new_col]

        return neighbors

    # -----------------------------------------------------
    # NEXT GENERATION
    # -----------------------------------------------------
    def next_generation(self):

        # Nouvelle grille vide
        new_grid = [

            [0 for _ in range(self.cols)]
            for _ in range(self.rows)
        ]

        # Parcours de chaque cellule
        for row in range(self.rows):

            for col in range(self.cols):

                alive_neighbors = self.count_neighbors(
                    row,
                    col
                )

                current_cell = self.grid[row][col]

                # -----------------------------------------
                # RÈGLES DU JEU
                # -----------------------------------------

                # cellule vivante
                if current_cell == 1:

                    # survit avec 2 ou 3 voisins
                    if alive_neighbors in [2, 3]:
                        new_grid[row][col] = 1

                    # sinon meurt
                    else:
                        new_grid[row][col] = 0

                # cellule morte
                else:

                    # naissance si exactement 3 voisins
                    if alive_neighbors == 3:
                        new_grid[row][col] = 1

        # Remplace ancienne grille
        self.grid = new_grid

    # -----------------------------------------------------
    # RUN GAME
    # -----------------------------------------------------
    def run(self, generations):

        for generation in range(generations):

            print(f"\nGeneration {generation + 1}")

            self.display_grid()

            self.next_generation()

            time.sleep(1)


# =========================================================
# START GAME
# =========================================================

game = GameOfLife(10, 10)

game.run(20)