A Data Analyst's job is not to write Python code. A Data Analyst's job is to solve business problems using data.


# The Complete Analytics Lifecycle

This diagram is the heart of our entire project.

Business Problem
        │
        ▼
Requirements Gathering
        │
        ▼
Data Collection
        │
        ▼
Data Validation
        │
        ▼
Data Cleaning
        │
        ▼
Data Transformation
        │
        ▼
Exploratory Data Analysis (EDA)
        │
        ▼
Statistical Analysis
        │
        ▼
Visualization
        │
        ▼
Power BI Dashboard
        │
        ▼
Business Report
        │
        ▼
Decision Making

---

## 1️⃣ Business Problem

Example:

> "Malnutrition rates seem to be increasing."

No data yet.

No Python.

Only a problem.

---

## 2️⃣ Requirements Gathering

Now we ask questions.

Example:

What data do we need?

Maybe:

* Beneficiaries
* Age
* Gender
* MUAC
* Governorate
* Distribution history
* Health visits

---

## 3️⃣ Data Collection

Now we receive data.

Usually from multiple sources.

Examples:

```
Excel

CSV

Kobo Toolbox

Google Forms

SQL Database

API
```

Rarely does all data come from one clean file.

---

## 4️⃣ Data Validation

Before cleaning, we ask:

> "Can we trust this data?"

Examples:

```
Age = -10

Date = 2035

Duplicate IDs

Blank governorates

Unknown gender

Impossible MUAC values
```

Validation checks whether the data makes sense.

---

## 5️⃣ Data Cleaning

Now we fix problems.

Examples:

```
Missing values

Duplicates

Wrong spellings

Wrong formats

Extra spaces

Mixed uppercase/lowercase
```

##### This is where analysts spend most of their time.

Validation

↓

Find Problems

↓

Cleaning

↓

Fix Problems

---

## 6️⃣ Data Transformation

Now we prepare the data for analysis.

Examples:

Merge tables.

Create new columns.

Calculate age groups.

Convert dates.

Aggregate records.

Engineer features.

---

## 7️⃣ Exploratory Data Analysis (EDA)

Now we start asking questions.

Examples:

Average age?

Most common governorate?

Distribution by gender?

Monthly trend?

Relationships?

Outliers?

Skewness?

EDA helps us understand what the data is telling us.

---

## 8️⃣ Statistical Analysis

Now we test assumptions.

Examples:

Is one district significantly different from another?

Is the increase in malnutrition statistically significant?

Is there a relationship between household size and assistance?

Now statistics becomes useful.

---

## 9️⃣ Visualization

We communicate the findings.

Charts.

Maps.

KPIs.

Dashboards.

Visualization is for **people**, not computers.

---

## 🔟 Power BI Dashboard

Executives don't read Python code.

They look at dashboards.

We'll build one.

---

## 1️⃣1️⃣ Business Report

Finally, we write:

What happened?

Why?

Evidence?

Recommendations?

Next actions?

---

## 1️⃣2️⃣ Decision Making

This is the real goal.

Not charts.

Not Python.

Not SQL.

We want decision-makers to answer questions like:

> Where should we send the next nutrition team?

> Which district should receive more funding?

> Which facility needs additional training?

---

# 🧩 Where Will We Use Each Technology?

| Technology              | Purpose in This Project                                                  |
| ----------------------- | ------------------------------------------------------------------------ |
| **Python**              | Automate tasks, clean data, perform analysis, calculate metrics.         |
| **NumPy**               | Efficient numerical calculations and array operations.                   |
| **Pandas**              | Load, clean, merge, reshape, and analyze tabular data.                   |
| **Matplotlib**          | Create foundational visualizations.                                      |
| **Seaborn**             | Produce statistical and presentation-ready charts.                       |
| **SciPy / Statsmodels** | Perform hypothesis tests and statistical analysis.                       |
| **SQL**                 | Query and combine relational datasets efficiently.                       |
| **Git / GitHub**        | Track changes, manage versions, and showcase the project professionally. |
| **Power BI**            | Build interactive dashboards for stakeholders.                          
---


# 🧩 Single Responsibility Principle (SRP)

A professional software engineering concept that applies equally well to analytics projects.



==============================
DAY 1 PROFESSIONAL NOTES
==============================

✔ Every analytics project starts with a business problem—not with Python code.

✔ Documentation is just as important as programming.

✔ Never modify the original raw dataset.

✔ Use virtual environments for every Python project.

✔ requirements.txt is the project's dependency blueprint.

✔ Write meaningful commit messages.

✔ Commit frequently with small logical changes.

✔ Always review changes using:
git status
git diff

before committing.

✔ Organize projects before writing code.

✔ Professional projects separate:
- Raw Data
- Cleaned Data
- Processed Data
- External Data

✔ Analytics is a complete workflow:

Business
↓

Data
↓

Cleaning

↓

EDA

↓

Statistics

↓

Visualization

↓

Dashboard

↓

Recommendation

✔ Dashboards communicate findings.
They do not make decisions.

✔ Always understand WHY before writing HOW.

✔ Every folder should have a clear purpose.

✔ Good projects are reproducible.

✔ Git is your project's time machine.

✔ GitHub is your portfolio, collaboration platform, and remote backup.

✔ Business understanding determines:
- required datasets,
- KPIs,
- analyses,
- and final recommendations.

✔ A normalized relational dataset is better than one massive spreadsheet.

✔ A professional analyst always asks:
"What business decision will this analysis support?"

==============================
DAY 1 COMMANDS MASTERED
==============================

Python:
- python --version
- where python
- pip install
- pip freeze

Git:
- git init
- git status
- git add
- git commit
- git push
- git log
- git diff

PowerShell:
- mkdir
- New-Item
- Remove-Item
- tree /F
- Get-ChildItem

==============================
DAY 1 PROFESSIONAL MINDSET
==============================

A Data Analyst is not hired to write Python code.

A Data Analyst is hired to solve business problems using data.

Python, SQL, Statistics, Power BI, and Git are simply the tools used to achieve that goal.

=========================================
DAY 1 PROFESSIONAL NOTES & BEST PRACTICES
=========================================

====================================================
SECTION 1 — THE PROFESSIONAL DATA ANALYST MINDSET
====================================================

✔ A Data Analyst is hired to solve business problems, not to write Python code.

✔ Business understanding always comes before coding.

✔ Never start analysis until you understand:
    • Business Problem
    • Business Objectives
    • Stakeholders
    • KPIs
    • Expected Deliverables

✔ Every analysis should answer a business question.

✔ Every chart, SQL query, and Python script should support a business decision.

✔ The final goal is not a dashboard.
The final goal is making better business decisions.

----------------------------------------------------

====================================================
SECTION 2 — ANALYTICS LIFECYCLE
====================================================

Professional Analytics Workflow

Business Understanding
        ↓
Requirement Gathering
        ↓
Data Collection
        ↓
Data Validation
        ↓
Data Cleaning
        ↓
Data Transformation
        ↓
Exploratory Data Analysis (EDA)
        ↓
Statistical Analysis
        ↓
Visualization
        ↓
Dashboard Development
        ↓
Reporting
        ↓
Recommendations
        ↓
Business Decision

Never skip steps.

----------------------------------------------------

====================================================
SECTION 3 — BUSINESS PROBLEM vs BUSINESS OBJECTIVE
====================================================

Business Problem

The issue the organization wants to solve.

Example:

High malnutrition among children under five.

----------------------------------------

Business Objective

The measurable outcome expected after solving the problem.

Example:

Reduce severe acute malnutrition by 20% within one year.

Business Problem answers:

"What is wrong?"

Business Objective answers:

"What do we want to achieve?"

----------------------------------------------------

====================================================
SECTION 4 — DATA VALIDATION vs DATA CLEANING
====================================================

Data Validation

Checks whether incoming data follows predefined business rules.

Examples

✔ Required values
✔ Correct data types
✔ Valid date formats
✔ Valid ID formats
✔ Allowed categories
✔ Logical ranges

----------------------------------------

Data Cleaning

Corrects existing data problems.

Examples

✔ Missing values
✔ Duplicate records
✔ Misspelled categories
✔ Invalid dates
✔ Wrong data types
✔ Impossible values
✔ Extra spaces
✔ Mixed text case

Validation checks quality.

Cleaning fixes quality problems.

----------------------------------------------------

====================================================
SECTION 5 — WHY PERFORM EDA BEFORE STATISTICS?
====================================================

EDA allows analysts to:

✔ Understand distributions

✔ Detect missing values

✔ Identify outliers

✔ Understand relationships

✔ Verify assumptions

✔ Decide which statistical tests are appropriate

Never perform hypothesis testing before understanding your data.

----------------------------------------------------

====================================================
SECTION 6 — PROJECT ARCHITECTURE
====================================================

Professional projects separate files into dedicated folders.

Benefits

✔ Easier maintenance

✔ Easier collaboration

✔ Easier debugging

✔ Easier scaling

✔ Easier onboarding

✔ Better organization

Poor organization becomes expensive as projects grow.

----------------------------------------------------

====================================================
SECTION 7 — DATA LAYERS
====================================================

RAW

Original untouched data.

Never modify.

----------------------------------------

CLEANED

Errors corrected.

Duplicates removed.

Missing values handled.

----------------------------------------

PROCESSED

Merged.

Grouped.

Aggregated.

Feature engineered.

Ready for analysis.

----------------------------------------

EXTERNAL

Reference datasets obtained from outside the organization.

Examples

Population

Exchange rates

Weather

Administrative boundaries

----------------------------------------------------

====================================================
SECTION 8 — WHY KEEP RAW DATA?
====================================================

Never overwrite original datasets.

Reasons

✔ Backup

✔ Reproducibility

✔ Audit trail

✔ Error recovery

✔ Comparison

Raw data is the source of truth.

----------------------------------------------------

====================================================
SECTION 9 — WHY MULTIPLE DATASETS?
====================================================

Professional organizations rarely store everything in one spreadsheet.

Instead they normalize data.

Benefits

✔ Less duplication

✔ Smaller tables

✔ Easier updates

✔ Better consistency

✔ SQL JOIN practice

✔ Realistic database design

----------------------------------------------------

====================================================
SECTION 10 — PROJECT DOCUMENTATION
====================================================

Every professional project should include

README

Business Requirements

Data Dictionary

KPIs

Cleaning Log

Analysis Report

Dashboard Guide

CHANGELOG

Master Coverage Matrix

ER Diagram

Good documentation reduces onboarding time dramatically.

----------------------------------------------------

====================================================
SECTION 11 — WHY CREATE PROJECT ARCHITECTURE FIRST?
====================================================

Architecture provides

✔ Project roadmap

✔ Folder organization

✔ Dataset planning

✔ SQL planning

✔ Dashboard planning

✔ Documentation planning

✔ Script planning

Without architecture

Projects become disorganized quickly.

----------------------------------------------------

====================================================
SECTION 12 — MASTER COVERAGE MATRIX
====================================================

Purpose

✔ Track every concept studied

✔ Ensure nothing is forgotten

✔ Connect theory with practice

✔ Track progress

✔ Support interview preparation

✔ Demonstrate portfolio evidence

This matrix guarantees every concept is implemented.

----------------------------------------------------

====================================================
SECTION 13 — DATASET PLANNING
====================================================

Before collecting data define

✔ Required tables

✔ Relationships

✔ Primary Keys

✔ Foreign Keys

✔ Required fields

✔ Data types

✔ Expected outputs

Good planning prevents redesign later.

----------------------------------------------------

====================================================
SECTION 14 — THINKING LIKE A SQL ANALYST
====================================================

Whenever someone asks

"Calculate average waiting time by governorate."

Do NOT immediately think

Python

Instead think

Which tables are involved?

Example

Patients

↓

Clinic Visits

↓

Health Facilities

↓

Governorates

Always identify required datasets before writing queries.

----------------------------------------------------

====================================================
SECTION 15 — PROJECT COMPONENTS
====================================================

A new analyst should understand the project using

README

↓

Business Requirements

↓

Folder Structure

↓

Data Dictionary

↓

Git History

↓

Python Scripts

↓

SQL Scripts

↓

Dashboard Guide

↓

Analysis Reports

↓

Master Coverage Matrix

Professional projects should be self-explanatory.

----------------------------------------------------

====================================================
SECTION 16 — GIT BEST PRACTICES
====================================================

✔ Commit frequently

✔ Small logical commits

✔ Meaningful commit messages

✔ Review using git status

✔ Review using git diff

✔ Check history using git log

Git is your project's time machine.

----------------------------------------------------

====================================================
SECTION 17 — INTERVIEW THINKING
====================================================

Managers rarely ask

"Write Python."

Instead they ask

Which clinic performs worst?

Why is malnutrition increasing?

Should funding be increased?

What recommendations do you have?

Always think

Business first.

Technology second.

----------------------------------------------------

====================================================
SECTION 18 — PROJECT PHILOSOPHY
====================================================

Throughout this bootcamp we will implement

✔ Every Python syntax

✔ Every NumPy concept

✔ Every Pandas concept

✔ Every Statistics concept

✔ Every Sampling technique

✔ Every Hypothesis Test

✔ Every SQL concept

✔ Every Git command

✔ Every GitHub concept

✔ Every Power BI feature

inside ONE professional humanitarian analytics platform.

Nothing will be studied in isolation.

Everything will be connected to a real business problem.

----------------------------------------------------

====================================================
SECTION 19 — DAY 1 TAKEAWAYS
====================================================

✔ Planning saves development time.

✔ Documentation is code.

✔ Business understanding is mandatory.

✔ Analytics is a complete lifecycle.

✔ Architecture comes before implementation.

✔ Professional projects separate data into layers.

✔ Raw data is never modified.

✔ SQL starts by identifying tables, not writing queries.

✔ Dashboards communicate insights—they don't make decisions.

✔ The best analysts ask "Why?" before "How?".

====================================================
END OF DAY 1 NOTES
====================================================

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

