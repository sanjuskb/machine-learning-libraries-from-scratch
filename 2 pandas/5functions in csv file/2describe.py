import pandas as pd
csv1=pd.read_csv("C:\\Users\\sanju\\OneDrive\\Desktop\\ml libraries\\pandas\\Test_new12.csv")
print(csv1.describe())

'''
You will get output like:

              a         b         c
count  6.000000  6.000000  6.000000
mean   3.500000  3.500000  3.500000
std    1.870829  1.870829  1.870829
min    1.000000  1.000000  1.000000
25%    2.250000  2.250000  2.250000
50%    3.500000  3.500000  3.500000
75%    4.750000  4.750000  4.750000
max    6.000000  6.000000  6.000000


Now let’s decode each row 👇

1️⃣ count
count = 6


➡️ Number of non-missing values
Each column has 6 numbers → count = 6

2️⃣ mean (average)

Values in column a:

1 + 2 + 3 + 4 + 5 + 6 = 21
21 / 6 = 3.5


So:

mean = 3.5


Same for b and c.

3️⃣ std (standard deviation)

This measures how spread out the values are.

For [1,2,3,4,5,6]:

std ≈ 1.8708


(You don’t need to calculate this manually now — just know it shows variation.)

4️⃣ min
min = 1


➡️ Smallest value in the column.

5️⃣ 25% (first quartile, Q1)
25% = 2.25


➡️ 25% of the data lies below this value.

6️⃣ 50% (median)
50% = 3.5


➡️ Middle value of the dataset.

7️⃣ 75% (third quartile, Q3)
75% = 4.75


➡️ 75% of the data lies below this value.

8️⃣ max
max = 6


➡️ Largest value in the column.
'''
