# parse le .csv
# verrifier la date de modification du fichier csv
# pour permettre de verifier que le jeu de donner nas pas changer depuis
# le dernier entrainement

# parser le theta


import csv
import pickle
import os

from pathlib import Path


def parser(filepath: str) -> dict:

    try:
        dir = Path("data")
        dir.mkdir(exist_ok=True)
        data_list = []
        with open(filepath, 'r') as fcsv:
            f = csv.DictReader(fcsv)

            for row in f:
                for k, v in row.items():
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

    return (data_list)


def create_theta_file(theta0: float, theta1: float) -> None:

    dir = Path("data")
    dir.mkdir(exist_ok=True)

    content = {"theta0": theta0, "theta1": theta1}

    with open("data/theta.pkl", "w") as f:
        pickle.dump(content, f)


def take_theta_file() -> dict:
    if not (os.path.exists("data/theta.pkl")):
        print("Lancez un learning rate avant tout")

    with
