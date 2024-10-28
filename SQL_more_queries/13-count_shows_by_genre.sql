-- Ce script liste tous les genres de la base de données hbtn_0d_tvshows
SELECT tg.name AS genre, COUNT(tg.id) AS number_of_shows
FROM tv_genres tg
JOIN tv_show_genres tsg ON tg.id = tsg.genre_id
GROUP BY tg.id
ORDER BY number_of_shows DESC;
