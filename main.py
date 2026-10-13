
# BONUS EXAMPLE
# Tracer les données dans un graphique afin de visualiser leur répartition.
# Tracer, dans le même graphique, la droite résultant de votre régression
# linéaire, pour voir le fruit de votre dur travail !
# Un programme qui calcule la précision de votre algorithme.

from src.parsing import parser
# from src.prog import


def main() -> None:
    value = parser("data/data.csv")
    print(value)


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("tchao")
