-- Vérifie si la base de données existe déjà, sinon la crée
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Vérifie si l'utilisateur existe déjà, sinon le crée
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Accordez seulement le privilège SELECT sur la base de données hbtn_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Appliquez les changements
FLUSH PRIVILEGES;
