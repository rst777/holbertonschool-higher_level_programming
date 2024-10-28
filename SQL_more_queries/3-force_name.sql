-- Utilise la base de données spécifiée
USE hbtn_0d_2;

-- Vérifie si la table force_name existe déjà, sinon la crée
CREATE TABLE IF NOT EXISTS force_name (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
