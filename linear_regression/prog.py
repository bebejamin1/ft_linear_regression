
# PREMIER PROGRAMME: estimatePrice
# Au lancement du programme, il doit vous demander un kilométrage
# vous renvoyer le prix estimé pour ce kilométrage

# Le programme utilisera l'hypothèse suivante pour prédire le prix :
# estimatePrice(kilometrage) = ϑ0 + (ϑ1 * kilometrage)
# ϑ = theta (mesure d'un angle)

#  Avant l'exécution du programme d'entraînement, theta0 et theta1 seront
# initialisés à 0

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

# DEUXIEME PROGRAMME: learningRate
# Il lira votre fichier de données et effectuera une régression linéaire sur les données.  # noqa
# Une fois la régression linéaire terminée
# vous sauvegarderez les variables theta0 et
# theta1 afin de les utiliser dans le premier programme.

# Vous utiliserez les formules suivantes :
# tmpϑ0 = learningRate * (1/m) Σi=0 m-1 (estimatePrice(kilometrage[i]) - prix[i])  # noqa
# tmpϑ1 = learningRate * (1/m) Σi=0 m-1 (estimatePrice(kilometrage[i]) - prix[i]) * kilometrage[i]  # noqa

# x = km
# y = price
# m = nbr dans le jeu de donner
# Σ = sigma beux dire somme


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
