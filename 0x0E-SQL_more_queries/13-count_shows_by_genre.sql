-- lists all genres from hbtn_0d_tvshows
SELECT tv_genres.name, COUNT(tv_show_genres.genre_id) FROM tv_genres RIGHT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id GROUP BY tv_genres.name ORDER BY COUNT(tv_show_genres.genre_id) DESC;
