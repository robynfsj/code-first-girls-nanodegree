/* SQL LESSON 2—CLASSWORK
-------------------------

Topics covered in lesson 2:
1. SELECT DISTINCT—constrain the results of the query to unique values
2. WHERE—add a conditional statement where a certain condition is met
3. Database normalisation
4. Constraints and relationships
5. Core DDL commands
*/


/* 1. SELECT DISTINCT
Query the parts database. Using the table ‘parts’, return all unique part 
names. What happens if we want to return all unique parts and their id number? 
Why? 
*/

USE nano_parts;

SELECT * FROM part;
SELECT * FROM project;
SELECT * FROM supplier;
SELECT * FROM supply;

SELECT DISTINCT p.pname
FROM part p;

SELECT DISTINCT p.pname, p.p_id
FROM part p;
-- screw appears twice because the p_id is different for both screw entries


/* 2. WHERE
Refer to the table ‘projects’ and return all projects that are run in London.
*/

SELECT DISTINCT
    proj.j_id, 
    proj.jname, 
    proj.city
FROM 
    project proj
WHERE
    proj.city = "London";
    
    
/* 3. DATABASE NORMALISATION

The idea behind normalisation is to organise a database into tables in such
way that a table is created about one specific topic only.

The main reasons to normalise a database are:
• to minimise duplicate data,
• to minimize or avoid data modification issues
• to simplify queries

There are three common forms of database normalization:
• 1st, 2nd, and 3rd normal form or
• 1NF, 2NF, and 3NF respectively
*/


/* 4. CONSTRAINTS AND RELATIONSHIPS

Constraints are the rules that we can apply on the type of data in a table. In 
other words, we can specify the limit on the type of data that can be stored in 
a particular column in a table. Using constraints ensures the accuracy and 
reliability of the data in the table. If there is a mismatch or any violation 
between the constraint we set and the data, then the action that we are trying 
to perform would be aborted.

Examples of constraints:
• NOT NULL
• UNIQUE
• CHECK
• PRIMARY KEY – a single field that uniquely defines a record
• FOREIGN KEY – matches a field in one table to a field in another table
• DEFAULT

Database relationships:
• one to one
• one to many
• many to one
• many to many

TASK:
Today we are going to be pizza makers, bakers and small restaurant owners! We 
accept orders online or by telephone and deliver pizza to our customers. We 
need to create a database to hold information about our customers, so we can 
keep records of their names, addresses , phone numbers, email addresses and 
any other useful information like placed orders.

• Design and create a relational normalised database called customers.
• Set reasonable primary keys to the tables.
• Set NOT NULL constraints on the columns that you think must have values.
*/

CREATE DATABASE nano_customers;
USE nano_customers;

CREATE TABLE customer(
    customer_id INTEGER NOT NULL PRIMARY KEY,
    first_name VARCHAR(55),
    last_name VARCHAR(55)
);

CREATE TABLE email(
    email_id INTEGER NOT NULL PRIMARY KEY,
    email_customer_id INTEGER,
    email VARCHAR(55) NOT NULL
);

CREATE TABLE phone(
    phone_id INTEGER NOT NULL PRIMARY KEY,
    phone_customer_id INTEGER,
    phone_number VARCHAR(55) NOT NULL
);

CREATE TABLE address(
    address_id INTEGER NOT NULL PRIMARY KEY,
    address_customer_id INTEGER,
    building_number VARCHAR (55) NOT NULL,
    street VARCHAR (55) NOT NULL,
    city VARCHAR (55) NOT NULL,
    county VARCHAR (55),
    postcode VARCHAR (10) NOT NULL
);

CREATE TABLE orders(
    order_id INTEGER NOT NULL PRIMARY KEY,
    order_customer_id INTEGER,
    order_date DATE NOT NULL
);


/* 5. CORE DDL COMMANDS
DDL stands for data definition language. They are SQL statements used to alter 
the structure of the database.

• CREATE
• ALTER
• DROP
• RENAME
• TRUNCATE
• COMMENT

TASK:
We have our pizzeria customers database. Let’s modify some tables in the 
database, so we add Foreign Keys to tables and define relationships between 
our tables.

• Add some data to the tables in the customers database.
• Alter tables email_address and phone_number in the customers database by
adding Foreign keys that reference Primary keys from relevant tables.
• Remove the table called orders from our database.
*/

INSERT INTO customer
    (customer_id, first_name, last_name)
VALUES
    (1, "Sian", "Jones"),
    (2, "Rhys", "Williams"),
    (3, "Owen", "Evans"),
    (4, "Elen", "Evans");

ALTER TABLE email
ADD CONSTRAINT fk_email
FOREIGN KEY (email_customer_id)
REFERENCES customer (customer_id);

ALTER TABLE phone
ADD CONSTRAINT fk_phone
FOREIGN KEY (phone_customer_id)
REFERENCES customer (customer_id);

DROP TABLE orders;