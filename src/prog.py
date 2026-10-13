
# PREMIER PROGRAMME: estimatePrice
# Au lancement du programme, il doit vous demander un kilométrage
# vous renvoyer le prix estimé pour ce kilométrage

# Le programme utilisera l'hypothèse suivante pour prédire le prix :
# estimatePrice(kilometrage) = ϑ0 + (ϑ1 * kilometrage)
# ϑ = theta (mesure d'un angle)

#  Avant l'exécution du programme d'entraînement, theta0 et theta1 seront
# initialisés à 0

def estimatePrice(value: int) -> None:
    pass


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

def learningRate() -> None:
    pass
