Problem Statement (Summary)-
Perform data transformations on employee dataset
Apply column operations using withColumn()
Sort and organize data using orderBy() / sort()
Handle missing and duplicate data
Perform aggregations using groupBy()
Combine datasets using union() and unionByName()
Work with string and date functions
Apply different types of joins for data analysis


Approach Description-
Created DataFrame with defined schema
Applied transformations using withColumn()
Sorted data using orderBy()
Cleaned data using drop() and dropDuplicates()
Handled null values using dropna()
Aggregated data using groupBy()
Used collect_list() for grouped insights
Combined DataFrames using union() and unionByName()
Applied joins (inner, left, right, anti)


Key Transformations Used-
Column operations - withColumn()
Sorting - orderBy(), sort()
Null handling - dropna()
Duplicate handling - dropDuplicates()
Aggregations - groupBy(), agg()
List aggregation - collect_list()
Combining data - union(), unionByName()
Joins - inner, left, right, anti
String functions - upper(), lower(), initcap()
Date functions - current_date(), date_add(), date_sub(), month()


Key Learnings-
Understanding core PySpark DataFrame transformations
Cleaning and preparing real-world data
Performing aggregations and grouping logic
Handling nulls and duplicates effectively
Using joins to combine datasets correctly
Applying string and date transformations


Writing structured and readable PySpark code
