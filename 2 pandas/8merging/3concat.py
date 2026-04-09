import pandas as pd
sr1 = pd.Series([1,2,3,4])
sr2 = pd.Series([11,21,31,41])

print(pd.concat([sr1, sr2]))
'''
0     1
1     2
2     3
3     4
0    11
1    21
2    31
3    41
dtype: int64
'''


print()

d1 = pd.DataFrame({
    "A":[1,2,3,4],
    "B":[11,12,13,14]
})

d2 = pd.DataFrame({
    "A":[1,2,3,5],
    "B":[21,22,23,24]
})

print(pd.concat([d1, d2])) #by default axis =0


print()
'''
   A   B
0  1  11
1  2  12
2  3  13
3  4  14
0  1  21
1  2  22
2  3  23
3  5  24

'''
print(pd.concat([d1, d2],axis=1))

print()
'''
   A   B  A   B
0  1  11  1  21
1  2  12  2  22
2  3  13  3  23
3  4  14  5  24

'''
d1 = pd.DataFrame({
    "A":[1,2,3,4],
    "B":[11,12,13,14]
})

d2 = pd.DataFrame({
    "A":[1,2],
    "B":[21,22]
})
print(pd.concat([d1, d2],axis=1 ))#by default ,join="outer"

'''
   A   B    A     B
0  1  11  1.0  21.0
1  2  12  2.0  22.0
2  3  13  NaN   NaN
3  4  14  NaN   NaN
'''
print()
print(pd.concat([d1, d2],axis=1,join="inner" ))
print()
'''
   A   B  A   B
0  1  11  1  21
1  2  12  2  22
'''
d1 = pd.DataFrame({"A":[1,2,3,4], "B":[11,12,13,14]})
d2 = pd.DataFrame({"A":[1,2,3,4], "C":[21,22,23,24]})

print(pd.concat([d1, d2], axis=1, keys=["d1", "d2"]))
print()

'''
   A     C
0  1   NaN
1  2   NaN
2  3   NaN
3  4   NaN
0  1  21.0
1  2  22.0
2  3  23.0
3  4  24.0
'''
'''
import pandas as pd

d1 = pd.DataFrame({"A":[1,2,3,4], "B":[11,12,13,14]})
d2 = pd.DataFrame({"A":[1,2,3,4], "C":[21,22,23,24]})

pd.concat([d1, d2], axis=1, keys=["d1", "d2"])
Step 1️⃣ What axis=1 means
axis=1 → concatenate column-wise (side by side)

So instead of stacking rows, Pandas places:

d1 on the left

d2 on the right

Step 2️⃣ What keys=["d1","d2"] does (VERY IMPORTANT)
keys creates a hierarchical (multi-level) column index

It tells Pandas:

“These columns came from different sources — label them”

How Pandas builds the columns
Original columns
d1 → A, B

d2 → A, C

After concat with keys
pgsql
Copy code
Level 0 (outer):   d1        d2
Level 1 (inner):  A   B     A   C
That’s why the output looks like:

css
Copy code
   d1        d2
    A   B     A   C
0   1  11     1  21
1   2  12     2  22
2   3  13     3  23
3   4  14     4  24
This is called a MultiIndex column.

🔑 Why this is useful (real-world logic)
You use keys when:

Combining data from multiple sources

Keeping track of feature origin

Avoiding column name clashes

Creating structured datasets for analysis

Accessing data from this result (important)
python
Copy code
result = pd.concat([d1, d2], axis=1, keys=["d1", "d2"])

result["d1"]        # all columns from d1
result["d2"]["C"]   # column C from d2

'''
print()


d1 = pd.DataFrame({"D":[1,2,3,4]})
d2 = pd.DataFrame({"A":[1,2,3,4], "C":[21,22,23,24]})

print(pd.concat([d1, d2], axis=0))
'''

     D    A     C
0  1.0  NaN   NaN
1  2.0  NaN   NaN
2  3.0  NaN   NaN
3  4.0  NaN   NaN
0  NaN  1.0  21.0
1  NaN  2.0  22.0
2  NaN  3.0  23.0
3  NaN  4.0  24.0
'''


