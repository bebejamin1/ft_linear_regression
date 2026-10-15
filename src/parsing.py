# parse le .csv
# parser le theta


import csv
import pickle
import os

from pathlib import Path


# *****************************************************************************
# *                               parser()                                    *
# *                                                                           *

def parser(filepath: str) -> list:

    try:
        dir = Path("data")
        dir.mkdir(exist_ok=True)
        data_list = []
        check = set()

        if not (os.path.exists("data/theta.pkl")):
            create_theta_file(0.0, 0.0)

        with open(filepath, 'r') as fcsv:
            f = csv.DictReader(fcsv)

            for row in f:
                for k in row.keys():
                    print()
                    check.add(k)

                if not (row.get("km") or row.get("price")):
                    continue

                km = row.get("km")
                price = row.get("price")

                try:
                    km = int(km)
                    price = int(price)

                except ValueError:
                    continue

                if (km < 0 or price < 0):
                    continue

                data_list.append({"km": km, "price": price})

    except FileNotFoundError:
        print("Fichier introuvable !" + "\n"
              "Veuillez mettre un fichier .csv avec un jeu de données dans"
              "le dossier data")
        exit()

    except Exception:
        print("\n" + "Le data.csv n'est pas conforme, les entêtes doivent être"
              " km et price" + "\n")
        exit()

    if (len(data_list) < 2):
        print("Le data.csv ne contient pas assez de données, minimum 2")
        exit()

    print

    if (check[0] != "km" or check[1] != "price"):
        print("\n" + "Le header du data.csv nest pas conforme"
              f"{check[0], check[1]} -> km, price" + "\n")
        exit()

    return (data_list)


# *****************************************************************************
# *                       create_theta_file()                                 *
# *                                                                           *

def create_theta_file(theta0: float, theta1: float) -> None:

    dir = Path("data")
    dir.mkdir(exist_ok=True)

    content = {"theta0": theta0, "theta1": theta1}

    with open("data/theta.pkl", "wb") as f:
        pickle.dump(content, f)


# *****************************************************************************
# *                        take_theta_file()                                  *
# *                                                                           *

def take_theta_file() -> tuple:
    if not (os.path.exists("data/theta.pkl")):
        print("\n" + "Lancez un learningRate avant tout !" + "\n"
              "Aucun fichier theta trouvé")
        exit()

    try:
        with open("data/theta.pkl", 'rb') as f:
            c = pickle.load(f)

    except Exception:
        print("Le fichier est corrompu, relancer un learningRate")
        exit()

    return (c["theta0"], c["theta1"])
