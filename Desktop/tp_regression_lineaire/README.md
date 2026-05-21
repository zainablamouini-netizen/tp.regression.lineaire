# Projet de Régression Linéaire

## Description

Ce projet est un travail pratique (TP) sur la **régression linéaire** utilisant Python. Il démontre comment:
- Charger et explorer des données
- Créer un modèle de régression linéaire avec scikit-learn
- Évaluer le modèle avec des métriques (R², pente, ordonnée à l'origine)
- Visualiser les résultats avec matplotlib
- Faire des prédictions

### Exemple du projet
- **Données d'exemple**: Relation entre les heures d'étude et les notes obtenues
- **Dataset externe**: Fichier `data.csv` avec des données supplémentaires

---

## Prérequis

- **Python 3.7+**
- **pip** (gestionnaire de paquets Python)

---

## Installation

### 1. Cloner le dépôt (optionnel si vous avez déjà les fichiers)
```bash
git clone https://github.com/zainablamouini-netizen/tp.regression.lineaire.git
cd tp.regression.lineaire
```

### 2. Créer un environnement virtuel (recommandé)
```bash
python -m venv venv
```

**Activer l'environnement virtuel:**

**Sur Windows (PowerShell):**
```bash
venv\Scripts\Activate.ps1
```

**Sur Windows (CMD):**
```bash
venv\Scripts\activate.bat
```

**Sur Mac/Linux:**
```bash
source venv/bin/activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

Ou installez les packages manuellement:
```bash
pip install numpy pandas matplotlib scikit-learn
```

---

## Structure du projet

```
tp.regression.lineaire/
├── TP_regression.py           # Script principal Python
├── TP_regression.ipynb        # Notebook Jupyter (optionnel)
├── data.csv                   # Données pour l'exercice
├── copy_to_desktop.py         # Script utilitaire
└── README.md                  # Ce fichier
```

---

## Comment exécuter le programme

### Option 1: Exécuter le script Python
```bash
python TP_regression.py
```

Le script affichera:
- Des graphiques montrant la relation entre les données
- La droite de régression
- Les coefficients du modèle:
  - **Pente**: coefficient de la variable indépendante
  - **Ordonnée à l'origine**: valeur quand X = 0
  - **R² (Score)**: qualité d'ajustement du modèle (0 à 1, plus proche de 1 = meilleur)
- Une prédiction pour une valeur donnée

### Option 2: Exécuter avec Jupyter Notebook
```bash
jupyter notebook TP_regression.ipynb
```

Puis cliquez sur "Run All" pour exécuter toutes les cellules.

---

## Résultats attendus

Le programme générera:
1. **Graphique 1**: Nuage de points (heures d'étude vs notes)
2. **Graphique 2**: Droite de régression linéaire superposée aux données
3. **Affichage console**:
   ```
   Pente (coefficient) : 6.0
   Ordonnée à l'origine (intercept) : 44.0
   Coefficient de détermination R² : 0.9945
   Prédiction pour 4.5 heures : 71.0
   ```

---

## Concepts clés

- **Régression linéaire**: Modèle pour prédire une variable continue basée sur une ou plusieurs variables indépendantes
- **Coefficient (Pente)**: Indique comment Y change avec X
- **Intercept**: Valeur de Y quand X = 0
- **R² Score**: Proportion de la variance expliquée par le modèle (0-1)

---

## Dépannage

### Erreur: "ModuleNotFoundError: No module named 'sklearn'"
```bash
pip install scikit-learn
```

### Erreur: "No such file or directory: 'data.csv'"
Assurez-vous que le fichier `data.csv` se trouve dans le même répertoire que le script.

### Les graphiques ne s'affichent pas
Essayez d'ajouter cette ligne au début du script:
```python
import matplotlib
matplotlib.use('TkAgg')  # ou 'Qt5Agg'
```

---

## Licence

Libre d'utilisation à titre éducatif.

---

## Auteur

Zainab Lamouini

---

## Ressources

- [Scikit-learn Documentation](https://scikit-learn.org/)
- [NumPy Documentation](https://numpy.org/)
- [Matplotlib Documentation](https://matplotlib.org/)
