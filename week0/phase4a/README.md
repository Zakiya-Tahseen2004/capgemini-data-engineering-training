-Problem Statement (Summary)
Calculate total spend for customers
Apply segmentation (Gold, Silver, Bronze using conditions)
Perform advanced segmentation (quantiles, ranking)
Group and compare segment results
Analyze and identify the best segmentation approach

-Approach Description
Loaded customer and sales data into DataFrames
Converted data types (cast total_amount to int)
Joined datasets to calculate total spend per customer
Applied aggregation (sum of total spend)
Implemented segmentation (rule-based, quantile-based, ranking)
Compared segmentation results for analysis

-Key Transformations Used
Aggregation - groupBy() with sum(), count()
Joins - join()
Window functions - percent_rank()
Conditional logic - when()
Quantile calculation - approxQuantile()

-Key Learnings
Applying different segmentation techniques
Using window functions for ranking
Comparing methods to choose the best approach
