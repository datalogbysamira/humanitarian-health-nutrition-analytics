Mission 19 — Generate Data with Python

This is where your project changes from documentation to software development.

I would slightly redesign Mission 19 to resemble a real Data Analyst project.

Mission 19.1 — Project Structure
Humanitarian_Analytics_Project/

data/
    raw/
    generated/
    cleaned/
    validation/

python_scripts/

    config.py
    helpers.py

    generate_facilities.py
    generate_staff.py
    generate_patients.py

    validate_data.py
    clean_data.py

docs/


Exactly like a real project.

Mission 19.2 — Read Lookup Tables

Instead of hardcoding values.

Python reads

Governorates.csv
Districts.csv
Departments.csv
Facility_Types.csv
Staff_Roles.csv
Visit_Types.csv
Medicines.csv
Diagnoses.csv
...

using pandas.

Example

governorates = pd.read_csv("data/raw/Governorates.csv")
departments = pd.read_csv("data/raw/Departments.csv")
facility_types = pd.read_csv("data/raw/Facility_Types.csv")

This immediately teaches

pandas
read_csv
dataframe operations
Mission 19.3 — Generate Facilities

Output

Facilities.csv

Approximately

120 facilities

Each facility should have

Facility_ID
Facility_Name
Facility_Type_ID
Governorate_ID
District_ID
Latitude
Longitude
Capacity
Opening_Date
Ownership
Status

Facility distribution should NOT be random.

Example

Hospitals

10%

PHCs

55%

Mobile Clinics

20%

Nutrition Centers

10%

Rehabilitation Centers

5%

Already using

numpy.random.choice(weights=...)
Mission 19.4 — Generate Staff

Output

Staff.csv

Approximately

900 staff

Distribution

Doctors

12%

Nurses

35%

Nutritionists

6%

Lab

6%

Pharmacy

5%

Midwives

5%

Administration

31%

Each employee

Staff_ID
First_Name
Last_Name
Gender
DOB
Hire_Date
Role_ID
Department_ID
Facility_ID
Salary
Employment_Type
Status
Mission 19.5 — Generate Patients

Largest master table.

40000 patients

Columns

Patient_ID
National_ID
First_Name
Last_Name
Gender
DOB
Age
Nationality
Governorate_ID
District_ID
Phone
Registration_Date
Blood_Group
Marital_Status
Disability
Alive
Mission 19.6 — Introduce Realistic Imperfections

This is what almost every portfolio misses.

Generate good data first.

Then intentionally introduce issues.

Example

Missing Values
2%

Phone

NULL

Duplicate Patients

0.5%

Wrong Phone Length

1%

Future DOB

0.2%

Age mismatch

DOB says 12

Age column says 25

Extra Spaces

"   Ahmad"

Mixed Case

ahmad

AHMAD

AhMad

Null District

District_ID

NULL

Invalid District

DIST999

Inactive Facility

Patient registered in

Inactive facility

Wrong Gender

M

Male

male

F

Female

instead of standardized values.

Mission 19.7 — Validation

Now write

validate_data.py

Checks

✓ duplicate PK

✓ FK existence

✓ missing values

✓ invalid dates

✓ future dates

✓ age consistency

✓ phone format

✓ categorical values

✓ district belongs to governorate

Mission 19.8 — Cleaning

Now write

clean_data.py

Tasks

remove duplicates

trim spaces

normalize gender

normalize names

recalculate age

fix dates

remove impossible values

standardize text

Mission 19.9 — Git

Commit

Mission 19

Generated master datasets (Facilities, Staff, Patients)

Added validation pipeline

Added cleaning pipeline

Implemented realistic synthetic healthcare data generation
Why I like this redesign

Notice something important.

From this point onward, every single mission will naturally use:

✅ Python
✅ Pandas
✅ NumPy
✅ File I/O
✅ Random distributions
✅ Functions
✅ Dictionaries
✅ Loops
✅ Classes (later, if we choose)
✅ Validation
✅ Cleaning
✅ Statistics
✅ Git
✅ SQL-ready data
✅ Power BI-ready data