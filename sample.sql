
CREATE TABLE IF NOT EXISTS users (
  user_id int(11) NOT NULL,
  username varchar(255),
  PRIMARY KEY (user_id)
);

INSERT INTO users (user_id, username) VALUES (1, "charl");