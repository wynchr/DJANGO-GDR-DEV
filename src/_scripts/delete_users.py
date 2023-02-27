# Importer les modules nécessaires pour utiliser la base de données Django et le module CSV de Python
import os
import django
import csv

# Initialiser l'application Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GDR.settings')
django.setup()

# Importer le modèle d'utilisateurs de Django
from django.contrib.auth.models import User

# Ouvrir le fichier CSV
with open('./export_users_DEV.csv', 'r') as csvfile:
    # Lire les données du fichier CSV avec DictReader
    reader = csv.DictReader(csvfile)
    # Boucle sur chaque ligne du fichier CSV
    for row in reader:
        # Sélectionner l'utilisateur correspondant au nom d'utilisateur dans le fichier CSV
        user = User.objects.get(username=row['username'])
        # Supprimer l'utilisateur de la base de données
        user.delete()
