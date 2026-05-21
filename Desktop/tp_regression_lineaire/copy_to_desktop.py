import shutil
import os

source = r"C:\Users\dell latitude 5520\.gemini\antigravity\scratch\tp_regression_lineaire"
dest = r"C:\Users\dell latitude 5520\Desktop\tp_regression_lineaire"

try:
    shutil.copytree(source, dest, dirs_exist_ok=True)
    print("Dossier copié sur le Bureau avec succès !")
except Exception as e:
    print("Erreur :", e)
