-- Crée la base de données hbtn_0d_usa seulement si elle n'existe pas déjà
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Utilise la base de données hbtn_0d_usa
USE hbtn_0d_usa;

-- Crée la table states seulement si elle n'existe pas déjà
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
