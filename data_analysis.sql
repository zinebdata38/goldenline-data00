-- Requête 1 : Calcul de la dépense moyenne par catégorie socioprofessionnelle
SELECT categorie_socioprofessionnelle, AVG(prix_panier_total) AS depense_moyenne
FROM clients
GROUP BY categorie_socioprofessionnelle;

-- Requête 2 : Nombre de clients par catégorie socioprofessionnelle
SELECT categorie_socioprofessionnelle, COUNT(*) AS nombre_clients
FROM clients
GROUP BY categorie_socioprofessionnelle;

-- Requête 3 : Clients ayant dépensé plus de 200 euros
SELECT * 
FROM clients
WHERE prix_panier_total > 200;

-- Requête 4 : Dépense totale par nombre d'enfants
SELECT nb_enfants, SUM(prix_panier_total) AS depense_totale
FROM clients
GROUP BY nb_enfants;

-- Requête 5 : Liste des clients avec 3 enfants
SELECT * 
FROM clients
WHERE nb_enfants = 3;

