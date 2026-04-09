import pandas as pd
csv1=pd.read_csv("C:\\Users\\sanju\\OneDrive\\Desktop\\ml libraries\\pandas\\Test_new1.csv")
print(csv1.index)#RangeIndex(start=0, stop=6, step=1)
print(csv1.columns) # prints all column names
print(csv1.describe())
'''
Your describe() output
        a  s  d
count   6  6  6
unique  6  6  6
top     1  1  1
freq    1  1  1


Let’s decode each line 👇

1️⃣ count
count   6  6  6


➡️ Number of non-missing values in each column
All columns have 6 values, so count = 6

2️⃣ unique
unique  6  6  6


➡️ Number of distinct (different) values

Example (column a):

1, i, 3, 4, 5, 6 → all different → 6 unique


Same for s and d

3️⃣ top
top     1  1  1


➡️ The most frequently occurring value (mode)

In your columns:

Every value appears only once

Pandas picks the first occurring value

So:

top = 1

4️⃣ freq
freq    1  1  1


➡️ Frequency of the top value

1 appears once, so frequency = 1

🧠 Why you didn’t see mean, min, max, etc.

Because:

Columns are object (string) type

Pandas cannot do math on strings

So instead of:

mean, std, min, max


You get:

unique, top, freq
'''