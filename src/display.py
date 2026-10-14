
import os

from prog import estimatePrice, learningRate
from parsing import create_theta_file
from tqdm import tqdm


# *****************************************************************************
# *                            estimate_display()                             *
# *                                                                           *

def check_int(value) -> int:
    try:
        value = int(value)
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

    print("\n" + f"Nous vous indiquons un prix de {price}€ pour {value}km")
    exit()


# *****************************************************************************
# *                         learning_display()                                *
# *                                                                           *


def learning_display(data: list) -> None:
    os.system("clear")

    print("\n" + "learningRate()".center(79, " ") + "\n\n")
    create_theta_file(0.0, 0.0)

    for _ in tqdm(range(10000000), desc="Training Process"):
        theta0, theta1 = learningRate(data)
        # print(theta0, theta1)
        create_theta_file(theta0, theta1)

    exit()
