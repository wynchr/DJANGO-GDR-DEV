# Importer les modules nécessaires pour utiliser la base de données Django
import os
import django
import csv

# Initialiser l'application Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GDR.settings')
django.setup()

# Importer le modèle d'utilisateurs de Django
from django.contrib.auth.models import User

# Ouvrir le fichier CSV
with open('./import_users_DEV.csv', 'r') as csvfile:
    # Lire les données du fichier CSV avec DictReader
    reader = csv.DictReader(csvfile)
    # Boucle sur chaque ligne du fichier CSV
    for row in reader:
        # Créer l'objet utilisateur en utilisant les données du fichier CSV
        user = User.objects.create_user(
            username=row['username'],
            first_name=row['prenom'],
            last_name=row['nom'],
            email=row['email'],
            password=row['password'],
            is_staff = row['is_staff']
        )
        # Enregistrer l'utilisateur dans la base de données
        user.save()
