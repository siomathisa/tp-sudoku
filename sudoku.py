# Mathis VIDUEIRA et Ruben KABANGA MUYA

# --- Consigne ---
# Combien de noeuds pour résoudre un sudoku de 2x2 totalement vide ?
# Réponse : Pour la première case on a 4 possibilités, pour la deuxième 4x3, pour la troisème 4x3x2 et pour la dernière 4!
# ça fait 4 + 12 + 24 + 24 = 64 noeuds avec le backtracking car dans le pire des cas il doit explorer toutes les possibilités et
# donc recommencer plusieurs fois.

# Algorithme de backtracking pour résoudre une grille de sudoku nxn n<=9

# --- Grilles de test ---
# Grille exemple
grille_exemple = [
    [0, 0, 1, 0],
    [0, 0, 0, 3],
    [0, 0, 0, 2],
    [2, 0, 3, 0]
]
# Grille 9x9
grille_9x9 = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Génération grille 4x4 aléatoire
import random

def generate_4x4_sudoku():
    grid = [[0]*4 for _ in range(4)]
    clues = random.randint(4, 8) 
    filled = 0
    while filled < clues:
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        if grid[row][col] == 0:
            num = random.randint(1, 4)
            if (num not in grid[row] and
                num not in [grid[r][col] for r in range(4)] and
                num not in [grid[r][c] for r in range(row//2*2, row//2*2+2) 
                            for c in range(col//2*2, col//2*2+2)]):
                grid[row][col] = num
                filled += 1
    return grid

# --- Foncions ---

#fonction affichage de la grille
def afficher_grille(grille):
    for ligne in grille:
        for num in ligne:
            print(num, end=" ")
        print()
    print()


# verifier si un nombre peut être placé à la position (ligne, colonne)
def est_valide(grille, ligne, colonne, num):
    n = len(grille)
    # ligne
    for j in range(n):
        if grille[ligne][j] == num:
            return False
    # colonne
    for i in range(n):
        if grille[i][colonne] == num:
            return False
    # sous-bloc
    racine = int(n ** 0.5)
    debut_ligne = ligne - ligne % racine
    debut_col = colonne - colonne % racine
    for i in range(racine):
        for j in range(racine):
            if grille[debut_ligne + i][debut_col + j] == num:
                return False
    return True


# resoudre le sudoku en plaçant les nombres
def resoudre(grille):
    n = len(grille)
    for i in range(n):
        for j in range(n):
            if grille[i][j] == 0:
                for num in range(1, n+1):
                    if est_valide(grille, i, j, num):
                        grille[i][j] = num
                        if resoudre(grille):
                            return True
                        grille[i][j] = 0
                return False
    return True

# --- Tests ---

print("Grille Exemple :")
afficher_grille(grille_exemple)
if resoudre(grille_exemple):
    print("Grille résolue :")
    afficher_grille(grille_exemple)
else:
    print("Aucune solution trouvée.")

print("Grille 9x9 :")
afficher_grille(grille_9x9)
if resoudre(grille_9x9):
    print("Grille résolue :")
    afficher_grille(grille_9x9)
else:
    print("Aucune solution trouvée.")
    
print("Grille 4x4 aléatoire :")
grille_4x4 = generate_4x4_sudoku()
afficher_grille(grille_4x4)
if resoudre(grille_4x4):
    print("Grille résolue :")
    afficher_grille(grille_4x4)
else:
    print("Aucune solution trouvée.")