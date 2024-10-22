
import psycopg2
import random

# Connexion à la base de données PostgreSQL
try:
    conn = psycopg2.connect(
        dbname="goldenline_db",
        user="postgres",  
        password="Saida000",  
        host="localhost"
    )
    print("Connexion à la base de données réussie.")
except Exception as e:
    print(f"Erreur de connexion : {e}")
    exit()

cur = conn.cursor()

# Fonction pour insérer des données aléatoires dans la table clients
def insert_clients():
    try:
        print("Début de l'insertion des données dans la table clients...")
        for _ in range(10):  # Nombre d'enregistrements à insérer
            nb_enfants = random.randint(0, 4)
            categorie_socio = random.choice(["A", "B", "C", "D"])
            prix_panier_total = round(random.uniform(10, 500), 2)
            print(f"Insertion : nb_enfants={nb_enfants}, categorie_socio={categorie_socio}, prix_panier_total={prix_panier_total}")
            cur.execute("""
                INSERT INTO clients (nb_enfants, categorie_socioprofessionnelle, prix_panier_total, identifiant_collecte)
                VALUES (%s, %s, %s, %s)
            """, (nb_enfants, categorie_socio, prix_panier_total, random.randint(1, 1000)))
            conn.commit()
        print("Données insérées avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'insertion des données : {e}")

# Insérer des clients
insert_clients()

cur.close()
conn.close()
print("Connexion fermée.")

