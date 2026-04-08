CREATE TABLE IF NOT EXISTS user (
	id_user INT AUTO_INCREMENT,
	username VARCHAR(50) NOT NULL,
	mail VARCHAR(100) NOT NULL UNIQUE,
	mdp text NOT NULL,
	PRIMARY KEY(id_user)
);

INSERT INTO user (id_user, username, mail, mdp) VALUES (1, 'titus', 'titus@gmail.com', 'titus32');