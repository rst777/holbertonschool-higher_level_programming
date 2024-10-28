-- Vérifie si la table id_not_null existe déjà, sinon la crée
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
