/* SQL LESSON 2—HOMEWORK PART 1—QUERY PARTS DB
----------------------------------------------

Use parts DB to write the following queries:
1. Find the name and weight of each red part.
2. Find all unique supplier(s) name from London.
*/

USE nano_parts;

-- Quick look at relevant tables
SELECT * FROM part;
SELECT * FROM supplier;

-- 1. Find the name and weight of each red part.
SELECT 
    p.pname,
    p.weight
FROM part p
WHERE colour = "red";
    
-- 2. Find all unique supplier(s) name from London.
SELECT DISTINCT
    s.sname
FROM supplier s
WHERE s.city = "London";