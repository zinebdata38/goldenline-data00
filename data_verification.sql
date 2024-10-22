-- Requête 1 : Vérifier toutes les données insérées dans la table clients
SELECT * FROM clients;

-- Requête 2 : Vérifier si les clients ayant 3 enfants sont bien insérés
SELECT * 
FROM clients
WHERE nb_enfants = 3;

-- Requête 3 : Vérifier le nombre total de clients insérés
SELECT COUNT(*) AS nombre_clients
FROM clients;

-- Requête 4 : Vérifier la dépense moyenne par catégorie socioprofessionnelle
SELECT categorie_socioprofessionnelle, AVG(prix_panier_total) AS depense_moyenne
FROM clients
GROUP BY categorie_socioprofessionnelle;

-- Requête 5 : Lister tous les clients ayant dépensé plus de 200 euros
SELECT * 
FROM clients
WHERE prix_panier_total > 200;

