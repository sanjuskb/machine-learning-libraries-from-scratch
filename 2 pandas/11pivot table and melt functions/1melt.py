import pandas as pd

var = pd.DataFrame({
    "days": [1,2,3,4,5,6],
    "eng": [10,12,14,15,16,12],
    "maths": [17,18,19,13,14,16]
})
print(var)
print()
print(pd.melt(var, id_vars=["days"])
)



'''
1️⃣ Your original DataFrame (before melt)
var = pd.DataFrame({
    "days": [1,2,3,4,5,6],
    "eng": [10,12,14,15,16,12],
    "maths": [17,18,19,13,14,16]
})


It looks like this:

   days  eng  maths
0   1     10    17
1   2     12    18
2   3     14    19
3   4     15    13
4   5     16    14
5   6     12    16


This is called wide format data.

2️⃣ The melt command used
pd.melt(var, id_vars=["days"])

3️⃣ What melt() means (in plain English)

“Unpivot the table: convert columns into rows.”

or even simpler:

“Make the DataFrame longer instead of wider.”

4️⃣ Role of id_vars=["days"]

id_vars full form is:

Identifier Variables
What that means (simple)

Columns that identify each row and should NOT be melted (changed).

In plain English

id_vars = keep these columns fixed

Other columns will be converted into rows

id_vars means:

“These columns should stay as they are (identifier columns).”

So:

days → stays fixed

eng and maths → will be converted into rows

5️⃣ What Pandas does internally

It takes:

eng   maths
10     17


and converts it into:

variable  value
eng       10
maths     17


And repeats this for each day.

6️⃣ Final output (your screenshot)
   days  variable  value
0   1     eng       10
1   2     eng       12
2   3     eng       14
3   4     eng       15
4   5     eng       16
5   6     eng       12
6   1     maths     17
7   2     maths     18
8   3     maths     19
9   4     maths     13
10  5     maths     14
11  6     maths     16

Meaning of new columns

variable → original column name (eng, maths)

value → value from that column


'''
print()
print(pd.melt(var, id_vars=["days"],value_name="gpa",var_name="python")
)

'''
    days python  gpa
0      1    eng   10
1      2    eng   12
2      3    eng   14
3      4    eng   15
4      5    eng   16
5      6    eng   12
6      1  maths   17
7      2  maths   18
8      3  maths   19
9      4  maths   13
10     5  maths   14
11     6  maths   16

'''







