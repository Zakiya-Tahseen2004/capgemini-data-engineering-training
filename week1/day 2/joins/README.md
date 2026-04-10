Problem Statement (Summary)

Retrieve employee data along with managers, departments, projects, and salary
Handle missing relationships (employees without manager/department/project)
Use joins to combine multiple tables
Identify specific conditions (no department, no project, no salary)
Perform aggregations (count employees per department)
Build queries for real-world scenarios with complete data coverage

Approach Description

Loaded all required tables (employees, departments, projects, salary)
Used self-join for employee–manager relationship
Applied different joins to combine datasets
Handled missing data using outer joins
Applied filters for specific conditions (no project, no department)
Performed aggregations and generated final outputs

Key Transformations Used

Joins - INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL JOIN, self join
Filtering - WHERE, IS NULL, IS NOT NULL
Aggregation - GROUP BY with COUNT()
Conditional handling - NULL checks

Key Learnings

Understanding different join types and when to use them
Handling missing data using outer joins
Using self-joins for hierarchical data (manager–employee)
Combining multiple tables for complete insights
Writing queries for real-world business scenarios
