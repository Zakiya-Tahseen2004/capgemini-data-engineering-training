SELECT * FROM sales;
SELECT *
FROM sales
WHERE sale_date IS NOT NULL
  AND total_amount IS NOT NULL;
  
SELECT sale_date, SUM(total_amount) AS daily_sales
FROM sales
GROUP BY sale_date
ORDER BY sale_date;

SELECT *
FROM customers
JOIN sales
ON customers.customer_id = sales.customer_id
WHERE customers.city IS NOT NULL
  AND sales.total_amount IS NOT NULL;

SELECT customers.city, SUM(sales.total_amount) AS revenue
FROM customers
JOIN sales
ON customers.customer_id = sales.customer_id
GROUP BY customers.city
ORDER BY revenue DESC;

SELECT customer_id, COUNT(*) AS order_count
FROM sales
GROUP BY customer_id
HAVING COUNT(*) > 1;

SELECT customers.city, sales.customer_id, SUM(sales.total_amount) AS total_spend
FROM customers
JOIN sales
ON customers.customer_id = sales.customer_id
GROUP BY customers.city, sales.customer_id
ORDER BY customers.city, total_spend DESC;


SELECT 
    customers.customer_id,
    customers.city,
    SUM(sales.total_amount) AS total_spend,
    COUNT(sales.sale_id) AS order_count
FROM customers
JOIN sales
ON customers.customer_id = sales.customer_id
GROUP BY customers.customer_id,customers.city;
