Worked on the following Problems-
CASE AND WHEN CHAINING PROBLEMS
Problem 1: Salary Hike Based on Experience and Performance
Scenario: You want to give a salary hike based on both experience and performance rating. If the employee has:
· Experience ≥ 8 and Performance 'A', they get a 20% hike.
· Experience ≥ 5 and Performance 'B', they get a 15% hike.
· Performance 'C' gets no hike.
· For other cases, they get a 10% hike.
2) Problem 2: Bonus Calculation Based on Department and Performance
Scenario: Bonus is calculated based on the department and performance rating:
· For Finance department:
o If performance is 'A', the bonus is 20% of the salary.
o If performance is 'B', the bonus is 15% of the salary.
o If performance is 'C', the bonus is 5% of the salary.
· For Engineering department:
o If performance is 'A', the bonus is 18% of the salary.
o If performance is 'B', the bonus is 12% of the salary.
o If performance is 'C', the bonus is 3% of the salary.
· For other departments, a flat 10% bonus.
Problem 3: Categorizing Employees by Salary Range and Performance
Scenario: You want to categorize employees based on salary ranges and their performance:
· If salary is greater than 80,000 and performance is 'A', label them as High Performer.
· If salary is between 50,000 and 80,000 and performance is 'B', label them as Mid Performer.
· If salary is less than 50,000 or performance is 'C', label them as Low Performer.
Problem 4: Risk Assessment Based on Experience and Department
Scenario: You want to assess employee risk based on their experience and department:
· For employees in the HR department:
o If experience is less than 5 years, they are High Risk.
o If experience is more than 5 years, they are Low Risk.
· For employees in Engineering or Finance departments:
o If experience is more than 8 years, they are Low Risk.
o If experience is less than 8 years, they are Medium Risk.
· Employees in other departments are automatically labeled Medium Risk.
Nested case and when
Problem 1: Nested CASE for Performance and Salary Hike Based on Multiple Criteria
Scenario: You want to determine the salary hike based on performance rating, experience, and current salary. The hike rules are:
· If performance is 'A':
o For salaries above 80,000, experience above 5 years gets a 25% hike, otherwise 20%.
o For salaries between 50,000 and 80,000, the hike is 15%.
· If performance is 'B':
o For experience above 5 years, the hike is 12%.
o Otherwise, it's 10%.
· For performance 'C', there is no hike.
2.Department and Performance
Scenario: You are tasked with giving bonuses based on the department, performance rating, and experience:
· For Finance department:
o If performance is 'A' and experience is more than 10 years, bonus is 25% of salary.
o Otherwise, bonus is 20%.
· For HR department:
o If performance is 'B' or experience is greater than 5 years, the bonus is 15%.
o Otherwise, the bonus is 10%.
· For other departments, the bonus is 8%.
Problem 3: Nested CASE for Employee Categorization Based on Salary, Performance, and ExperienceScenario: Categorize employees based on their salary, performance rating, and experience:
· If salary is above 70,000:
o If performance is 'A', and experience is more than 8 years, they are labeled 'Top Performer'.
o If experience is less than 8 years, label them as 'Mid Performer'.
· If salary is between 50,000 and 70,000, they are 'Average Performer' unless their performance is 'A', in which case they are 'Rising Star'.
· If salary is below 50,000, they are 'Low Performer'.
4.Nested CASE for Tax Bracket Based on Salary and Experience
Scenario: You want to determine the tax bracket of employees based on their salary and experience:
· If salary is above 90,000:
o If experience is more than 10 years, they fall into the 35% tax bracket.
o Otherwise, they fall into the 30% tax bracket.
· If salary is between 60,000 and 90,000:
o If experience is more than 5 years, they fall into the 25% tax bracket.
o Otherwise, they fall into the 20% tax bracket.
· For salaries below 60,000, the tax rate is 15%.
Problem 5: Nested CASE for Promotion Eligibility Based on Performance, Salary, and Experience
Scenario: You want to determine if employees are eligible for promotion based on their performance rating, salary, and experience:
· If performance is 'A':
§ If salary is more than 75,000 and experience is greater than 7 years, they are 'Eligible for Senior Role'.
§ Otherwise, they are 'Eligible for Junior Role'.
· If performance is 'B':
§ If experience is more than 5 years, they are 'Eligible for Consideration'.
§ Otherwise, they are 'Not Eligible'.
· If performance is 'C', they are automatically 'Not Eligible'.

ROW_NUMBER() ONLY Questions
1.	Assign a unique row number to all employees based on salary (highest first). 
2.	Assign row numbers to employees within each department based on salary descending. 
3.	Assign row numbers based on employee joining date (latest first). 
4.	Assign row numbers within each department based on earliest joining date. 
5.	Assign row numbers to employees based on salary (lowest first). 
6.	Assign row numbers within department for employees based on name alphabetically. 
RANK() ONLY Questions
7.	Rank all employees based on salary (highest first). 
8.	Rank employees within each department based on salary. 
9.	Rank employees based on joining date (latest gets rank 1). 
10.	Rank employees within department based on salary (lowest first). 
11.	Rank employees based on name alphabetically.
DENSE_RANK() ONLY Questions
12.	Assign dense rank to employees based on salary (highest first). 
13.	Assign dense rank within each department based on salary. 
14.	Assign dense rank to employees based on joining date. 
15.	Assign dense rank to employees based on salary (lowest first). 
16.	Assign dense rank within department based on joining date. 

Key Learnings-
Using CASE / when() for conditional logic (salary hike, bonus, categorization)
Writing nested conditions to handle multiple business rules
Understanding window functions (ROW_NUMBER, RANK, DENSE_RANK)
Using partitioning and ordering in window functions
Difference between ranking functions 
Building complex transformations step by step
Translating business scenarios into SQL logic
