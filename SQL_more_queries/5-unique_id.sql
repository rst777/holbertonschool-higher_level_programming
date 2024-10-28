-- Utilise la base de données spécifiée
USE hbtn_0d_2;

-- Vérifie si la table unique_id existe déjà, sinon la crée
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
