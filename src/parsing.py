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
        coord = set()

        with open(filepath, 'r') as fcsv:
            f = csv.DictReader(fcsv)

            for row in f:
                for k, v in row.items():
                    coord.add(k)
                    try:
                        if not (isinstance(v, int)):
                            row[k] = int(v)

                    except ValueError:
                        print(f"La valeur {k}: {v} n'est pas une INTEGER, par "
                              "conséquent cette valeur a été ignorée")

                data_list.append(row)

    except FileNotFoundError:
        print("Fichier introuvable !" + "\n"
              "Veuillez mettre un fichier .csv avec un jeu de données dans"
              "le dossier data")
        exit()

    return [data_list, tuple(coord)]


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

def take_theta_file() -> dict:
    if not (os.path.exists("data/theta.pkl")):
        print("\n" + "Lancez un learningRate avant tout !" + "\n"
              "Aucun fichier theta trouvé")
        exit()

    try:
        with open("data/theta.pkl", 'rb') as f:
            content = pickle.load(f)

    except Exception:
        print("Le fichier est corrompu, relancer un learningRate")
        exit()

    return (content)
