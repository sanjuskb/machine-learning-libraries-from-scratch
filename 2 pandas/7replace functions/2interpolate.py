import pandas as pd
csv1=pd.read_csv("C:\\Users\\sanju\\OneDrive\\Desktop\\ml libraries\\pandas\\Test_new11.csv")
print(csv1)
print()
'''
     a    b     c
0   1.0  5.0  11.0
1   NaN  2.0   2.0
2   3.0  NaN   NaN
3   4.0  6.0   NaN
4   NaN  NaN   NaN
5   6.0  6.0   NaN
6   6.0  5.0   NaN
7   3.0  NaN   6.0
8   NaN  1.0   3.0
9   NaN  5.0   NaN
10  1.0  3.0   4.

'''
print(csv1.interpolate())#it fills the missing values automatically and only works for numbers and doesnot work for strings 
print()


print(csv1.interpolate(limit=2))
print()
'''
Your code
print(csv1.interpolate(limit=2))

Important comparison
This:
csv1.interpolate(limit=2)


Means:

“Fill at most 2 consecutive NaNs per block per column”


You expected:

“Limit = 2 should apply the same way to all columns”

But you observed:

“It looks like limit=2 is applied only to the last column”

👉 What you’re seeing is correct behavior, and here’s why.

🔑 The MOST IMPORTANT RULE (this explains everything)

limit in interpolate() applies ONLY to consecutive NaNs in a column

Not:

total NaNs in a column ❌

number of NaNs in the whole DataFrame ❌

But:

continuous (back-to-back) NaNs ✅

How Pandas actually processes interpolate(limit=2)

Pandas works column by column, top to bottom.

For each column separately:

Find blocks of consecutive NaNs

Interpolate at most limit NaNs per block

Stop when the block is broken by a real value

Why it looks like only column c is affected

Because column c is the only one that has long consecutive NaNs.

Let’s analyze briefly.

Column a

Example pattern (simplified):

1, NaN, 3, 4, NaN, 6, 6, 3, NaN, NaN, 1


NaNs appear:

mostly single

blocks of size 1 or 2

broken frequently by valid numbers

👉 limit=2 never blocks interpolation
👉 So all NaNs get filled

Column b

Pattern:

5, 2, NaN, 6, NaN, 6, 5, NaN, 1, 5, 3


Again:

NaNs are isolated

Not long runs

👉 limit=2 has no visible restriction

Column c (THIS IS THE KEY)

Pattern:

11, 2, NaN, NaN, NaN, NaN, NaN, 6, 3, NaN, 4


Here you have:

NaN, NaN, NaN, NaN, NaN   ← 5 consecutive NaNs


Now apply:

limit = 2


Result:

(first 2 NaNs) → interpolated
(remaining NaNs) → stay NaN


✅ That’s exactly what you’re seeing.
'''
print(csv1.interpolate(limit_direction="forward",limit=2))#from the top fill 2
print()
print(csv1.interpolate(limit_direction="backward",limit=2))#from the bottom fill 2
print()
print(csv1.interpolate(limit_direction="both",limit=2))#from the top 2 and from the bottom 2
print()
print(csv1.interpolate(limit_area="inside"))#fills all the null values
print()
print(csv1.interpolate(limit_area="outside"))#remains all nan values same
'''
print(csv1.interpolate())
What interpolate() means (simple)
Fill missing values (NaN) using values before and after them

It estimates missing data instead of guessing or using a constant.

By default:

Method = "linear"

Axis = column-wise (axis=0)

Column-by-column explanation
🔹 Column a
Values:

r
Copy code
NaN, NaN, 3, 4, NaN, 6
Interpolation logic:

Missing values are filled using a straight line between known values

Result:

Copy code
2, 2.5, 3, 4, 5, 6
Why?

Between 3 and 6 → evenly spaced

Values before first known value are forward-filled logically

🔹 Column b
Values:

r
Copy code
NaN, 2, 5, 6, NaN, 6
Interpolated result:

Copy code
2, 2, 5, 6, 6, 6
Explanation:

NaN at top → filled using first valid value

NaN between 6 and 6 → stays 6

🔹 Column c
Values:

r
Copy code
11, 2, 3, 4, 55, NaN
Interpolated result:

Copy code
11, 2, 3, 4, 55, 55
Explanation:

NaN at end → filled using last valid value
'''