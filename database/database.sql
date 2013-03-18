SET SESSION storage_engine = "InnoDB";
ALTER DATABASE CHARACTER SET "utf8";

DROP TABLE IF EXISTS user;
CREATE TABLE user (
	id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
	username varchar(50) NOT NULL UNIQUE,
	email varchar(100) NOT NULL UNIQUE,
	password varchar(100) NOT NULL ,
	introduction varchar(300), 
    follower_count int NOT NULL DEFAULT 0 
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
    created timestamp,
    private int NOT NULL DEFAULT 0
);

DROP TABLE IF EXISTS link;
CREATE TABLE link (
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    title varchar(200) NOT NULL,
    url varchar(300) NOT NULL,
    url_domain varchar(200) NOT NULL,
    description varchar(500) ,
    comments_count int NOT NULL DEFAULT 0,
    like_count int NOT NULL DEFAULT 0,
    updated timestamp,
    created timestamp,
    group_id int NOT NULL REFERENCES linkgroup(id),
    KEY(created)
);

DROP TABLE IF EXISTS following_user;
CREATE TABLE following_user (
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user_id int NOT NULL REFERENCES user(id),
    follower_id int NOT NULL REFERENCES user(id)
);

DROP TABLE IF EXISTS following_group;
CREATE TABLE following_group (
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user_id int NOT NULL REFERENCES user(id),
    group_id int NOT NULL REFERENCES linkgroup(id)
);

DROP TABLE IF EXISTS comment;
CREATE TABLE comment (
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    content varchar(500),
    user_id int NOT NULL REFERENCES user(id),
    link_id int NOT NULL REFERENCES link(id),
    created timestamp
);
