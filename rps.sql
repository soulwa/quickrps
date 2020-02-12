DROP TABLE IF EXISTS wins;

CREATE TABLE wins (
	id INTEGER PRIMARY KEY,
	count BIGINT NOT NULL,
	name TEXT NOT NULL
);

INSERT INTO wins (id, count, name)
VALUES
	(0, 0, "user"), 
	(1, 0, "cpu"),
	(2, 0, "ties");