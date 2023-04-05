CREATE TABLE users(id SERIAL UNIQUE PRIMARY KEY, name VARCHAR, age INT);
CREATE TABLE articles(
    id SERIAL,
    author_id BIGINT,
    title VARCHAR,
    FOREIGN KEY(author_id) REFERENCES users(id));
INSERT INTO users(id, name, age) VALUES (1, 'John', 30), (2, 'Mary', 24), (3, 'Joe', 56);
INSERT INTO articles(author_id, title) VALUES
    (1, 'How to become famous'),
    (1, 'How to stop being famous'),
    (2, 'How to write interesting articles');
