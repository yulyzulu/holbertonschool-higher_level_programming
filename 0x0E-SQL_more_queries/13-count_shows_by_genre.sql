-- Script that lists all genres from hbtn_0d_tvshows and display the number of shows linked to each.
SELECT tv_genres.name as genre, COUNT(tv_show_genres.tv_show) as number_of_shows
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.show_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
