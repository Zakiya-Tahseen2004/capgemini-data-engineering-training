-Problem Statement (Summary)
Clean sales and customer data (handle nulls, invalid rows)
Join datasets to combine customer and sales details
Calculate key metrics (daily sales, total spend, order count)
Identify repeat and top customers
Apply aggregations (city-wise revenue, customer-wise spend)
Build final reporting table for analysis


-Approach Description
Loaded customer and sales data into DataFrames
Cleaned sales data (handled nulls, converted data types)
Joined customer and sales datasets
Filtered valid records for analysis
Applied aggregations (daily sales, city revenue, order count)
Generated outputs for reporting and insights


-Key Transformations Used
Aggregation - groupBy() with sum(), count()
Joins - join() (inner join)
Filtering - filter()
Data cleaning - dropna()
Type conversion - withColumn() + cast()


-Key Learnings
Importance of cleaning data before processing
Preparing datasets before joining
Using aggregations to derive insights
Building a simple end-to-end pipeline

