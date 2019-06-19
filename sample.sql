
CREATE TABLE IF NOT EXISTS users (
  user_id int(11) NOT NULL,
  username varchar(255),
  age int(10),
  PRIMARY KEY (user_id)
);

INSERT INTO users (user_id, username, age) VALUES (1, "charl", 4), (2, "ricky", 5);