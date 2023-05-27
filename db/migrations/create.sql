use chat;

CREATE TABLE users (
    id int NOT NULL,
    username VARCHAR(255) NOT NULL,
    firstName VARCHAR(255),
    lastName VARCHAR(255),
    pw VARCHAR(255) NOT NULL,
    birthday DATE,
    email VARCHAR(255),
    PRIMARY KEY (id)
);

CREATE TABLE messages (
    id int NOT NULL,
    isGroup int NOT NULL,
    threadId int NOT NULL,
    sender int NOT NULL,
    content VARCHAR(255) NOT NULL,
    timeSent DATE NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE threads (
    id int NOT NULL,
    user1 int NOT NULL,
    user2 int NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE groupThreads (
    id int NOT NULL,
    users VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);