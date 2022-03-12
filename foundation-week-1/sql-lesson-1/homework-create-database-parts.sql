/*SQL LESSON 1—HOMEWORK
-----------------------

Create new Database called PARTS. The Database should contain four 
tables, which must store the data provided.
*/


CREATE DATABASE nano_parts;
USE nano_parts;


-- 1. Create tables

CREATE TABLE part(
    p_id CHAR(2) NOT NULL,
    pname VARCHAR(20),
    colour VARCHAR(20),
    weight INT,
    city VARCHAR(20)
);

CREATE TABLE project(
    j_id CHAR(2) NOT NULL,
    jname VARCHAR(20),
    city VARCHAR(20)
);
    
CREATE TABLE supplier(
    s_id CHAR(2) NOT NULL,
    sname VARCHAR(20),
    stat INT,
    city VARCHAR(20)
);

CREATE TABLE supply(
    s_id CHAR(2),
    p_id CHAR(2),
    j_id CHAR(2),
    quantity INT
);


-- 2. Populate tables

INSERT INTO part
(p_id, pname, colour, weight, city)
VALUES
('P1', 'nut', 'red', 12, 'London'),
('P2', 'bolt', 'green', 17, 'Paris'),
('P3', 'screw', 'blue', 17, 'Rome'),
('P4', 'screw', 'red', 14, 'London'),
('P5', 'cam', 'blue', 12, 'Paris'),
('P6', 'cog', 'red', 19, 'London');

INSERT INTO project
(j_id, jname, city)
VALUES
('J1', 'sorter', 'Paris'),
('J2', 'display', 'Rome'),
('J3', 'ocr', 'Athens'),
('J4', 'console', 'Athens'),
('J5', 'raid', 'London'),
('J6', 'eds', 'Oslo'),
('J7', 'tape', 'London');

INSERT INTO supplier
(s_id, sname, stat, city)
VALUES
('S1', 'Smith', 20, 'London'),
('S2', 'Jones', 10, 'Paris'),
('S3', 'Blake', 30, 'Paris'),
('S4', 'Clark', 20, 'London'),
('S5', 'Adams', 30, 'Athens');

INSERT INTO supply
(s_id, p_id, j_id, quantity)
VALUES
('S1', 'P1', 'J1', 200),
('S1', 'P1', 'J4', 700),
('S2', 'P3', 'J1', 400),
('S2', 'P3', 'J2', 200),
('S2', 'P3', 'J3', 200),
('S2', 'P3', 'J4', 500),
('S2', 'P3', 'J5', 600),
('S2', 'P3', 'J6', 400),
('S2', 'P3', 'J7', 800),
('S2', 'P5', 'J2', 100),
('S3', 'P3', 'J1', 200),
('S3', 'P4', 'J2', 500),
('S4', 'P6', 'J3', 300),
('S4', 'P6', 'J7', 300),
('S5', 'P2', 'J2', 200),
('S5', 'P2', 'J4', 100),
('S5', 'P5', 'J5', 500),
('S5', 'P5', 'J7', 100),
('S5', 'P6', 'J2', 200),
('S5', 'P1', 'J4', 100),
('S5', 'P3', 'J4', 200),
('S5', 'P4', 'J4', 800),
('S5', 'P5', 'J4', 400),
('S5', 'P6', 'J4', 500);


-- 3. Check tables

SELECT * FROM part;
SELECT * FROM project;
SELECT * FROM supplier;
SELECT * FROM supply;