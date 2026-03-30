-Problem Statement (Summary)
Join customer and orders data
Calculate total spend and average order amount
Identify top customers based on spend
Find customers with no or multiple orders
Perform aggregations (customer-wise, city-wise)
Sort results for reporting


-Approach Description
Loaded customers and sales data into DataFrames
Joined customers and sales data
Applied aggregations (sum, avg, count)
Filtered and sorted data (top customers, multiple orders)
Generated final outputs for analysis


-Key Transformations Used
Aggregation - groupBy() with sum(), avg(), count()
Sorting & limiting - orderBy(), limit()
Joins - join() (inner, left)
Filtering - filter()


-Key Learnings
Importance of handling missing data
Joining datasets for better insights
Using aggregations for analysis
Filtering and sorting results for reporting
