CREATE TABLE customers (
    customer_id INT,
    name VARCHAR(50),
    city VARCHAR(50),
    age INT
);

CREATE TABLE sales (
    sale_id INT,
    customer_id INT,
    product VARCHAR(50),
    sale_date DATE,
    quantity INT,
    total_amount INT
);

INSERT INTO customers VALUES
(1, 'Ravi', 'Hyderabad', 25),
(2, 'Sita', 'Chennai', 32),
(3, 'Arun', 'Hyderabad', 28),
(4, 'Meena', 'Delhi', 30),
(5, 'John', 'Bangalore', 35),
(6, 'Ali', 'Mumbai', 40),
(7, 'Sara', 'Chennai', 27),
(8, 'David', 'Delhi', 45);

INSERT INTO sales VALUES
(101,1,'Laptop','2024-01-01',1,5000),
(102,1,'Mouse','2024-01-02',2,1000),
(103,1,'Keyboard','2024-01-03',1,1500),
(104,2,'Laptop','2024-01-01',1,7000),
(105,2,'Mouse','2024-01-04',1,800),
(106,3,'Laptop','2024-01-02',1,12000),
(107,4,'Monitor','2024-01-03',1,4000),
(108,5,'Mouse','2024-01-04',1,500),
(109,6,'Tablet','2024-01-05',1,6000),
(110,7,'Keyboard','2024-01-06',1,2000),
(111,7,'Mouse','2024-01-07',1,1500);
-- Daily Sales
SELECT sale_date AS date, SUM(total_amount) AS total_sales
FROM sales
GROUP BY sale_date
ORDER BY sale_date;
-- City-wise Revenue
SELECT customers.city, SUM(sales.total_amount) AS total_revenue
FROM customers 
JOIN sales ON customers.customer_id = sales.customer_id
GROUP BY customers.city;
-- Top 5 Customers
SELECT customers.name AS customer_name, SUM(sales.total_amount) AS total_spend
FROM customers
JOIN sales ON customers.customer_id = sales.customer_id
GROUP BY customers.name
ORDER BY total_spend DESC
LIMIT 5;
-- Repeated Customers (>1 order)
SELECT customer_id, COUNT(*) AS order_count
FROM sales
GROUP BY customer_id
HAVING COUNT(*) > 1;
--  Customer Segmentation → Create business logic: total_spend > 10000 → Gold 5000–10000 → Silver <5000  → Bronze
SELECT 
    customers.name AS customer_name,
    SUM(sales.total_amount) AS total_spend,
    CASE 
        WHEN SUM(sales.total_amount) > 10000 THEN 'Gold'
        WHEN SUM(sales.total_amount) BETWEEN 5000 AND 10000 THEN 'Silver'
        ELSE 'Bronze'
    END AS segment
FROM customers
JOIN sales ON customers.customer_id = sales.customer_id
GROUP BY customers.name;
--  Final Reporting Table 
SELECT 
    customers.name AS customer_name,
    customers.city,
    SUM(sales.total_amount) AS total_spend,
    COUNT(sales.sale_id) AS order_count,
    CASE 
        WHEN SUM(sales.total_amount) > 10000 THEN 'Gold'
        WHEN SUM(sales.total_amount) BETWEEN 5000 AND 10000 THEN 'Silver'
        ELSE 'Bronze'
    END AS segment
FROM customers
JOIN sales ON customers.customer_id = sales.customer_id
GROUP BY customers.name, customers.city;
