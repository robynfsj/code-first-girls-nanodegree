/* SQL LESSON 3—CLASSWORK
-------------------------

Topics covered in lesson 3:
1. Operators and wildcards
2. Data sorting, filering and aggregation
*/


/* 1. Operators and wildcards

Comparison operators:
<           less than
>           greater than
<=          less than or equal to
>=          more than or equal to
=           equal to (NOTE: this is confusing as it is different to Python)
!= or <>    not equal to

Logical operators:
AND         both conditions must be true
OR          either condition or both must be true
IS          only used for NULL (IS NULL)
IS NOT      only used for NULL (IS NOT NULL)
BETWEEN     select values in given range
NOT BETWEEN select values outside of the given range
IN          specify multiple values in a WHERE clause
LIKE        used with wildcards to find strings that match a pattern

Wildcards:
%           zero, one or multiple characters
_           a single character only

For this practice exercise, please use our database ‘bakery’.
*/

USE nano_bakery;

-- Quick look at tables
SELECT * FROM savoury;
SELECT * FROM sweet;

-- Q1 Find all savoury items that have either pork or beef filling
SELECT
    sav.item_name
FROM 
    savoury AS sav
WHERE 
    main_ingredient = "pork" 
    OR main_ingredient = "beef";

-- Q2 Find all sweet items that cost 50 cents or cheaper
SELECT
    swe.item_name
FROM
    sweet AS swe
WHERE
    price <= 0.5;
    
-- Q3 Find all sweet items and their price, except for cannoli
SELECT
    swe.item_name,
    swe.price
FROM
    sweet AS swe
WHERE
    item_name != "cannoli";

-- Q4 Find all sweet items that start with the letter "c"
SELECT
    swe.item_name
FROM
    sweet AS swe
WHERE
    item_name LIKE "c%";

-- Q5 Find all savoury items that cost more than £1, but less than £3
SELECT
    sav.item_name,
    sav.price
FROM
    savoury AS sav
WHERE
    price > 1 AND price < 3;


/* 2. Aggregation and order

ORDER BY
Return data in a sorted order.
Comes after a WHERE clause.
Used with keywords ASC for ascending order (default) or DESC for descending 
order.

Set functions
The are numerous built-in functions in SQL. Some of the most used are:
COUNT
MAX
MIN
SUM
AVG

GROUP BY
Group rows that have the same values.
Often used with set functions to summarise data in a database. 
Function is applied to each subset based on the group and returns one row per 
subset.
Columns in GROUP BY must appear in SELECT list.

HAVING
Used in the place of the WHERE clause when applying aggregate functions.
Filters records based on the summarised GROUP BY results.
Note that WHERE and HAVING can be used in the same query.
The difference is that WHERE is only applied to individual records whilst HAVING 
is applied to summarised group records.

These topics are explored in today's homework.
*/