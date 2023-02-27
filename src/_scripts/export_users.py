# Importer les modules nécessaires pour utiliser la base de données Django et le module CSV de Python
import os
import django
import csv

# Initialiser l'application Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GDR.settings')
django.setup()

# Importer le modèle d'utilisateurs de Django
from django.contrib.auth.models import User

# Sélectionner tous les utilisateurs de la base de données Django
users = User.objects.all()

# Ouvrir un fichier CSV en mode écriture
with open('./export_users_DEV.csv', 'w', newline='') as csvfile:
    # Créer un objet writer pour écrire les données dans le fichier CSV
    writer = csv.writer(csvfile)
    # Écrire les en-têtes de colonnes dans le fichier CSV
    writer.writerow(['username', 'nom', 'prenom', 'email', 'password', 'is_staff'])
    # Écrire les données de chaque utilisateur dans le fichier CSV
    for user in users:
        writer.writerow([user.username, user.last_name, user.first_name, user.email, user.password, user.is_staff])

