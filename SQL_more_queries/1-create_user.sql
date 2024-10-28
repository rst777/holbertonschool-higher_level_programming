-- Vérifie si l'utilisateur existe déjà
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Accordez tous les privilèges à l'utilisateur
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Appliquez les changements
FLUSH PRIVILEGES;
