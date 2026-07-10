
# 2. Normalization

## What is Normalization?

Normalization is the process of organizing data to reduce duplication and improve consistency.

**Goal:**

* Minimize repeated data.
* Improve data quality.
* Make updates easier.
* Save storage.
* Maintain consistency.

---

## Example WITHOUT normalization ❌

| Patient_ID | Patient Name | Governorate | Facility   | Visit Date |
| ---------- | ------------ | ----------- | ---------- | ---------- |
| 1          | Ahmad        | Aleppo      | Hospital A | Jan        |
| 1          | Ahmad        | Aleppo      | Hospital A | Feb        |
| 1          | Ahmad        | Aleppo      | Hospital A | Mar        |

The patient's information is repeated in every visit.

Problems:

* Wasted storage.
* If Ahmad changes his name or address, you must update many rows.
* Easy to introduce inconsistencies.

---

## Example WITH normalization ✅

### Patients

| Patient_ID | Name  | Governorate |
| ---------- | ----- | ----------- |
| 1          | Ahmad | Aleppo      |

### Clinic_Visits

| Visit_ID | Patient_ID | Facility   | Visit Date |
| -------- | ---------- | ---------- | ---------- |
| 1001     | 1          | Hospital A | Jan        |
| 1002     | 1          | Hospital A | Feb        |
| 1003     | 1          | Hospital A | Mar        |

Patient information is stored once, and visits reference it via `Patient_ID`.

---

## The Three Normal Forms (Simplified)

### 1NF (First Normal Form)

Each column contains a single value.

❌

| Patient | Diseases    |
| ------- | ----------- |
| Ahmad   | Flu, Asthma |

✅

| Patient | Disease |
| ------- | ------- |
| Ahmad   | Flu     |
| Ahmad   | Asthma  |

---

### 2NF (Second Normal Form)

Every non-key column must depend on the whole primary key.

Think:

No unnecessary repeated information.

---

### 3NF (Third Normal Form)

Columns should depend only on the primary key.

Example:

❌

Patients table

| Patient_ID | District | Governorate |

Governorate depends on District, not directly on Patient.

Better:

Patients

↓

Districts

↓

Governorates

---

**Interview Tip**

You don't need to memorize formal definitions. Explain the idea:

> "Normalization reduces duplication and organizes data into related tables to improve consistency and make maintenance easier."

---

# 3. Fact vs Dimension Tables

This is a core data warehousing concept.

## Fact Table

Stores measurable events or transactions.

Examples:

* Clinic visits
* Lab requests
* Pharmacy dispensing
* Vaccinations

Contains numbers you analyze.

Example:

| Visit_ID | Patient_ID | Facility_ID | Waiting_Time |
| -------- | ---------- | ----------- | ------------ |
| 1001     | 1          | 10          | 18           |

---

## Dimension Table

Describes the facts.

Examples:

* Patients
* Facilities
* Staff
* Governorates
* Dates

Example:

| Patient_ID | Gender | Age Group |
| ---------- | ------ | --------- |
| 1          | Male   | 18–64     |

---

### Think of it this way:

**Facts answer:**

> What happened?

**Dimensions answer:**

> Who? Where? When? How?

---

### Example

Business Question:

Average waiting time by governorate.

Fact:

Clinic_Visits

Dimension:

Governorates

---

# 4. Primary Key (PK)

A Primary Key uniquely identifies every row in a table.

Example:

Patients

| Patient_ID | Name  |
| ---------- | ----- |
| 1          | Ahmad |
| 2          | Sara  |

`Patient_ID` is the PK.

Rules:

* Unique.
* Cannot be NULL.
* One PK per table.

---

# 5. Foreign Key (FK)

A Foreign Key links one table to another.

Example:

Patients

| Patient_ID | Name  |
| ---------- | ----- |
| 1          | Ahmad |

Visits

| Visit_ID | Patient_ID |
| -------- | ---------- |
| 100      | 1          |

`Patient_ID` in Visits is an FK pointing to the Patients table.

Think of it as a "reference" that creates relationships between tables.

---

# 6. One-to-Many Relationships (1:M)

One record in the parent table relates to many records in the child table.

Example:

One patient

↓

Many visits

```text
Patient
   │
   ├── Visit 1
   ├── Visit 2
   ├── Visit 3
```

Other examples in our project:

* One facility → many visits.
* One doctor → many consultations.
* One governorate → many facilities.

---

# 7. Master / Reference Data

These are stable tables that define allowed values.

Examples:

* Diseases
* Departments
* Medicines
* Vaccines
* Staff Roles
* Facility Types

Instead of typing "Pediatrics" manually every time, we reference a master table.

Benefits:

* Consistency.
* Easier updates.
* No spelling variations.
* Better joins.

---

# 8. Transactional Data

These tables record events.

Examples:

* Clinic Visits
* Laboratory Requests
* Pharmacy Dispensing
* Nutrition Screenings

Characteristics:

* Grow continuously.
* Large number of records.
* Linked to master tables via foreign keys.

---

# 9. Relational Healthcare Database Design

Our project will be a relational database where tables are connected rather than duplicated.

Example:

```text
Patients
   │
   ├── Clinic_Visits
   │        │
   │        ├── Laboratory_Requests
   │        ├── Pharmacy_Dispensing
   │        ├── Vaccinations
   │        └── Referrals
   │
Facilities
   │
Departments
   │
Staff
```

This design allows us to answer complex questions by joining tables.

---

# 🎤 Interview Questions & Professional Answers

### 1. Why normalize a database?

**Professional answer:**

> Normalization reduces data duplication, improves consistency, simplifies updates, and maintains data integrity by storing related information in separate linked tables.

---

### 2. What is the difference between a fact table and a dimension table?

**Professional answer:**

> Fact tables store measurable business events, such as clinic visits or laboratory requests, while dimension tables provide descriptive information, such as patient demographics, facilities, or dates, used to analyze those events.

---

### 3. Why separate master data from transactional data?

**Professional answer:**

> Master data changes infrequently and provides standardized reference information, while transactional data records daily business activities. Separating them reduces redundancy, improves consistency, and simplifies maintenance.

---

### 4. Why are lookup tables useful?

**Professional answer:**

> Lookup tables ensure standardized values across the database, prevent spelling inconsistencies, simplify maintenance, and improve data quality and query performance.

---

### 5. Why design the database before generating data?

**Professional answer:**

> Database design defines the required entities, relationships, and business rules before data generation. This ensures that generated data is realistic, internally consistent, and capable of answering the intended business questions without major redesign later.

---

## 💡 Memory Trick

When you're asked to design a database in an interview, think in this order:

```text
Business Problem
        ↓
Business Questions
        ↓
KPIs
        ↓
Entities (Tables)
        ↓
Relationships (PK/FK)
        ↓
Business Rules
        ↓
Generate / Collect Data
        ↓
Analyze
        ↓
Visualize
        ↓
Recommend Actions
```

This flow is the backbone of our project. Every dataset we generate, every SQL query we write, every Python analysis, and every Power BI dashboard will follow this same sequence, which is why we're spending time getting it right before writing code.

| Concept                     | Master Data Dimentional     | Lookup (Reference) Data                     | Fact (Transactional) Data                 |
| --------------------------- | --------------------------- | ------------------------------------------- | ----------------------------------------- |
| Changes frequently?         | Rarely                      | Very rarely                                 | Continuously                              |
| Number of records           | Medium                      | Small                                       | Very large                                |
| Contains business entities? | Yes                         | Usually just allowed values                 | Yes (events/transactions)                 |
| Used in joins?              | Yes                         | Yes                                         | Yes                                       |
| Examples                    | Patients, Staff, Facilities | Diseases, Departments, Governorates, Gender | Visits, Lab Requests, Pharmacy Dispensing |

