-- Ce script liste tous les genres de l'émission "Dexter"
-- à partir de la base de données hbtn_0d_tvshows.
-- Chaque enregistrement affiche : tv_genres.name.
-- Les résultats sont triés par ordre croissant selon le nom du genre.

SELECT tg.name
FROM tv_genres tg
JOIN tv_show_genres tsg ON tg.id = tsg.genre_id
JOIN tv_shows ts ON tsg.show_id = ts.id
WHERE ts.title = 'Dexter'
ORDER BY tg.name ASC;
