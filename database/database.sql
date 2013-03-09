SET SESSION storage_engine = "InnoDB";
ALTER DATABASE CHARACTER SET "utf8";

DROP TABLE IF EXISTS user;
CREATE TABLE user (
	id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
	username varchar(50) NOT NULL UNIQUE,
	email varchar(100) NOT NULL UNIQUE,
	password varchar(100) NOT NULL 
);

DROP TABLE IF EXISTS following;
CREATE TABLE following (
	id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
	user_id int NOT NULL REFERENCES user(id),
	follower_id int NOT NULL REFERENCES user(id)
);

DROP TABLE IF EXISTS linkgroup;
CREATE TABLE linkgroup (
	id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
	user_id int NOT NULL REFERENCES user(id),
	group_name varchar(200) NOT NULL,
	follower_count int NOT NULL DEFAULT 0 ,
	like_count int NOT NULL DEFAULT 0,
	links_count int NOT NULL DEFAULT 0,
	updated timestamp,
	created timestamp
);

DROP TABLE IF EXISTS link;
CREATE TABLE link (
	id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
	title varchar(200) NOT NULL,
	url varchar(300),
	url_domain varchar(200) NOT NULL,
	description varchar(500) ,
	comments_count int NOT NULL DEFAULT 0,
	like_count int NOT NULL DEFAULT 0,
	updated timestamp,
	created timestamp,
	group_id int NOT NULL REFERENCES linkgroup(id),
	KEY(created)
)