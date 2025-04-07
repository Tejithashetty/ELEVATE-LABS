# ELEVATE-LABS TASK 1

## Data Cleaning

This is a simple program of how to clean and handle the Null or Missing values of a dataset

- the observations of the dataset i choose.

## Initial Observations:

Rows: 2,240

Columns: 29

Missing values: Only in the Income column (24 missing entries).

## opertions perfomed in this task for potential cleanup

- Missing values in Income

- Possibly inconsistent date formats in Dt_Customer

- Text standardization in Education and Marital_Status

- Uniform column names (some have uppercase and spaces)

- Data type consistency (e.g., Dt_Customer is a string, should be datetime)



## Summary of Cleaning:

Original rows: 2,240

Rows after cleaning: 2,216

Missing values handled: 24 rows dropped with missing Income

Duplicates removed: 0


Standardized text: education, marital_status → all lowercase and stripped

Date format fixed: dt_customer → converted to proper datetime (dd-mm-yyyy)

Column headers cleaned: All lowercase with underscores

Data types adjusted: Ensured proper formats for date, age, income, etc.
