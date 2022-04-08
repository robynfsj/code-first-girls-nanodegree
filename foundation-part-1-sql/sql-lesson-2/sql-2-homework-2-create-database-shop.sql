/* SQL LESSON 2—HOMEWORK PART 2—CREATE DATABASE SHOP
----------------------------------------------------

Create a new database called SHOP. We will be using it during next lesson.
Add a new table called SALES1. It should contain the provided data.
*/

CREATE DATABASE nano_shop;
USE nano_shop;


CREATE TABLE sales1 (
	store VARCHAR(30),
    week INT,
    day VARCHAR(30),
    sales_person VARCHAR(30),
    sales_amount DEC(4,2),
    month CHAR(3)
);


INSERT INTO sales1
	(store, week, day, sales_person, sales_amount, month)
VALUES
	("London", 2, "Monday", "Frank", 56.25, "May"),
	("London", 5, "Tuesday", "Frank", 74.32, "Sep"),
    ("London", 5, "Monday", "Bill", 98.42, "Sep"),
    ("London", 5, "Saturday", "Bill", 73.90, "Dec"),
    ("London", 1, "Tuesday", "Josie", 44.27, "Sep"),
    ("Dusseldorf", 4, "Monday", "Manfred", 77.00, "Jul"),
    ("Dusseldorf", 3, "Tuesday", "Inga", 09.99, "Jun"),
    ("Dusseldorf", 4, "Wednesday", "Manfred", 86.81, "Jul"),
    ("London", 6, "Friday", "Josie", 74.02, "Oct"),
    ("Dusseldorf", 1, "Saturday", "Manfred", 43.11, "Apr");
    
    
-- Check
SELECT * FROM sales1;