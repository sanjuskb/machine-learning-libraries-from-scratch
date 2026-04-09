'''

Why we use Pandas (brief & clear)

Pandas is used to work with real-world data easily.

In Machine Learning, data is usually:

Large

Messy

Stored in tables (rows & columns)

Pandas helps us to:

Read data from files (CSV, Excel, etc.)

Organize data in table form

Clean missing or wrong values

Select, filter, and modify data

Prepare data before applying ML models

👉 Without Pandas, ML is almost impossible in practice

-------------------------------------------------------------------------------------------
Pandas Data Structures (types)

Pandas mainly uses two data structures:

Series → 1-D (one-dimensional)

DataFrame → 2-D (rows and columns)

Think like this:

Series = single column

DataFrame = full table (multiple columns)

Series (important concept)
What is a Series?

A Series is a one-dimensional labeled array.

Simple words:

A Series is like a single column of data with an index.

Example:

Marks of students

Temperatures of days

Ages of people

Structure of a Series

A Series has two parts:

Values → actual data

Index → labels for each value

Index →  0   1   2   3
Value → 10  20  30  40

Creating a Series (basic example)
import pandas as pd

s = pd.Series([10, 20, 30, 40])
print(s)


Output:

0    10
1    20
2    30
3    40
dtype: int64


✔ Left side → index
✔ Right side → values

Series with custom index
s = pd.Series([85, 90, 78], index=['Maths', 'Physics', 'Chemistry'])
print(s)


Output:

Maths        85
Physics      90
Chemistry    78


👉 This is very useful in data analysis.

Accessing elements in a Series
print(s['Maths'])   # by index label


or

print(s[0])         # by position

Why Series is important for ML

Each column of a DataFrame is actually a Series

ML features (input columns) are handled as Series

Understanding Series = understanding Pandas basics

'''