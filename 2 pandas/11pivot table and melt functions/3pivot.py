import pandas as pd

var = pd.DataFrame({
    "days": [1,1,1,1,5,6],
    "st_name": ["a","b","c","a","b","c"],
    "eng": [10,12,14,15,16,12],
    "maths": [17,18,19,13,14,16]
})
print(var)
print()
# print(var.pivot(index="days", columns="st_name"))shows error because 
'''
1️⃣ Your DataFrame (what Pandas sees)
   days st_name  eng  maths
0     1       a   10     17
1     1       b   12     18
2     1       c   14     19
3     1       a   15     13
4     5       b   16     14
5     6       c   12     16


Focus on day = 1 👇
For days = 1 and st_name = a, you have TWO rows:

(1, a) → eng = 10
(1, a) → eng = 15


⚠️ That is the root problem.

2️⃣ Why pivot() is failing

You wrote:

var.pivot(index="days", columns="st_name")

What Pandas is trying to do:

Rows → days

Columns → st_name

Values → ❓ (Pandas doesn’t know which column to use)

Even if you specify values, the real issue remains:

3️⃣ The Golden Rule of pivot()

🚨 pivot() requires ONE value per (index, column) pair

This must be true:

(days, st_name) → exactly ONE row


But in your data:

(1, a) → TWO rows ❌


So Pandas raises this error:

ValueError: Index contains duplicate entries, cannot reshape
'''

print(var.pivot_table(index="days", columns="st_name", aggfunc="sum"))

'''
          eng             maths
st_name     a     b     c     a     b     c
days
1        25.0  12.0  14.0  30.0  18.0  19.0
5         NaN  16.0   NaN   NaN  14.0   NaN
6         NaN   NaN  12.0   NaN   NaN  16.0

------------------------------------------------------------------------------
What is aggfunc?

aggfunc = Aggregation Function

👉 It tells Pandas how to combine multiple values into ONE value when duplicates exist.

Why do we need aggfunc?

In your data you had this situation:

days = 1, st_name = 'a'
eng = 10
eng = 15


Two values for the same (days, st_name) pair.

Pandas asks:

“I need ONE value. What should I do with 10 and 15?”

That’s where aggfunc comes in.

What does aggfunc="sum" do?
var.pivot_table(
    index="days",
    columns="st_name",
    values="eng",
    aggfunc="sum"
)

Meaning in plain English 👇

➡️ If multiple values exist,
➡️ add them together.

Example:

10 + 15 = 25


So Pandas stores 25 in that cell.

Common aggfunc values (easy to remember)
aggfunc	What it does
"sum"	Adds values
"mean"	Average
"max"	Largest value
"min"	Smallest value
"count"	Number of values

Example:

aggfunc="mean"   # (10 + 15) / 2 = 12.5
aggfunc="max"    # 15
aggfunc="count"  # 2

One-line definition (exam perfect)

aggfunc specifies how duplicate values are combined when reshaping data using pivot_table()

Why pivot() doesn’t have aggfunc

Because:

pivot() assumes no duplicates

So there is nothing to aggregate

That’s why aggfunc exists only in pivot_table()

Final clarity sentence 🧠

If your data can have duplicates → use pivot_table() with aggfunc

---------------------------------------------------------------------------
Mental model (remember this)

pivot() → “I promise there is only one value”

pivot_table() → “There may be many values, please combine them”
'''
print()

print(var.pivot_table(index="days", columns="st_name", aggfunc="sum",margins=True))
'''
          eng                 maths
st_name     a     b     c All     a     b     c All
days
1        25.0  12.0  14.0  51  30.0  18.0  19.0  67
5         NaN  16.0   NaN  16   NaN  14.0   NaN  14
6         NaN   NaN  12.0  12   NaN   NaN  16.0  16
All      25.0  28.0  26.0  79  30.0  32.0  35.0  97

margins=True adds totals (sum) for rows and columns
Pandas adds:

1️⃣ Extra column → total of each row
2️⃣ Extra row → total of each column

The label is All by default.
'''