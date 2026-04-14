drop table if exists users;
CREATE TABLE IF NOT EXISTS users (
	id_user INT AUTO_INCREMENT,
	username VARCHAR(50) NOT NULL,
	email VARCHAR(100) NOT NULL UNIQUE,
	password text NOT NULL,
	PRIMARY KEY(id_user)
);

INSERT INTO users (id_user, username, email, password) VALUES (1, 'titus', 'titus@gmail.com', 'titus32');