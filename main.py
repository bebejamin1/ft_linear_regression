
# BONUS EXAMPLE
# Tracer les données dans un graphique afin de visualiser leur répartition.
# Tracer, dans le même graphique, la droite résultant de votre régression
# linéaire, pour voir le fruit de votre dur travail !
# Un programme qui calcule la précision de votre algorithme.

import os

from src.parsing import parser
from src.display import estimate_display, learning_display
# from src.prog import estimatePrice, learningRate


def dispatch(choice: any) -> None:
    os.system("clear")

    try:
        choice = int(choice)

    except ValueError:
        main()

    data, coord = parser("data/data.csv")

    if (choice == 1):
        estimate_display()

    if (choice == 2):
        learning_display(data)

    if (choice == 3):
        exit()

    main()


def main() -> None:
    os.system("clear")

    print("\n" + "Bienvenue sur ft_linear_regression".center(79, " ") + "\n\n")

    print("1. Estimer un prix")
    print("2. Entraîner le jeu de données")
    print("3. Quitter le programme" + "\n")

    choice = input("Faites votre choix: ")

    dispatch(choice)


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("tchao")
