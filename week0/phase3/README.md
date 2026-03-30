-Problem Statement (Summary)
Clean sales and customer data (nulls, invalid values, duplicates)
Validate cleaned data (row counts/checks)
Join datasets to combine customer and sales info
Calculate key metrics (daily sales, total spend, order count)
Apply aggregations (city-wise revenue, repeat customers)
Build final reporting table for analysis


-Approach Description
Loaded customer and sales data into DataFrames
Cleaned data (handled nulls, removed duplicates, filtered invalid values)
Converted data types (cast total_amount to int)
Joined datasets to combine customer and sales data
Applied aggregations (daily sales, city-wise revenue, order counts)
Generated final outputs for reporting and analysis


-Key Transformations Used
Aggregation - groupBy() with sum(), count()
Joins - join() (inner join)
Filtering - filter()
Data cleaning - dropna(), fillna(), dropDuplicates()
Type conversion - withColumn() + cast()


-Key Learnings
Importance of data cleaning (nulls, duplicates, invalid values)
Preparing data before joining datasets
Using aggregations to generate insights
Building a complete data processing workflow

