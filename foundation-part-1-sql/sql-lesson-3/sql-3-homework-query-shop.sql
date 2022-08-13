/* SQL LESSON 3—HOMEWORK
-------------------------

We are going to use a mock database that holds a table, which contains sales data
for a shop chain (you created it at home)
• Importantly, we are going to assume the role of a Business Analyst or an Auditor (who
do you prefer to be ☺) to work with this sales database
• Our task will be to write a number of queries to analyse sales data and ‘report it back
to our big bosses’
• All queries that we will not finish in class will need to be completed as part of
homework for week 3
*/


USE nano_shop;
SELECT * FROM sales1;


-- Find all sales records (and all columns) that took place in the London store, 
-- not in December, but sales concluded by Bill or Frank for the amount higher 
-- than £50.
SELECT
    s1.store,
    s1.week,
    s1.day,
    s1.sales_person,
    s1.sales_amount,
    s1.month
FROM sales1 AS s1
WHERE
    s1.store = "London" AND 
    s1.month != "Dec" AND 
    (s1.sales_person = "Bill" OR s1.sales_person = "Frank") AND 
    s1.sales_amount > 50;


-- Find out how many sales took place each week (in no particular order)
SELECT
    s1.week,
    COUNT(s1.sales_amount) AS number_of_sales
FROM sales1 AS s1
GROUP BY s1.week;


-- Find out how many sales took place each week (and present data by week in
-- descending and then in ascending order)
SELECT
    s1.week,
    COUNT(s1.sales_amount) AS number_of_sales
FROM sales1 AS s1
GROUP BY s1.week
ORDER BY s1.week DESC;
    
SELECT
    s1.week,
    COUNT(s1.sales_amount) AS number_of_sales
FROM sales1 AS s1
GROUP BY s1.week
ORDER BY s1.week ASC;
    

-- Find out how many sales were recorded each week on different days of the week
SELECT
    s1.week,
    s1.day,
    COUNT(s1.day) AS number_of_sales
FROM sales1 AS s1
GROUP BY
    s1.week,
    s1.day
ORDER BY s1.week;


-- We need to change salesperson's name Inga to Annette
-- NOTE: need to disable safe mode to do this
UPDATE sales1 AS s1
SET s1.sales_person = "Annette"
WHERE s1.sales_person = "Inga";


-- Find out how many sales did Annette do
SELECT
    s1.sales_person,
    COUNT(s1.sales_amount) AS sales_made
FROM sales1 AS s1
WHERE s1.sales_person = "Annette";


-- Find the total sales amount by each person by day
SELECT
    s1.sales_person,
    s1.day,
    SUM(sales_amount)
FROM sales1 AS s1
GROUP BY
    s1.sales_person,
    s1.day;


-- How much (sum) each person sold for the given period
SELECT
    s1.sales_person,
    SUM(sales_amount) AS total_sales_amount
FROM sales1 AS s1
GROUP BY s1.sales_person
ORDER BY total_sales_amount DESC;


-- How much (sum) each person sold for the given period, including the number of 
-- sales per person, their average, lowest and highest sale amounts
SELECT
    s1.sales_person,
    SUM(s1.sales_amount) AS total_sales_amount,
    COUNT(s1.sales_amount) AS number_of_sales,
    AVG(s1.sales_amount) AS average_sale_amount,
    MIN(s1.sales_amount) AS lowest_sale_amount,
    MAX(s1.sales_amount) AS highest_sale_amount
FROM sales1 AS s1
GROUP BY s1.sales_person;


-- Find the total monetary sales amount achieved by each store
SELECT
    s1.store,
    SUM(sales_amount) AS store_sales_amount
FROM sales1 AS s1
GROUP BY s1.store;


-- Find the number of sales by each person if they did less than 3 sales for the 
-- past period
SELECT
    s1.sales_person,
    COUNT(s1.sales_amount) AS number_of_sales
FROM sales1 AS s1
GROUP BY s1.sales_person
HAVING number_of_sales < 3;


-- Find the total amount of sales by month where combined total is less than £100
-- NOTE: wasn't sure if "total amount of sales" means the total number of sales or 
--       the total sales amount so have included both
SELECT
    s1.month,
    COUNT(s1.sales_amount) AS number_of_sales,
    SUM(s1.sales_amount) AS total_sales_amount
FROM sales1 AS s1
GROUP BY s1.month
HAVING total_sales_amount < 100;