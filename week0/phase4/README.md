-Problem Statement (Summary)
Clean and prepare sales and customer data
Join datasets to combine required information
Calculate key metrics (daily sales, total spend, order count)
Apply aggregations (city-wise revenue, top customers)
Implement business logic (customer segmentation)
Build and save final reporting output

-Approach Description
Loaded customer and sales data into DataFrames
Converted data types (cast total_amount to int)
Joined datasets to combine customer and sales data
Applied aggregations (daily sales, revenue, total spend, order count)
Implemented business logic (customer segmentation using conditions)
Created and saved final reporting table

-Key Transformations Used
Aggregation - groupBy() with sum(), count()
Joins - join()
Filtering - filter()
Sorting & limiting - orderBy(), limit()
Conditional logic - when()
Type conversion - withColumn() + cast()

-Key Learnings
Importance of preparing and cleaning data
Joining datasets to get complete insights
Using aggregations for analysis
Applying business logic (segmentation)
Building an end-to-end data pipeline
