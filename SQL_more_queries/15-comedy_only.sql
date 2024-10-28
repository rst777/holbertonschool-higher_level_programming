-- Ce script liste toutes les émissions de type "Comedy"
-- à partir de la base de données hbtn_0d_tvshows.
-- Chaque enregistrement affiche : tv_shows.title.
-- Les résultats sont triés par ordre croissant selon le titre de l'émission

SELECT ts.title
FROM tv_shows ts
JOIN tv_show_genres tsg ON ts.id = tsg.show_id
JOIN tv_genres tg ON tsg.genre_id = tg.id
WHERE tg.name = 'Comedy'
ORDER BY ts.title ASC;
