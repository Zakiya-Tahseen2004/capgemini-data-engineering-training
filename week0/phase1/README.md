-Problem Statement (Summary)
Retrieve all customer records
Filter customers based on city (e.g., Chennai)
Filter customers based on age (> 25)
Select specific columns (customer_name, city)
Perform aggregation (count customers per city)


-Approach Description 
Created a Spark session
Loaded customer data into a DataFrame
Displayed all customer records
Applied filters (city = Chennai, age > 25)
Selected required columns (customer_name, city)
Performed aggregation (count of customers per city)


-Key Transformations Used
Filtering - filter() (city, age conditions)
Column selection - select()
Aggregation - groupBy() and count()


-Key Learnings
Working with PySpark DataFrames
Applying filters and selecting columns
Using aggregation (groupBy, count)
Building a simple data workflow

