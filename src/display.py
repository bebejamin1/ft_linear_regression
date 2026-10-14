
import os

from prog import estimatePrice, learningRate
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
    value = input("Indiquez votre nombre de kilométrage: ")
    if (value == "exit"):
        exit()

    value = check_int(value)

    price = estimatePrice(value)

    print("\n" + f"Nous vous indiquons un prix de {price}€ pour {value}km")
    exit()


# *****************************************************************************
# *                         learning_display()                                *
# *                                                                           *


def learning_display() -> None:
    os.system("clear")

    print("\n" + "learningRate()".center(79, " ") + "\n\n")

    theta0, theta1 = 0
    for _ in tqdm(range(100), desc="Training Process"):
        learningRate()

    exit()
