-- Ce script liste toutes les émissions et tous les genres liés à chaque émission
-- à partir de la base de données hbtn_0d_tvshows.
-- Chaque enregistrement affiche : tv_shows.title - tv_genres.name.
-- Si une émission n'a pas de genre, NULL sera affiché dans la colonne genre.
-- Les résultats sont triés par ordre croissant selon le titre de l'émission et le nom du genre.

SELECT ts.title, tg.name
FROM tv_shows ts
LEFT JOIN tv_show_genres tsg ON ts.id = tsg.show_id
LEFT JOIN tv_genres tg ON tsg.genre_id = tg.id
ORDER BY ts.title ASC, tg.name ASC;
