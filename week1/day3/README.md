Problem Statement (Summary)

Apply conditional logic for salary hike, bonus, categorization, and risk
Implement nested conditions for complex business rules
Use window functions to rank employees based on salary, date, and department
Perform partitioning for department-wise analysis
Handle real-world scenarios (promotion, tax, segmentation)
Generate insights using ranking and classification

Approach Description

Loaded employee dataset
Applied conditional logic using CASE / when()
Implemented nested conditions for complex rules
Defined window specifications (partition, order)
Applied window functions (ROW_NUMBER, RANK, DENSE_RANK)
Generated final outputs for analysis

Key Transformations Used 

Conditional logic - CASE, when() / otherwise()
Nested conditions - multiple when() or nested CASE
Window functions - ROW_NUMBER(), RANK(), DENSE_RANK()
Partitioning - partitionBy()
Sorting - orderBy()

Key Learnings

Writing conditional and nested logic for business rules
Understanding differences between ranking functions
Using window functions with partitioning and ordering
Translating real-world scenarios into SQL/PySpark logic
Building structured and step-by-step data transformations
