# ft_linear_regression : Introduction au Machine Learning

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Linear%20Regression-success.svg)


## 🎬​ Preview
<img width="800" height="530" alt="ft_lr" src="https://github.com/user-attachments/assets/9a615372-728c-44c3-9b70-c2c4001bc747" />


Ce projet est une introduction aux concepts fondamentaux du **Machine Learning**. L'objectif est de créer un algorithme capable de **prédire le prix d'une voiture en fonction de son kilométrage**.

Pour ce faire, nous n'utilisons pas de bibliothèques mathématiques complexes toutes faites (comme `scikit-learn` ou `numpy.polyfit`). Nous implémentons nous-mêmes un algorithme d'apprentissage automatique basique : **la régression linéaire avec descente de gradient**.

---

## 🧠 Comprendre le projet (Explication simple)

Imaginez que vous vouliez vendre votre voiture. Vous regardez les annonces de voitures similaires et vous remarquez une règle logique : **plus la voiture a roulé (kilométrage élevé), moins elle est chère.**

Si nous plaçons ces données sur un graphique (Kilométrage en X, Prix en Y), nous obtenons un nuage de points :

<img width="1000" height="600" alt="dataset" src="https://github.com/user-attachments/assets/c5828012-86fc-4c4c-b6b9-5b3720572cf1" />
*Exemple de nos données : chaque point représente une voiture avec son kilométrage et son prix.*

**Le but du jeu (et de notre algorithme) :**
Trouver et tracer la "meilleure ligne droite" possible qui traverse ce nuage de points.
Une fois cette ligne tracée, si l'on me donne un nouveau kilométrage, je n'ai qu'à regarder où il tombe sur ma ligne pour deviner le prix !

<img width="1000" height="600" alt="with_regression" src="https://github.com/user-attachments/assets/ef02d7b3-6c76-4e52-9cd8-9dff271afece" />
*Notre algorithme a "appris" à tracer cette ligne rouge. C'est notre modèle prédictif.*

---

## 🛠️ Fonctionnalités du projet

Le projet est divisé en deux programmes distincts, conformément aux consignes :

1. **Le programme d'entraînement (Train) :**
   Il lit le fichier de données (`data.csv`), analyse les kilométrages et les prix, et "entraîne" le modèle. Il calcule les variables $\theta_0$ et $\theta_1$ (les coefficients de notre ligne droite) et les sauvegarde dans un fichier (`theta.pkl`).
2. **Le programme de prédiction (Predict) :**
   Il demande à l'utilisateur de saisir un kilométrage, charge les variables $\theta_0$ et $\theta_1$ précédemment calculées, et affiche le prix estimé. Si l'entraînement n'a pas encore été fait, les variables valent 0 et le prix estimé sera de 0.

**🌟 Bonus implémentés :**
* Affichage graphique des données (nuage de points).
* Affichage de la ligne de régression sur le graphique.

---

## ⚙️ Installation et Utilisation

Ce projet utilise **Python**. Les dépendances et l'environnement virtuel sont gérés via `pyproject.toml` et l'outil `uv` (ou `pip` classique).

### 1. Installation

Clonez le dépôt et installez les dépendances :

```bash
git clone https://github.com/bebejamin1/ft_linear_regression.git
cd ft_linear_regression
# Si vous utilisez uv (recommandé pour ce projet) :
uv sync
```

### 2. Lancer le projet

Lancez le programme et choisissez d'estimer un prix ou d'entraîner vos thêta :

```bash
uv run python3 -m linear_regression
```

## 🧮 Sous le capot : Les Mathématiques

Pour ceux qui veulent comprendre comment la machine "apprend", voici la logique mathématique.

### L'Hypothèse
Notre ligne droite est définie par une équation mathématique simple (l'équation d'une droite affine $y = ax + b$) :

$$estimatePrice(mileage) = \theta_0 + (\theta_1 * mileage)$$

*   $\theta_0$ (Thêta 0) : L'ordonnée à l'origine (le prix de base estimé si la voiture a 0 km).
*   $\theta_1$ (Thêta 1) : La pente de la ligne (la perte de valeur par kilomètre parcouru).

### L'Apprentissage : La Descente de Gradient
Au début, $\theta_0$ et $\theta_1$ valent `0`. La ligne est donc horizontale à zéro. Ce n'est pas bon.
Pour corriger cela, l'algorithme va calculer "l'erreur" (la différence entre le prix estimé par notre ligne actuelle et le prix réel dans nos données) et ajuster les $\theta$ pas à pas pour réduire cette erreur.

Voici les formules utilisées simultanément à chaque itération (boucle) :

$$tmp\theta_0 = learningRate * \frac{1}{m} \sum_{i=0}^{m-1} (estimatePrice(mileage[i]) - price[i])$$

$$tmp\theta_1 = learningRate * \frac{1}{m} \sum_{i=0}^{m-1} (estimatePrice(mileage[i]) - price[i]) * mileage[i]$$

*   $m$ : Le nombre total de voitures dans notre jeu de données.
*   $learningRate$ : La taille des "pas" que fait l'algorithme pour corriger son erreur. (Un pas trop grand et l'algorithme se perd, un pas trop petit et l'apprentissage est beaucoup trop long).

*(Note : Dans le code, les données sont normalisées avant d'appliquer ces formules afin d'éviter les dépassements de mémoire et d'accélérer l'apprentissage).*

### 1. Les données initiales (Le problème).
Tout commence par un jeu de données brut. Dans votre projet, il s'agit du kilométrage d'une voiture par rapport à son prix. Si l'on place ces données sur un graphique (ici, l'axe horizontal serait le kilométrage et l'axe vertical le prix), on obtient un nuage de points.
L'objectif de la régression linéaire est de trouver une tendance claire dans ce chaos apparent.
<img width="2752" height="1536" alt="1" src="https://github.com/user-attachments/assets/b439201f-0cfb-4203-9c39-fe2b2353b92c" />


### 2. La droite de régression (La solution)
La régression linéaire consiste à tracer la droite qui s'ajuste le mieux à tous ces points (la ligne de meilleur ajustement).
L'équation de cette droite est définie par votre hypothèse : Prix estimé = theta0 + (theta1 * kilométrage).
Une fois cette ligne rouge tracée, vous pouvez prédire la valeur d'un point (le prix) pour n'importe quelle valeur sur l'axe horizontal (le kilométrage), même si cette voiture n'existait pas dans votre jeu de données de base.
<img width="2752" height="1536" alt="2" src="https://github.com/user-attachments/assets/756de152-87b3-4772-91b4-4c5645bed84e" />


### 3. La descente de gradient (L'apprentissage)
Mais comment l'algorithme trouve-t-il la position parfaite pour cette ligne rouge ? Il utilise un concept appelé la Descente de Gradient.
Imaginez une vallée en forme de bol : la hauteur représente "l'erreur" de votre droite (la distance entre votre ligne et les vrais points de données).
L'algorithme démarre avec une ligne au hasard (en haut du bol, où l'erreur est très grande) et fait de petits pas vers le bas, en ajustant theta0 et theta1. Il s'arrête lorsqu'il atteint le fond du bol, ce qui correspond à l'erreur minimale. C'est à cet instant précis que la ligne rouge est parfaitement ajustée !
<img width="2752" height="1536" alt="3" src="https://github.com/user-attachments/assets/804acc30-303a-4b20-9493-dc6186905988" />

### 🔍 Exemple pas-à-pas : Comment la machine apprend-elle vraiment ?

Pour démystifier ces mathématiques, faisons "tourner" l'algorithme à la main sur sa toute première itération, avec un mini jeu de données de 3 voitures.
*(Pour simplifier la lecture : $x = 1$ signifie 10 000 km, $y = 8$ signifie 8 000 €).*

| 🚗 Voiture | Kilométrage ($x$) | Prix Réel ($y$) |
| :--- | :---: | :---: |
| **#1** | 1 | 8 |
| **#2** | 2 | 6 |
| **#3** | 3 | 4 |

**Conditions de départ :**
* $\theta_0 = 0$ et $\theta_1 = 0$ (L'algorithme n'a encore rien appris).
* Taux d'apprentissage (`learning_rate`) = $0.1$.

#### Étape 1 : Le constat des erreurs
L'algorithme teste sa formule actuelle `Prix estimé = 0 + (0 * km)` sur chaque voiture :

* **Voiture 1 :** Il prédit 0€. Elle en vaut 8. L'erreur est de **-8**.
* **Voiture 2 :** Il prédit 0€. Elle en vaut 6. L'erreur est de **-6**.
* **Voiture 3 :** Il prédit 0€. Elle en vaut 4. L'erreur est de **-4**.

Il additionne ensuite toutes ces erreurs (avec une pondération mathématique pour $\theta_1$).

#### Étape 2 : La correction (Le calcul du Gradient)
Une fois toutes les voitures analysées, l'algorithme utilise la somme de ses erreurs pour calculer comment corriger son tir. En appliquant les formules vues plus haut, il calcule des valeurs de correction temporaires :
* Correction pour $\theta_0$ : `-0.6`
* Correction pour $\theta_1$ : `-1.066`

#### Étape 3 : La mise à jour
L'algorithme met à jour ses connaissances (les fameux $\theta$) en y soustrayant ces corrections :
* Nouveau $\theta_0 = 0 - (-0.6) = \mathbf{0.6}$
* Nouveau $\theta_1 = 0 - (-1.066) = \mathbf{1.066}$

**🎉 Fin de la première boucle (Epoch 1) !**
L'algorithme a compris que ses prix étaient trop bas. Pour son prochain passage, sa formule de prédiction ne sera plus `0 + (0 * km)`, mais `0.6 + (1.066 * km)`.
Il va répéter cette boucle de constat/correction des milliers de fois, jusqu'à ce que son erreur soit la plus proche possible de zéro !


---

## 📂 Structure du code

```text
ft_linear_regression/
├── README.md               # Ce fichier
├── pyproject.toml / uv.lock# Fichiers de configuration Python
├── data/
│   ├── data.csv            # Le jeu de données fourni (kilométrage, prix)
│   └── theta.pkl           # Fichier généré contenant les poids du modèle
├── img/
│   ├── dataset.png         # Image d'illustration des données
│   └── with_regression.png # Image d'illustration du résultat
└── linear_regression/      # Code source du projet
    ├── __init__.py
    ├── __main__.py         # Point d'entrée du programme
    ├── display.py          # Gestion de l'affichage graphique (Bonus)
    ├── graph.py            # Logique de création des graphiques (Bonus)
    ├── parsing.py          # Lecture et validation du fichier CSV
    └── prog.py             # Algorithme de descente de gradient et prédiction
