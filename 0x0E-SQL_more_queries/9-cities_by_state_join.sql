-- lists all cities contained in the database hbtn_0d_usa.
SELECT cities.id, cities.name, states.name FROM states RIGHT JOIN cities ON cities.state_id = state.id;
