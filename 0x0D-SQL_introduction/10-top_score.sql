-- lists all records of the table second_table
SELECT score, name FROM second_table GROUP BY score ORDER BY MIN(score) DESC;
