CREATE TABLE customers (
    customer_id INT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    phone_number VARCHAR(20),
    address VARCHAR(100),
    city VARCHAR(50),
    state VARCHAR(50),
    zip_code VARCHAR(10)
);
CREATE TABLE sales (
    sale_id INT,
    customer_id INT,
    product_id VARCHAR(20),
    sale_date DATE,
    quantity INT,
    total_amount INT
);
INSERT INTO customers VALUES
(1,'Ravi','Kumar','ravi@gmail.com','111','Addr1','Hyderabad','TS','500001'),
(2,'Sita','Devi','sita@gmail.com','222','Addr2','Chennai','TN','600001'),
(3,'Arun','Raj','arun@gmail.com','333','Addr3','Hyderabad','TS','500002'),
(4,'John','Paul','john@gmail.com','444','Addr4','Delhi','DL','110001');
INSERT INTO sales VALUES
(101,1,'P1','2024-01-01',2,500),
(102,1,'P2','2024-01-02',1,300),
(103,2,'P3','2024-01-03',5,1000),
(104,3,'P1','2024-01-04',1,200);

SELECT customer_id, SUM(total_amount) AS total_spend
FROM sales
GROUP BY customer_id;

SELECT customer_id, SUM(total_amount) AS total_spend
FROM sales
GROUP BY customer_id
ORDER BY total_spend DESC
LIMIT 3;

SELECT *
FROM customers
LEFT JOIN sales
ON customers.customer_id = sales.customer_id
WHERE sales.customer_id IS NULL;

SELECT customers.city, SUM(sales.total_amount) AS revenue
FROM customers
JOIN sales
ON customers.customer_id = sales.customer_id
GROUP BY customers.city;

SELECT customer_id, AVG(total_amount) AS avg_amount
FROM sales
GROUP BY customer_id;

SELECT customer_id, COUNT(*) AS orders
FROM sales
GROUP BY customer_id
HAVING COUNT(*) > 1;

SELECT customer_id, SUM(total_amount) AS total_spend
FROM sales
GROUP BY customer_id
ORDER BY total_spend DESC;
