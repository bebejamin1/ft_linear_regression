
import os

from .prog import estimatePrice, learningRate
from .parsing import create_theta_file
from .graph import make_graph_data_only, make_graph_with_regression
from tqdm import tqdm


# *****************************************************************************
# *                            estimate_display()                             *
# *                                                                           *

def check_int(value) -> int:
    try:
        value = int(value)
        if (value < 0):
            raise ValueError()
    except ValueError:
        estimate_display()

    return (value)


def estimate_display() -> None:
    os.system("clear")

    print("\n" + "estimatePrice(value)".center(79, " ") + "\n\n")

    print("Écrivez exit pour quitter le programme")
    value = input("Indiquez votre nombre de kilométrage: ").rstrip("")

    if (value == "exit"):
        exit()

    value = check_int(value)

    price = estimatePrice(value)

    if (price <= 0):
        print("\n" + f"Votre voiture n'a plus de valeur avec {value}km")
        exit()

    print("\n" + f"Nous vous indiquons un prix de {price}€ pour {value}km")
    exit()


# *****************************************************************************
# *                         learning_display()                                *
# *                                                                           *


def learning_display(data: list) -> None:
    os.system("clear")

    print("\n" + "learningRate()".center(79, " ") + "\n\n")
    create_theta_file(0.0, 0.0)

    for _ in tqdm(range(10000), desc="Training Process"):
        theta0, theta1 = learningRate(data)
        create_theta_file(theta0, theta1)

    make_graph_data_only(data)
    make_graph_with_regression(data, theta0, theta1)

    print("\nEntraînement terminé! "
          f"Theta0: {theta0:.4f}, Theta1: {theta1:.4f}")
    exit()
