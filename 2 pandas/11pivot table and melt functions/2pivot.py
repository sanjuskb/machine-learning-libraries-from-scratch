import pandas as pd

var = pd.DataFrame({
    "days": [1,2,3,4,5,6],
    "st_name": ["a","b","c","a","b","c"],
    "eng": [10,12,14,15,16,12],
    "maths": [17,18,19,13,14,16]
})
print(var)
'''
      days  st_name      eng    maths
0     1       a           10     17
1     2       b           12     18
2     3       c           14     19
3     4       a           15     13
4     5       b           16     14
5     6       c           12     16
'''   
print()
print(var.pivot(index="days", columns="st_name")
)
'''
          eng             maths
st_name     a     b     c     a     b     c
days
1        10.0   NaN   NaN  17.0   NaN   NaN
2         NaN  12.0   NaN   NaN  18.0   NaN
3         NaN   NaN  14.0   NaN   NaN  19.0
4        15.0   NaN   NaN  13.0   NaN   NaN
5         NaN  16.0   NaN   NaN  14.0   NaN
6         NaN   NaN  12.0   NaN   NaN  16.0
------------------------------------------------------------------
1️⃣ First, understand the data you have
var = pd.DataFrame({
    "days": [1,2,3,4,5,6],
    "st_name": ["a","b","c","a","b","c"],
    "eng": [10,12,14,15,16,12],
    "maths": [17,18,19,13,14,16]
})


This is long-format data:

Each row = one observation

Subjects (eng, maths) are columns

Student names repeat

2️⃣ What does pivot() do? (Core idea)

👉 pivot() reshapes data from long → wide

In simple words:

Pivot converts rows into columns

3️⃣ Pivot syntax (very important)
DataFrame.pivot(index=..., columns=..., values=...)

Parameter	Meaning
index	What stays as rows
columns	What becomes new columns
values	Data to fill inside the table
4️⃣ Apply pivot to your data (logical choice)

We want:

Rows → days

Columns → st_name

Values → eng (or maths)

Example 1: Pivot for English marks
var.pivot(index="days", columns="st_name", values="eng")

Output idea:
st_name   a     b     c
days
1       10    NaN   NaN
2       NaN   12    NaN
3       NaN   NaN   14
4       15    NaN   NaN
5       NaN   16    NaN
6       NaN   NaN   12


✔ Rows = days
✔ Columns = students
✔ Values = English marks

5️⃣ Pivot for Maths marks
var.pivot(index="days", columns="st_name", values="maths")


Same structure, different subject.

6️⃣ Why do NaN values appear?

Because:

On day 1, only student a exists

No data for b or c → NaN

👉 Pivot does NOT create new data
👉 It only rearranges existing data

7️⃣ Very important rule of pivot()

🚨 Pivot requires unique combinations

This must be true:

(index, columns) → ONE value only


If duplicates exist → ❌ error

That’s why:

pivot() → strict

pivot_table() → flexible (can aggregate)

8️⃣ Melt vs Pivot (one-line clarity)
Function	Purpose
melt()	Wide → Long
pivot()	Long → Wide

👉 They are opposites

9️⃣ Why we even need pivot in real life?

Machine Learning feature tables

Student report cards

Sales dashboards

Time-series reshaping

Excel-style analysis in Python

🔑 Final one-line intuition

pivot() is like creating an Excel Pivot Table using Python
'''

print()
print(var.pivot(index="days", columns="st_name",values="eng")
)
'''
st_name     a     b     c
days
1        10.0   NaN   NaN
2         NaN  12.0   NaN
3         NaN   NaN  14.0
4        15.0   NaN   NaN
5         NaN  16.0   NaN
6         NaN   NaN  12.0
'''
