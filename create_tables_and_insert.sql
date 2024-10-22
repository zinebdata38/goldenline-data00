CREATE TABLE clients (
    id SERIAL PRIMARY KEY,
    nb_enfants INT,
    categorie_socioprofessionnelle VARCHAR(255),
    prix_panier_total DECIMAL,
    identifiant_collecte INT
);

CREATE TABLE collecte (
    id SERIAL PRIMARY KEY,
    id_client INT REFERENCES clients(id),
    categorie VARCHAR(255),
    prix DECIMAL
);

-- Insertion de données exemple
INSERT INTO clients (nb_enfants, categorie_socioprofessionnelle, prix_panier_total, identifiant_collecte)
VALUES (2, 'A', 150.75, 1);

INSERT INTO collecte (id_client, categorie, prix)
VALUES (1, 'alimentation', 50.25);


