/* SQL LESSON 1—CREATING AND POPULATING A DATABASE
--------------------------------------------------

It is time to create our very first database and populate it with few tables.

1. Create a database called Bakery.

2. Let’s add two tables to the database. One should be called ‘Sweet’ and the one 
should be called ‘Savoury’. 

3. The Sweet table should have three columns: id (which 
is a number), item_name (name of a pastry) and price (prices can be expressed in 
pound and pennies).

4. Include the same columns in the Savoury table. In addition to that add a column
called main_ingredient (it will be a descriptive word) 

5. Populate the database with the data provided.
*/


-- create database
CREATE DATABASE nano_bakery;
USE nano_bakery;


-- create tables
CREATE TABLE sweet(
    id INT NOT NULL,
    item_name VARCHAR(50),
    price FLOAT(2)
);

CREATE TABLE savoury(
    id INT NOT NULL,
    item_name VARCHAR(50),
    price FLOAT(2),
    main_ingredient VARCHAR(100)
);


-- populate tables
INSERT INTO sweet
    (id, item_name, price)
VALUES
    (1, 'doughnut', 0.5),
    (2, 'croissant', 0.75),
    (3, 'painauchocolat', 0.55),
    (4, 'cinnamon twirl', 0.45),
    (5, 'cannoli', 0.88),
    (6, 'apple tart', 1.12);

INSERT INTO savoury
    (id, item_name, price, main_ingredient)
VALUES
    (1, 'meat pie', 1.25, 'pork'),
    (2, 'sausage roll', 1, null),
    (3, 'pasty', 2.45, 'beef');


-- check tables
SELECT * FROM sweet;
SELECT * FROM savoury;