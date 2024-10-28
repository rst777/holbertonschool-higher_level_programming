-- Vérifie si la table force_name existe déjà, sinon la crée
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
