import pandas as pd


var1 = pd.DataFrame(
    {"A":[1,2,3,4], "B":[11,12,13,14]}
)

var2 = pd.DataFrame(
    {"C":[10,20,30,40], "D":[11,22,33,44]}
)

print(var1.join(var2))
print()
'''
   A   B   C   D
0  1  11  10  11
1  2  12  20  22
2  3  13  30  33
3  4  14  40  44
'''

var1 = pd.DataFrame(
    {"A":[1,2,3,4], "B":[11,12,13,14]}
)

var2 = pd.DataFrame(
    {"C":[10,20], "D":[11,22]}
)
print(var1.join(var2))
'''
   A   B     C     D
0  1  11  10.0  11.0
1  2  12  20.0  22.0
2  3  13   NaN   NaN
3  4  14   NaN   NaN

Because NaN exists in columns C and D, Pandas automatically converts the column type to float.

Now the full logic (step-by-step)
Your data
var1 index → 0,1,2,3
var2 index → 0,1


After join():

Index  C     D
0      10    11
1      20    22
2      NaN   NaN
3      NaN   NaN

🔑 The core rule (VERY IMPORTANT)

NaN is a floating-point concept in NumPy

Integers cannot represent NaN

Floats can represent NaN

So Pandas does this internally:

int + NaN  → float

Why Pandas changes 10 → 10.0

When Pandas sees this:

[10, 20, NaN, NaN]


It says:

“I must use a data type that can store NaN”

✔ int ❌ cannot
✔ float ✅ can

So the entire column becomes float

This is NOT a bug ❌

It’s automatic type upcasting ✅

'''
print()
var1 = pd.DataFrame(
    {"A":[1,2,3,4], "B":[11,12,13,14]},
    index=["a","b","c","d"]
)

var2 = pd.DataFrame(
    {"C":[10,20], "D":[11,22]}
)


print(var1.join(var2))
'''
   A   B   C   D
a  1  11 NaN NaN
b  2  12 NaN NaN
c  3  13 NaN NaN
d  4  14 NaN NaN

Why NaNs appear?

var1 index → ["a","b","c","d"]

var2 index → [0,1]

❌ Indexes DO NOT MATCH

So Pandas says:

“I don’t know which row in var2 belongs to index a, b, c, d”

Result:

C  D → NaN NaN


✔ Pandas does index-based left join
✔ No index match → NaN


'''

print()
var1 = pd.DataFrame(
    {"A":[1,2,3,4], "B":[11,12,13,14]},
    index=["a","b","c","d"]
)

var2 = pd.DataFrame(
    {"C":[10,20], "D":[11,22]},index=["a","b"]
)

print(var1.join(var2))

'''
   A   B     C     D
a  1  11  10.0  11.0
b  2  12  20.0  22.0
c  3  13   NaN   NaN
d  4  14   NaN   NaN

'''
print()
print(var2.join(var1))
'''
    C   D  A   B
a  10  11  1  11
b  20  22  2  12

'''
print()


print(var2.join(var1,how="right"))# in this line var  1 is on right side so printing is done according to var1
'''
     C     D  A   B
a  10.0  11.0  1  11
b  20.0  22.0  2  12
c   NaN   NaN  3  13
d   NaN   NaN  4  14
'''
print()
print(var2.join(var1,how="outer"))#same as above
'''
Given DataFrames (assumed from context)
var1 = pd.DataFrame(
    {"A":[1,2,3,4], "B":[11,12,13,14]}
)

var2 = pd.DataFrame(
    {"C":[10,20], "D":[11,22]}
)


Indexes:

var1.index → 0,1,2,3

var2.index → 0,1

1️⃣ how="right"
print(var2.join(var1, how="right"))

Meaning:

Keep ALL indexes from the RIGHT DataFrame (var1)

Right DF → var1

Index taken → 0,1,2,3

Result logic:

Rows 0,1 → match in both

Rows 2,3 → missing in var2 → NaN

So output index is based on var1 only.

2️⃣ how="outer"
print(var2.join(var1, how="outer"))

Meaning:

Keep ALL indexes from BOTH DataFrames (union of indexes)

Indexes:

var2 → 0,1

var1 → 0,1,2,3

Union = 0,1,2,3

So again output index is:

0,1,2,3

❗ Why they look the same here

Because:

var2.index ⊆ var1.index


So:

Right join (keep var1)

Outer join (keep both)

➡️ Both end up with the same index set

'''
print()
print(var2.join(var1,how="inner"))
#it means Keep common indexes from BOTH DataFrames (intersection of indexes)

print()
var1 = pd.DataFrame(
    {"A":[1,2,3,4], "B":[11,12,13,14]},
    index=["a","b","c","d"]
)

var2 = pd.DataFrame(
    {"C":[10,20], "B":[11,22]},index=["a","b"]
)

print(var1.join(var2,how="outer",lsuffix="_1",rsuffix="_2" ))
'''
   A  B_1     C   B_2
a  1   11  10.0  11.0
b  2   12  20.0  22.0
c  3   13   NaN   NaN
d  4   14   NaN   NaN
'''

print()
