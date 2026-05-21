


# 1. Importer les bibliothèques
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import warnings
warnings.filterwarnings('ignore') # Pour éviter les warnings d'affichage lors des prédictions


# 2. Création d’un petit dataset
print("--- PARTIE COURS ---")
heures = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)
notes = np.array([50, 55, 65, 70, 75, 80])

plt.scatter(heures, notes)
plt.xlabel("Heures d'étude")
plt.ylabel("Note")
plt.title("Relation entre heures d'étude et note")
plt.show()


model = LinearRegression()
model.fit(heures, notes)


print("Pente (coefficient) :", model.coef_[0])
print("Ordonnée à l'origine (intercept) :", model.intercept_)
print("Coefficient de détermination R² :", model.score(heures, notes))


plt.scatter(heures, notes)
plt.plot(heures, model.predict(heures), color='red')
plt.xlabel("Heures d'étude")
plt.ylabel("Note")
plt.title("Droite de régression")
plt.show()

# 7. Faire une prédiction
pred = model.predict([[4.5]])
print("Prédiction pour 4.5 heures :", pred[0])
print("\n" + "="*50 + "\n")


# %% [markdown]
# # Exercices de Régression Linéaire

# %%
print("--- EXERCICE 1 : Modifier les données ---")
# Exercice 1 : Modifier les données
# Mes propres valeurs : impact du temps de sport sur la fréquence cardiaque au repos
heures_sport = np.array([0, 1, 2, 3, 4, 5, 6, 7]).reshape(-1, 1)
freq_cardiaque = np.array([80, 78, 75, 71, 68, 65, 62, 60])

# Tracer le scatter plot
plt.scatter(heures_sport, freq_cardiaque, color='green')
plt.xlabel("Heures de sport par semaine")
plt.ylabel("Fréquence cardiaque au repos")
plt.title("Ex 1 : Relation entre sport et fréquence cardiaque")

# Entraîner le modèle
model_ex1 = LinearRegression()
model_ex1.fit(heures_sport, freq_cardiaque)

# Tracer la droite
plt.plot(heures_sport, model_ex1.predict(heures_sport), color='red')
plt.show()

# Afficher la pente, l'intercept et le R²
print("Pente (coefficient) :", model_ex1.coef_[0])
print("Ordonnée à l'origine (intercept) :", model_ex1.intercept_)
print("Coefficient de détermination R² :", model_ex1.score(heures_sport, freq_cardiaque))
print("\n" + "="*50 + "\n")


# %%
print("--- EXERCICE 2 : Prédictions ---")
# Utilisation du modèle initial (Heures d'étude -> Note) pour prédire
heures_a_predire = [[2.5], [7], [0]]
predictions = model.predict(heures_a_predire)

print(f"Note prédite pour 2.5 heures d'étude : {predictions[0]:.2f}")
print(f"Note prédite pour 7 heures d'étude : {predictions[1]:.2f}")
print(f"Note prédite pour 0 heure d'étude : {predictions[2]:.2f}")
print("\n" + "="*50 + "\n")



# ### Exercice 3 : Interprétation du modèle
# 

# La pente (environ 6.14) représente l'augmentation moyenne de la note pour chaque heure d'étude supplémentaire. Autrement dit, une heure d'étude en plus rapporte en moyenne un peu plus de 6 points à l'examen.
# 


# L'ordonnée à l'origine (environ 44.28) représente la note théorique qu'obtiendrait un étudiant s'il étudiait 0 heure. C'est la valeur de base sans la variable explicative. Attention, dans la réalité, parfois les prédictions extrêmes (comme 0 heure) peuvent sortir du domaine de validité du modèle.
# 

# Le coefficient de détermination R² est d'environ 0.98. Ce résultat est excellent, car il est très proche de 1. Cela signifie que 98% de la variance des notes est expliquée par le nombre d'heures d'étude. Le modèle est donc très fiable pour ces données.


# %%
print("--- EXERCICE 4 : Ajouter du bruit aux données ---")
# Création d'un dataset plus réaliste avec du bruit
np.random.seed(42) # Pour assurer la reproductibilité

# Reprenons le même nombre d'heures, avec plus de valeurs
heures_bruit = np.random.uniform(0, 10, 50).reshape(-1, 1)

# Créons une note fictive générée autour de notre modèle précédent (44 + 6 * heures)
# + on ajoute un bruit aléatoire important (+/- 15 points max)
bruit = np.random.randint(-15, 15, size=50)
notes_bruit = (44.28 + 6.14 * heures_bruit.flatten()) + bruit

# Tracer le nouveau nuage de points
plt.scatter(heures_bruit, notes_bruit, alpha=0.7)
plt.title("Ex 4 : Données réalistes avec ajout de bruit")
plt.xlabel("Heures d'étude")
plt.ylabel("Note avec bruit")

# Ré-entraîner un nouveau modèle
model_bruit = LinearRegression()
model_bruit.fit(heures_bruit, notes_bruit)

# Tracer la nouvelle droite de régression
x_simul = np.linspace(0, 10, 100).reshape(-1, 1)
plt.plot(x_simul, model_bruit.predict(x_simul), color='red', linewidth=3)
plt.show()

# Comparer les valeurs de R² avant et après ajout du bruit
print(f"R² initial (sans bruit) : {model.score(heures, notes):.4f}")
print(f"R² avec du bruit      : {model_bruit.score(heures_bruit, notes_bruit):.4f}")
print("On observe que l'ajout de bruit diminue le R². Le modèle a plus de mal")
print("à capturer la variation des données à cause de la dispersion importante.")
print("\n" + "="*50 + "\n")


# %%
print("--- EXERCICE 5 : Dataset CSV ---")
# On importe le CSV qu'on a généré au préalable
csv_path = 'data.csv'
df = pd.read_csv(csv_path)

# Variables explicative et à prédire
X_csv = df[['X']] # DataFrame de format N,1
Y_csv = df['Y']

# Tracer le scatter plot
plt.scatter(X_csv, Y_csv, color='purple')
plt.xlabel("Variable Explicative (X)")
plt.ylabel("Variable à prédire (Y)")
plt.title("Ex 5 : Régression Linéaire sur Dataset CSV")

# Entraîner le modèle
model_csv = LinearRegression()
model_csv.fit(X_csv, Y_csv)

# Tracer la droite
plt.plot(X_csv, model_csv.predict(X_csv), color='orange', linewidth=2)
plt.show()

# Afficher la pente, l'intercept et le R²
print("Pente (coefficient) :", model_csv.coef_[0])
print("Ordonnée à l'origine (intercept) :", model_csv.intercept_)
print("Coefficient de détermination R² :", model_csv.score(X_csv, Y_csv))
print("\n" + "="*50 + "\n")
