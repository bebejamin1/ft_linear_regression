# graph sur le dataset de base
# graph sur le dataset avec la droite de régression linéaire

import matplotlib.pyplot as plt


# *****************************************************************************
# *                      make_graph_data_only()                               *
# *                                                                           *

def make_graph_data_only(data: list):
    """Enregistre les données SANS la droite de régression"""
    x = [row['km'] for row in data]
    y = [row['price'] for row in data]

    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color='blue', label='Données réelles')
    plt.xlabel('Kilométrage')
    plt.ylabel('Prix')
    plt.title('Données brutes (sans régression)')
    plt.legend()
    plt.grid(True)
    plt.savefig("img/dataset.png", dpi=300, bbox_inches='tight')
    plt.close()


# *****************************************************************************
# *                      make_graph_with_regression()                         *
# *                                                                           *

def make_graph_with_regression(data: list, theta0: float, theta1: float):
    """Enregistre les données AVEC la droite de régression"""
    x = [row['km'] for row in data]
    y = [row['price'] for row in data]

    # Dénormalisation
    theta0_denorm = theta0 * 10000.0
    theta1_denorm = theta1 * 0.1

    # Droite de régression
    x_min = min(x) - 20000
    x_max = max(x) + 20000
    x_line = [x_min, x_max]
    y_line = [theta0_denorm + theta1_denorm * x_min,
              theta0_denorm + theta1_denorm * x_max]

    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color='blue', label='Données réelles')
    plt.plot(x_line, y_line, color='red', label='Régression linéaire')
    plt.xlabel('Kilométrage')
    plt.ylabel('Prix')
    plt.title('Données avec régression linéaire')
    plt.legend()
    plt.grid(True)
    plt.savefig("img/with_regression.png", dpi=300, bbox_inches='tight')
    plt.close()
