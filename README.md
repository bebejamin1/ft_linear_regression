# 🚗 ft_linear_regression : Introduction au Machine Learning

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Linear%20Regression-success.svg)

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
* Calcul de la précision de l'algorithme (ex: calcul du coût ou du score de précision).

---

## ⚙️ Installation et Utilisation

Ce projet utilise **Python**. Les dépendances et l'environnement virtuel sont gérés via `pyproject.toml` et l'outil `uv` (ou `pip` classique).

### 1. Installation

Clonez le dépôt et installez les dépendances :

```bash
git clone <votre_repo>
cd ft_linear_regression
# Si vous utilisez uv (recommandé pour ce projet) :
uv sync
# Ou via pip classique :
pip install .
```

### 2. Entraîner le modèle

Lancez le programme d'entraînement pour lire les données et calculer les $\theta$ :

```bash
python -m linear_regression train data/data.csv
```
*(Ceci va générer et sauvegarder le fichier `data/theta.pkl` et afficher les graphiques de résultat).*

### 3. Prédire un prix

Lancez le programme de prédiction :

```bash
python -m linear_regression predict
```
Le programme vous demandera : `Veuillez entrer un kilométrage :`. Entrez un nombre et il vous retournera le prix estimé !

---

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
