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
def insert_clients(n):
    try:
        print(f"Début de l'insertion de {n} enregistrements dans la table clients...")
        for _ in range(n):  # Nombre d'enregistrements à insérer
            nb_enfants = random.randint(0, 4)
            categorie_socio = random.choice(["A", "B", "C", "D"])
            prix_panier_total = round(random.uniform(10, 500), 2)
            cur.execute("""
                INSERT INTO clients (nb_enfants, categorie_socioprofessionnelle, prix_panier_total, identifiant_collecte)
                VALUES (%s, %s, %s, %s)
            """, (nb_enfants, categorie_socio, prix_panier_total, random.randint(1, 1000)))
            conn.commit()
        print(f"Insertion de {n} enregistrements réussie.")
    except Exception as e:
        print(f"Erreur lors de l'insertion des données : {e}")

# Insérer 1000 clients
insert_clients(1000)

cur.close()
conn.close()
print("Connexion fermée.")
