CREATE TABLE IF NOT EXISTS test (id int, name varchar(10), days int);

INSERT INTO test VALUES (1,'January',31);
INSERT INTO test (id,name,days) VALUES (2,'February',29);
INSERT INTO test (id,days) VALUES (2,29);

SELECT * FROM test;
SELECT name FROM test;

SELECT * FROM test ORDER BY name;
SELECT * FROM test ORDER BY name DESC;

SELECT *
FROM test
WHERE days = 29;

SELECT *
FROM test
WHERE id != 1 AND days = 29
ORDER BY name;

SELECT * FROM test WHERE name IN ('aa','aaaaa');

SELECT * FROM test WHERE days BETWEEN 27 and 30;

SELECT * FROM test WHERE name LIKE '%b%';
SELECT * FROM test WHERE name LIKE 'a%';
SELECT * FROM test WHERE name LIKE '%b';

SELECT COUNT()FROM test;
SELECT SUM(id)FROM test;
SELECT AVG(id)FROM test;

SELECT MIN(name)FROM test;
SELECT MAX(name)FROM test;

SELECT MIN(days)FROM test;
SELECT MAX(days)FROM test;

SELECT name, avg(days)FROM test;

SELECT *
FROM test
WHERE id > (
    SELECT AVG(id) FROM test
    )
