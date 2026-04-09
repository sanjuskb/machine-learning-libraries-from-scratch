import pandas as pd
var1 = pd.DataFrame(
    {"A":[1,2,3,4], "B":[11,12,13,14]},
    index=["a","b","c","d"]
)

var2 = pd.DataFrame(
    {"C":[10,20], "B":[11,22]},
    index=["a","b"]
)
print(var1._append(var2))
'''
     A   B     C
a  1.0  11   NaN
b  2.0  12   NaN
c  3.0  13   NaN
d  4.0  14   NaN
a  NaN  11  10.0
b  NaN  22  20.0

'''

print(var1._append(var2,ignore_index=True))
'''
     A   B     C
0  1.0  11   NaN
1  2.0  12   NaN
2  3.0  13   NaN
3  4.0  14   NaN
4  NaN  11  10.0
5  NaN  22  20.0

index is came in ordered manner

'''

'''


Why do we have BOTH merge() and join()?

Because they solve two different real-world problems.

🔹 join() — Index-based combination
Think:

“Attach columns to an existing table using index alignment”

Core idea

Works on index by default

Fast and simple

Cleaner syntax when index already has meaning

Example use cases

Time-series data (dates as index)

Feature engineering

Adding derived columns

Appending lookup tables indexed by ID

Example
df.join(features_df)

🔹 merge() — Relational / SQL-style join
Think:

“Match rows using keys (columns)”

Core idea

Works on columns

Very flexible

Similar to SQL JOIN

Example use cases

Customer ID matching

Foreign keys

Database-style joins

Datasets from different sources

Example
pd.merge(orders, customers, on="customer_id")

Side-by-side comparison (IMPORTANT)
Feature	join()	merge()
Default key	Index	Column(s)
Syntax	Short & clean	Explicit
Speed	Slightly faster	Slightly slower
Use case	Feature add	Data relationship
SQL-like	❌	✅
Multiple keys	❌	✅
Column overlap handling	Suffix required	Suffix optional

'''