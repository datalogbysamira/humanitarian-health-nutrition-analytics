==============================
DAY 1 INTERVIEW QUESTIONS
==============================

Q1.
Tell me about the first step of any data analytics project.

Professional Answer:

The first step is understanding the business problem. Before collecting or analyzing data, I work with stakeholders to identify business objectives, define KPIs, understand success criteria, and determine which data is required to answer the business questions.

------------------------------------------------------

Q2.
How do you organize your analytics projects?

Professional Answer:

I organize projects into clearly separated folders including:

- raw data
- cleaned data
- processed data
- external data
- Python scripts
- SQL scripts
- documentation
- reports
- outputs
- Power BI
- tests

This structure improves maintainability, collaboration, and reproducibility.

------------------------------------------------------

Q3.
Explain the Git workflow.

Professional Answer:

The Git workflow consists of:

Working Directory

↓

Staging Area (git add)

↓

Local Repository (git commit)

↓

Remote Repository (git push)

This workflow allows changes to be reviewed before they become part of the project history.

------------------------------------------------------

Q4.
What would you do if another analyst joined your project?

Professional Answer:

I would ensure the project contains:

- README
- Business Requirements
- Data Dictionary
- Documentation
- Git history
- Clear folder structure
- SQL scripts
- Python scripts
- Dashboard documentation

This enables the new analyst to understand the project quickly and contribute efficiently.

------------------------------------------------------

Q5.
Why is documentation important?

Professional Answer:

Documentation improves collaboration, simplifies maintenance, supports onboarding of new team members, and preserves business knowledge throughout the project lifecycle.

------------------------------------------------------

Q6.
Why shouldn't analysts modify raw data?

Professional Answer:

Raw data should always remain unchanged because it serves as the original source of truth. Any cleaning or transformation should be performed on copies to ensure reproducibility and allow recovery if mistakes occur.

------------------------------------------------------

Q7.
How would you answer a manager asking:
"Which governorate should receive more funding?"

Professional Answer:

I would not answer immediately. I would first validate the data, perform exploratory analysis, calculate relevant KPIs, compare historical performance, analyze trends, and investigate the root causes before making a recommendation.



# ⭐⭐⭐⭐⭐ Interview Question

    "How do you organize your data analytics projects?"


I organize my projects by separating responsibilities into dedicated folders so that the project is easy to understand, maintain, and reproduce. I keep the original datasets in data/raw and never modify them. After validation and cleaning, I save cleaned datasets in data/cleaned and analysis-ready datasets in data/processed. Any external datasets, such as population statistics or reference tables, are stored in data/external.

I separate Python scripts by responsibility. For example, one script loads data, another validates and cleans it, another performs statistical analysis, and another creates visualizations. This modular approach makes debugging, testing, and maintaining the code much easier.

SQL queries are stored in a dedicated sql folder, while Power BI dashboards are kept in a powerbi folder. Project documentation, business rules, and learning notes are stored in docs, generated reports are saved in reports, and all automatically generated files, such as summary tables and charts, are written to outputs.

I also use Git and GitHub throughout the project to track every change with meaningful commits, maintain version history, and collaborate effectively. This structure makes the project reproducible, scalable, and easy for other analysts to understand and continue.

## ⭐ The Complete Lifecycle of DATA ANALYSIS

Business Problem
        │
        ▼
Business Objective
        │
        ▼
Business Questions
        │
        ▼
Required Data
        │
        ▼
Data Collection
        │
        ▼
Validation
        │
        ▼
Cleaning
        │
        ▼
Transformation
        │
        ▼
EDA
        │
        ▼
Statistics
        │
        ▼
Visualization
        │
        ▼
Dashboard
        │
        ▼
Business Report
        │
        ▼
Decision

This is the lifecycle we'll follow throughout the project.


## 🎤 Interview Question

  "Describe your daily Git workflow."

I first understand the business task, implement and test the changes, review them with git status, stage only the relevant files, create a meaningful commit describing the change, review the history if needed, push to GitHub, and update the project documentation. This keeps the repository organized and makes collaboration much easier.

## 🎯 Interview Tip

  "How do you make your Git history easy for your team to understand?"

I create small, focused commits that each represent a single logical change. Before committing, I review the modified files with git status, test my code, and write descriptive commit messages. This makes it easy to trace changes, debug issues, and collaborate with other developers.


## 🎤 Interview Questions & Professional Answers - DAY 2
1. Why normalize a database?

Professional answer:

Normalization reduces data duplication, improves consistency, simplifies updates, and maintains data integrity by storing related information in separate linked tables.

2. What is the difference between a fact table and a dimension table?

Professional answer:

Fact tables store measurable business events, such as clinic visits or laboratory requests, while dimension tables provide descriptive information, such as patient demographics, facilities, or dates, used to analyze those events.

3. Why separate master data from transactional data?

Professional answer:

Master data changes infrequently and provides standardized reference information, while transactional data records daily business activities. Separating them reduces redundancy, improves consistency, and simplifies maintenance.

4. Why are lookup tables useful?

Professional answer:

Lookup tables ensure standardized values across the database, prevent spelling inconsistencies, simplify maintenance, and improve data quality and query performance.

5. Why design the database before generating data?

Professional answer:

Database design defines the required entities, relationships, and business rules before data generation. This ensures that generated data is realistic, internally consistent, and capable of answering the intended business questions without major redesign later.