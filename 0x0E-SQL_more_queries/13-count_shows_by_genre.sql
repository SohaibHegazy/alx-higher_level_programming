-- a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_genre.name, COUNT(tv_show_genres.show_id) AS n
FROM INNER JOIN tv_genre, tv_show_genres
ON tv_show_genres.genre_id = tv_genre.name
GROUP BY tv_genre.name
ORDER BY n DESC;
