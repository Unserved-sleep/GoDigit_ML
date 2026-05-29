CREATE TABLE top_rated_films(
                                title VARCHAR NOT NULL,
                                release_year SMALLINT
);

CREATE TABLE most_popular_films(
                                   title VARCHAR NOT NULL,
                                   release_year SMALLINT
);

INSERT INTO top_rated_films(title, release_year)
VALUES
    ('The Shawshank Redemption', 1994),
    ('The Godfather', 1972),
    ('The Dark Knight', 2008),
    ('12 Angry Men', 1957);

INSERT INTO most_popular_films(title, release_year)
VALUES
    ('An American Pickle', 2020),
    ('The Godfather', 1972),
    ('The Dark Knight', 2008),
    ('Greyhound', 2020);

select * from top_rated_films

select * from most_popular_films

SELECT * FROM top_rated_films
UNION
SELECT * FROM most_popular_films;

SELECT * FROM top_rated_films
UNION ALL
SELECT * FROM most_popular_films
order by release_year desc;

SELECT *
FROM most_popular_films
INTERSECT
SELECT *
FROM top_rated_films;

SELECT * FROM top_rated_films
EXCEPT
SELECT * FROM most_popular_films;

drop table top_rated_films, most_popular_films

CREATE TABLE employees (
                           employee_id SERIAL PRIMARY KEY,
                           full_name VARCHAR NOT NULL,
                           manager_id INT
);

INSERT INTO employees (employee_id, full_name, manager_id)
VALUES
    (1, 'Michael North', NULL),
    (2, 'Megan Berry', 1),
    (3, 'Sarah Berry', 1),
    (4, 'Zoe Black', 1),
    (5, 'Tim James', 1),
    (6, 'Bella Tucker', 2),
    (7, 'Ryan Metcalfe', 2),
    (8, 'Max Mills', 2),
    (9, 'Benjamin Glover', 2),
    (10, 'Carolyn Henderson', 3),
    (11, 'Nicola Kelly', 3),
    (12, 'Alexandra Climo', 3),
    (13, 'Dominic King', 3),
    (14, 'Leonard Gray', 4),
    (15, 'Eric Rampling', 4),
    (16, 'Piers Paige', 7),
    (17, 'Ryan Henderson', 7),
    (18, 'Frank Tucker', 8),
    (19, 'Nathan Ferguson', 8),
    (20, 'Kevin Rampling', 8);


WITH RECURSIVE subordinates AS (
    SELECT
        employee_id,
        manager_id,
        full_name
    FROM
        employees
    WHERE
        employee_id = 2
    UNION
    SELECT
        e.employee_id,
        e.manager_id,
        e.full_name
    FROM
        employees e
            INNER JOIN subordinates s ON s.employee_id = e.manager_id
)
SELECT * FROM subordinates;

drop table employees


CREATE TABLE links (
                       id SERIAL PRIMARY KEY,
                       url VARCHAR(255) NOT NULL,
                       name VARCHAR(255) NOT NULL,
                       description VARCHAR (255),
                       last_update DATE
);
INSERT INTO links (url, name)
VALUES('https://neon.com/postgresql','PostgreSQL Tutorial');

SELECT * FROM links;
INSERT INTO links (url, name)
VALUES('http://www.oreilly.com','O''Reilly Media');

INSERT INTO links (url, name, last_update)
VALUES('https://www.google.com','Google','2013-06-01');

INSERT INTO links (url, name)
VALUES('https://www.postgresql.org','PostgreSQL')
RETURNING id;

drop table links

CREATE TABLE contacts (
                          id SERIAL PRIMARY KEY,
                          first_name VARCHAR(50) NOT NULL,
                          last_name VARCHAR(50) NOT NULL,
                          email VARCHAR(384) NOT NULL UNIQUE
);
INSERT INTO contacts (first_name, last_name, email)
VALUES
    ('John', 'Doe', 'john.doe@example.com'),
    ('Jane', 'Smith', 'jane.smith@example.com'),
    ('Bob', 'Johnson', 'bob.johnson@example.com');

SELECT * FROM contacts;

INSERT INTO contacts (first_name, last_name, email)
VALUES
    ('Alice', 'Johnson', 'alice.johnson@example.com'),
    ('Charlie', 'Brown', 'charlie.brown@example.com')
RETURNING *;

drop table contacts

CREATE TABLE courses(
                        course_id serial PRIMARY KEY,
                        course_name VARCHAR(255) NOT NULL,
                        price DECIMAL(10,2) NOT NULL,
                        description VARCHAR(500),
                        published_date date
);


INSERT INTO courses( course_name, price, description, published_date)
VALUES
    ('PostgreSQL for Developers', 299.99, 'A complete PostgreSQL for Developers', '2020-07-13'),
    ('PostgreSQL Administration', 349.99, 'A PostgreSQL Guide for DBA', NULL),
    ('PostgreSQL High Performance', 549.99, NULL, NULL),
    ('PostgreSQL Bootcamp', 777.99, 'Learn PostgreSQL via Bootcamp', '2013-07-11'),
    ('Mastering PostgreSQL', 999.98, 'Mastering PostgreSQL in 21 Days', '2012-06-30');

SELECT * FROM courses;

UPDATE courses
SET published_date = '2020-08-01'
WHERE course_id = 3
returning *;

drop table courses

CREATE TABLE product_segment (
                                 id SERIAL PRIMARY KEY,
                                 segment VARCHAR NOT NULL,
                                 discount NUMERIC (4, 2)
);


INSERT INTO
    product_segment (segment, discount)
VALUES
    ('Grand Luxury', 0.05),
    ('Luxury', 0.06),
    ('Mass', 0.1);

CREATE TABLE product(
                        id SERIAL PRIMARY KEY,
                        name VARCHAR NOT NULL,
                        price NUMERIC(10,2),
                        net_price NUMERIC(10,2),
                        segment_id INT NOT NULL,
                        FOREIGN KEY(segment_id) REFERENCES product_segment(id)
);


INSERT INTO
    product (name, price, segment_id)
VALUES
    ('diam', 804.89, 1),
    ('vestibulum aliquet', 228.55, 3),
    ('lacinia erat', 366.45, 2),
    ('scelerisque quam turpis', 145.33, 3),
    ('justo lacinia', 551.77, 2),
    ('ultrices mattis odio', 261.58, 3),
    ('hendrerit', 519.62, 2),
    ('in hac habitasse', 843.31, 1),
    ('orci eget orci', 254.18, 3),
    ('pellentesque', 427.78, 2),
    ('sit amet nunc', 936.29, 1),
    ('sed vestibulum', 910.34, 1),
    ('turpis eget', 208.33, 3),
    ('cursus vestibulum', 985.45, 1),
    ('orci nullam', 841.26, 1),
    ('est quam pharetra', 896.38, 1),
    ('posuere', 575.74, 2),
    ('ligula', 530.64, 2),
    ('convallis', 892.43, 1),
    ('nulla elit ac', 161.71, 3);

UPDATE
    product p
SET
    net_price = price - price * discount
FROM
    product_segment s
WHERE
    p.segment_id = s.id
returning *;

drop table product, product_segment

DELETE FROM member
    USING denylist
WHERE member.phone = denylist.phone;

DELETE FROM member
WHERE phone IN (
    SELECT
        phone
    FROM
        denylist
);

-- FOREIGN KEY(department_id)
--REFERENCES departments(id)
--ON DELETE CASCADE

-- DELETE  FROM      deleting duplicates
--     basket a
--         USING basket b
-- WHERE
--     a.id > b.id
--     AND a.fruit = b.fruit;


-- DELETE FROM basket   deleting duplicates using subquery
-- WHERE id IN
--     (SELECT id
--     FROM
--         (SELECT id,
--          ROW_NUMBER() OVER( PARTITION BY fruit
--         ORDER BY  id ) AS row_num
--         FROM basket ) t
--         WHERE t.row_num > 1 );


-- -- step 1       making a copy of the table
-- CREATE TABLE basket_temp (LIKE basket);
--
-- -- step 2
-- INSERT INTO basket_temp(fruit, id)
-- SELECT
--     DISTINCT ON (fruit) fruit,
--     id
-- FROM basket;
--
-- -- step 3
-- DROP TABLE basket;
--
-- -- step 4
-- ALTER TABLE basket_temp
-- RENAME TO basket;


CREATE TABLE Inventory1(
                           id INT PRIMARY KEY,
                           name VARCHAR(255) NOT NULL,
                           price DECIMAL(10,2) NOT NULL,
                           quantity INT NOT NULL
);

INSERT INTO inventory1(id, name, price, quantity)
VALUES
    (1, 'A', 15.99, 100),
    (2, 'B', 25.49, 50),
    (3, 'C', 19.95, 75)
RETURNING *;

INSERT INTO inventory1 (id, name, price, quantity)
VALUES (1, 'A', 16.99, 120)
ON CONFLICT(id)
    DO UPDATE SET
                  price = EXCLUDED.price,
                  quantity = EXCLUDED.quantity;

SELECT * FROM inventory1
WHERE id = 1;

drop table inventory1


-- merge
-- MERGE INTO target_table
-- USING source_table
-- ON match_condition
-- WHEN MATCHED AND condition THEN
--     UPDATE SET column1 = value1, column2 = value2
-- WHEN MATCHED AND NOT condition THEN
--     DELETE
-- WHEN NOT MATCHED THEN
--     INSERT (column1, column2) VALUES (value1, value2)
-- RETURNING merge_action(), target_table.*;


-- Create the main products table
CREATE TABLE products (
                          product_id SERIAL PRIMARY KEY,
                          name TEXT UNIQUE,
                          price DECIMAL(10,2),
                          stock INTEGER,
                          status TEXT,
                          last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert some initial data
INSERT INTO products (name, price, stock, status) VALUES
                                                      ('Laptop', 999.99, 50, 'active'),
                                                      ('Keyboard', 79.99, 100, 'active'),
                                                      ('Mouse', 29.99, 200, 'active');

-- Create a table for our updates
CREATE TABLE product_updates (
                                 name TEXT,
                                 price DECIMAL(10,2),
                                 stock INTEGER,
                                 status TEXT
);

-- Insert mixed update data (new products, updates, and discontinuations)
INSERT INTO product_updates VALUES
                                ('Laptop', 1099.99, 75, 'active'),      -- Update: price and stock change
                                ('Monitor', 299.99, 30, 'active'),      -- Insert: new product
                                ('Keyboard', NULL, 0, 'discontinued'),  -- Delete: mark as discontinued
                                ('Headphones', 89.99, 50, 'active');    -- Insert: another new product

-- Perform the MERGE operation
MERGE INTO products p
USING product_updates u
ON p.name = u.name
WHEN MATCHED AND u.status = 'discontinued' THEN
    DELETE
WHEN MATCHED AND u.status = 'active' THEN
    UPDATE SET
               price = COALESCE(u.price, p.price),
               stock = u.stock,
               status = u.status,
               last_updated = CURRENT_TIMESTAMP
WHEN NOT MATCHED AND u.status = 'active' THEN
    INSERT (name, price, stock, status)
    VALUES (u.name, u.price, u.stock, u.status)
    RETURNING
        merge_action() as action,
        p.product_id,
        p.name,
        p.price,
        p.stock,
        p.status,
        p.last_updated;

drop table products, product_updates

-- Transactions
-- BEGIN TRANSACTION;
-- BEGIN WORK;
-- BEGIN;

-- COMMIT WORK;
-- COMMIT TRANSACTION;
-- COMMIT;

-- ROLLBACK;
-- ROLLBACK TRANSACTION;
-- ROLLBACK WORK;

-- SAVEPOINT savepoint_name;
-- ROLLBACK TO SAVEPOINT savepoint_name;

-- importing csv file
-- COPY sample_table_name
-- FROM 'C:\sampledb\sample_data.csv'
-- DELIMITER ','    needed for csv
-- CSV HEADER;

-- exporting csv file
-- COPY persons TO 'C:\temp\persons_db.csv' DELIMITER ',' CSV HEADER;

-- COPY persons(first_name,last_name,email)
-- TO 'C:\temp\persons_partial_db.csv' DELIMITER ',' CSV HEADER;

-- \copy (SELECT * FROM persons) to 'C:\temp\persons_client.csv' with csv    ---from psl client



CREATE TABLE accounts (  --if not exists
                          user_id SERIAL PRIMARY KEY,
                          username VARCHAR (50) UNIQUE NOT NULL,
                          password VARCHAR (50) NOT NULL,
                          email VARCHAR (255) UNIQUE NOT NULL,
                          created_at TIMESTAMP NOT NULL,
                          last_login TIMESTAMP
);

-- sequence
CREATE TABLE order_details(
                              order_id SERIAL,
                              item_id INT NOT NULL,
                              item_text VARCHAR NOT NULL,
                              price DEC(10,2) NOT NULL,
                              PRIMARY KEY(order_id, item_id)
);

CREATE SEQUENCE order_item_id
    START 10
    INCREMENT 10
    MINVALUE 10
    OWNED BY order_details.item_id;

INSERT INTO
    order_details(order_id, item_id, item_text, price)
VALUES
    (100, nextval('order_item_id'),'DVD Player',100),
    (100, nextval('order_item_id'),'Android TV',550),
    (100, nextval('order_item_id'),'Speaker',250);

select * from order_details;


CREATE TABLE contacts(
                         id SERIAL PRIMARY KEY,
                         first_name VARCHAR(50) NOT NULL,
                         last_name VARCHAR(50) NOT NULL,
                         full_name VARCHAR(101) GENERATED ALWAYS AS (first_name || ' ' || last_name) STORED,
                         email VARCHAR(300) UNIQUE
);

-- Alter table add, drop, rename column name
-- ALTER TABLE alter column target set default, add check, add constraints

-- ALTER TABLE assets
-- ALTER COLUMN asset_no TYPE INT;

-- type casting
-- ALTER TABLE assets
-- ALTER COLUMN asset_no TYPE INT
-- USING asset_no::integer;

-- NOTICE:  truncate cascades to table "order_items"
-- TRUNCATE TABLE

-- CREATE TABLE new_table AS
-- TABLE existing_table
-- WITH NO DATA;


DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS contacts;

CREATE TABLE customers(
                          customer_id INT GENERATED ALWAYS AS IDENTITY,
                          customer_name VARCHAR(255) NOT NULL,
                          PRIMARY KEY(customer_id)
);

CREATE TABLE contacts(
                         contact_id INT GENERATED ALWAYS AS IDENTITY,
                         customer_id INT,
                         contact_name VARCHAR(255) NOT NULL,
                         phone VARCHAR(15),
                         email VARCHAR(100),
                         PRIMARY KEY(contact_id),
                         CONSTRAINT fk_customer
                             FOREIGN KEY(customer_id)
                                 REFERENCES customers(customer_id)
);

-- CONSTRAINT fk_customer
--       FOREIGN KEY(customer_id)
-- 	  REFERENCES customers(customer_id)
-- 	  ON DELETE SET NULL /  ON DELETE CASCADE / ON DELETE RESTRICT / ON DELETE NO ACTION


SELECT
    title,
    length,
    CASE WHEN length > 0
        AND length <= 50 THEN 'Short' WHEN length > 50
        AND length <= 120 THEN 'Medium' WHEN length > 120 THEN 'Long' END duration
FROM
    film
ORDER BY
    title;


SELECT
    id,
    title,
    COALESCE (
            NULLIF (excerpt, ''),
            LEFT (body, 40)
    )
FROM
    posts;


