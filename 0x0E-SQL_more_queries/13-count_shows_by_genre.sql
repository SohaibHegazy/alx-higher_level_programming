-- a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_genre.name, COUNT(*) AS n
FROM tv_genre INNER JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genre.id
GROUP BY tv_genre.name
ORDER BY n DESC;
