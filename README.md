Projet GoldenLine
# Projet GoldenLine

Ce projet vise à développer une application permettant de gérer et analyser les tickets de caisse pour une entreprise fictive, GoldenLine. Le projet inclut la création d'une base de données relationnelle, l'insertion de données clients et de tickets de caisse, ainsi que la visualisation des données via une interface web interactive.

## Table des matières
1. [Introduction]
2. [Phases du projet]
   - 1. Création de la base de données
   - 2. Génération des données
   - 3. Insertion des données
   - 4. Visualisation des données
   - 5. Tests unitaires
3. [Fichiers du projet]
4. [Installation]
5. [Utilisation]
6. [Documentation]
7. [Tests]
8. [Contact]

## Introduction

GoldenLine est un projet qui permet de simuler les opérations d'un magasin vendant plusieurs catégories de produits (alimentation, vêtements, maison, hygiène) et d'analyser les habitudes de consommation des clients. L'objectif est de stocker les informations des clients et des tickets de caisse dans une base de données relationnelle, puis de visualiser ces informations à travers des graphiques.

---

## Phases du projet

### 1. Création de la base de données

La première phase consiste à créer la structure de la base de données. Cela inclut la conception des tables suivantes :
- **Client** : Informations sur les clients, incluant un identifiant unique, leur catégorie socioprofessionnelle (CSP), et le nombre d'enfants.
- **Ticket de Caisse** : Détails sur les achats réalisés par chaque client, incluant un identifiant, une référence client, une date d'achat, et le total du ticket.
- **Collecte** : Montants dépensés dans les différentes catégories de produits (alimentaire, vêtements, maison, hygiène).

Le fichier **`create_tables_and_insert_data.py`** contient le code Python pour créer ces tables dans une base de données SQLite.

### 2. Génération des données

Pour tester l'application, nous avons besoin de générer des données fictives. Cela inclut :
- La génération aléatoire de clients (nom, prénom, CSP, enfants).
- La création aléatoire de tickets de caisse et des montants associés pour chaque catégorie de produits.

Le fichier **`insert_data.py`** et **`insert_large_data.py`** sont utilisés pour générer et insérer ces données dans la base de données.

### 3. Insertion des données

Les données générées sont ensuite insérées dans la base de données à l'aide des scripts Python. Ces scripts créent des entrées pour chaque client, ticket de caisse et collecte de données. Ces informations sont stockées dans un fichier SQLite **`my_database.db`**.

### 4. Visualisation des données

Une fois les données stockées dans la base de données, nous utilisons **Flask** et **Streamlit** pour créer une interface web permettant de visualiser les informations :
- **Flask** pour afficher les tickets de caisse et les informations des clients.
- **Streamlit** pour afficher les graphiques dynamiques (répartition des dépenses, évolution des tickets, etc.).

Le fichier **`streamlit_app.py`** est utilisé pour lancer cette interface de visualisation.

### 5. Tests unitaires

Des tests unitaires ont été écrits pour valider le bon fonctionnement de l'application. Ces tests vérifient :
- La création correcte des tables dans la base de données.
- L'insertion des données sans erreurs.
- Le bon affichage des informations via l'interface web.

Le fichier **`test_app.py`** contient les tests unitaires basés sur le framework **unittest**.

---

## Fichiers du projet

- **`README.md`** : Ce fichier explicatif.
- **`Documentation Technique.txt`** : Contient les détails techniques et les justifications des choix d'implémentation.
- **`NOMS.csv`** et **`PRENOMS.csv`** : Fichiers de données utilisés pour générer les noms et prénoms aléatoires des clients.
- **`Projet_data_goldenline.ipynb`** : Un notebook Jupyter qui détaille les étapes du projet avec des explications et du code interactif.
- **`app_functions.py`** : Script Flask pour afficher les données des tickets de caisse.
- **`bdd_sqlite.ipynb`** : Un notebook Jupyter contenant du code pour interagir avec la base de données SQLite.
- **`my_database.db`** : Le fichier SQLite contenant les données des clients et des tickets de caisse.
- **`requirements.txt`** : Fichier listant les dépendances Python nécessaires au projet.
- **`streamlit_app.py`** : Script pour visualiser les données via Streamlit.
- **`test_app.py`** : Fichier de tests unitaires.

---

## Installation

1. **Cloner le dépôt GitHub** :
   ```bash
   git clone https://github.com/zinebdata38/goldenline-data00.git
