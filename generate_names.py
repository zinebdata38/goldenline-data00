import pandas as pd
from faker import Faker

# Initialiser Faker
fake = Faker()

# Nombre de noms à générer
num_names = 100  # Remplace par le nombre de noms que tu souhaites

# Générer les noms et prénoms
data = {
    'Nom': [fake.last_name() for _ in range(num_names)],
    'Prénom': [fake.first_name() for _ in range(num_names)]
}

# Créer un DataFrame
df = pd.DataFrame(data)

# Sauvegarder dans un fichier CSV
df.to_csv('noms_prenoms.csv', index=False)
print("Fichier 'noms_prenoms.csv' créé avec succès !")

