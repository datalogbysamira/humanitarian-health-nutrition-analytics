==============================
DAY 1 PROFESSIONAL QUESTIONS
==============================

Q1. What is the difference between pip install and pip freeze?

Answer:
- pip install installs one or more Python packages into the current environment.
- pip freeze lists all installed packages with their exact versions, usually to create requirements.txt.

------------------------------------------------------

Q2. Why do we use a virtual environment (.venv)?

Answer:
A virtual environment isolates project dependencies from the global Python installation. This prevents version conflicts between projects, keeps the system clean, and allows the project to be reproduced on another machine.

------------------------------------------------------

Q3. Why is requirements.txt important?

Answer:
requirements.txt records the exact versions of the libraries used in the project. Another developer can recreate the same environment using:

pip install -r requirements.txt

------------------------------------------------------

Q4. What is the difference between Git and GitHub?

Answer:
Git is a distributed version control system used to track changes locally.
GitHub is a cloud platform used to host Git repositories, collaborate with others, manage issues, pull requests, and version history.

------------------------------------------------------

Q5. What is the difference between git add and git commit?

Answer:
git add moves modified files from the Working Directory to the Staging Area.

git commit permanently saves the staged snapshot into the Local Git Repository.

------------------------------------------------------

Q6. Why is "update" considered a bad commit message?

Answer:
Because it doesn't describe what actually changed. Good commit messages are descriptive and explain the purpose of the change.

Example:

feat: initialize analytics project structure

------------------------------------------------------

Q7. Why don't we upload .venv to GitHub?

Answer:
The virtual environment is machine-specific and can easily be recreated using requirements.txt. Uploading it unnecessarily increases repository size and may cause compatibility issues.

------------------------------------------------------

Q8. Why do analytics projects begin with a business problem instead of a dataset?

Answer:
Because the business problem determines:
- what data should be collected,
- which analyses should be performed,
- which KPIs matter,
- and what recommendations will be useful.

Without understanding the business problem, analysis has no direction.

------------------------------------------------------

Q9. What is the difference between Data Validation and Data Cleaning?

Answer:

Data Validation:
Ensures that collected data follows predefined business rules and quality standards.

Examples:
- Required fields
- Valid dates
- Correct ranges
- Correct data types

Data Cleaning:
Fixes errors that already exist in the data.

Examples:
- Missing values
- Duplicate records
- Misspellings
- Invalid categories
- Incorrect formats

------------------------------------------------------

Q10. Why do we perform Exploratory Data Analysis (EDA) before statistical testing?

Answer:
EDA helps analysts understand the structure and quality of the data before applying statistical methods.

EDA is used to:
- detect missing values,
- identify outliers,
- examine distributions,
- explore relationships,
- verify assumptions required for statistical tests.

------------------------------------------------------

Q11. Why do we separate data into Raw, Cleaned, Processed, and External folders?

Answer:

Raw:
Original untouched data.

Cleaned:
Data after correcting errors.

Processed:
Merged and transformed data ready for analysis.

External:
Reference datasets obtained from external sources.

This separation improves reproducibility, transparency, and data governance.

------------------------------------------------------

Q12. Why do we use multiple related datasets instead of one huge CSV?

Answer:
Using multiple datasets follows database normalization principles.

Benefits:
- reduces duplication,
- improves consistency,
- simplifies maintenance,
- enables SQL JOIN practice,
- reflects real-world database design.

------------------------------------------------------

Q13. What is the complete analytics lifecycle?

Answer:

1. Business Understanding
2. Requirement Gathering
3. Data Collection
4. Data Validation
5. Data Cleaning
6. Data Transformation
7. Exploratory Data Analysis
8. Statistical Analysis
9. Visualization
10. Dashboard Development
11. Reporting
12. Business Recommendation

------------------------------------------------------

Q14. Why isn't a dashboard the final goal?

Answer:
A dashboard only communicates findings.

The real goal is to support better business decisions based on data-driven insights.

------------------------------------------------------

Q15. Why do we design the project architecture before writing code?

Answer:
A well-designed architecture improves organization, scalability, maintainability, collaboration, and reproducibility. It ensures that coding follows a clear plan instead of becoming disorganized.

------------------------------------------------------

Q16. Why is the Master Coverage Matrix important?

Answer:
It guarantees that every Python, SQL, Statistics, Git, GitHub, and Power BI concept is implemented in a real project. It also tracks progress and ensures no important topic is missed.

------------------------------------------------------

Q17. Which project components help a new analyst understand the project quickly?

Answer:
- README
- Business Requirements
- Data Dictionary
- Master Coverage Matrix
- Git History
- CHANGELOG
- Folder Structure
- SQL Scripts
- Python Scripts
- Analysis Reports
- Dashboard Guide

==============================
DAY 2 PROFESSIONAL QUESTIONS
==============================
✅ Question 1
Why do professional projects design the database before writing Python code?

    "Professional projects design the database before writing Python code because the database defines what information will be collected, how it will be organized, and how entities are related. A well-designed database ensures that all business questions can be answered efficiently. Python is only a tool used to process and analyze the data—the database design determines whether the required analysis is even possible."

    ⭐ Interview Tip "Database design is driven by business requirements. We first identify the questions management needs answered, then design the database to support those questions."

✅ Question 2
Why are Primary Keys and Foreign Keys essential?

    "Primary Keys uniquely identify each record within a table, while Foreign Keys connect related tables. These relationships eliminate data duplication, maintain data integrity, and enable SQL JOIN operations. Without them, it would be impossible to accurately combine information from different datasets such as patients, clinic visits, facilities, laboratory tests, and pharmacy records."

✅ Question 3
Why use multiple related tables instead of one giant CSV?

    "Professional databases are normalized into multiple related tables to reduce redundancy, improve consistency, simplify maintenance, and accurately represent real-world business processes. Smaller related tables also improve query performance, make validation easier, and allow analysts to combine information using SQL JOINs instead of storing duplicated information in every row.
    Advantages:

    ✔ Less duplication

    ✔ Better performance

    ✔ Easier updates

    ✔ Easier validation

    ✔ Easier maintenance

    ✔ More realistic database design

    ✔ Supports SQL relationships

    ✔ Reduces storage requirements"

