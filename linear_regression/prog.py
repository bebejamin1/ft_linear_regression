
from .parsing import take_theta_file


# *****************************************************************************
# *                             estimatePrice()                               *
# *                                                                           *

def estimatePrice(value: int) -> int:
    result = 0

    theta0, theta1 = take_theta_file()

    if (theta0 == 0 or theta1 == 0):
        print("\n" + "Lancez un learningRate avant tout!" + "\n"
              "Vos valeurs theta sont à 0")
        exit()

    normalized_value = value / 100000.0
    normalized_result = theta0 + (theta1 * normalized_value)
    result = normalized_result * 10000.0

    return (int(result))


# *****************************************************************************
# *                             learningRate()                                *
# *                                                                           *

LEARNING_RATE = 0.01


def learningRate(data) -> tuple:
    m = len(data)
    somme0 = 0.0
    somme1 = 0.0
    theta0, theta1 = take_theta_file()

    for row in data:
        try:
            km = row['km'] / 100000.0
            price = row['price'] / 10000.0

        except KeyError:
            print("\n" + "Le data csv ne convient pas, veuillez le remplacer")
            exit()

        estimate = theta0 + theta1 * km
        erreur = estimate - price
        somme0 += erreur
        somme1 += erreur * km

    tmp0 = LEARNING_RATE * (1 / m) * somme0
    tmp1 = LEARNING_RATE * (1 / m) * somme1

    theta0 = theta0 - tmp0
    theta1 = theta1 - tmp1

    return (theta0, theta1)
