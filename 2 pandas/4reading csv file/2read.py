import pandas as pd
csv1=pd.read_csv("C:\\Users\\sanju\\OneDrive\\Desktop\\ml libraries\\pandas\\Test_new1.csv",header=2) #changing the column names (that is header) as row of index 2
print(csv1)
print()

csv1=pd.read_csv("C:\\Users\\sanju\\OneDrive\\Desktop\\ml libraries\\pandas\\Test_new1.csv",names=['col1','col2','col3']) #adding a new column names at the top
print(csv1)
print()
csv1=pd.read_csv("C:\\Users\\sanju\\OneDrive\\Desktop\\ml libraries\\pandas\\Test_new1.csv",header=None).add_prefix("col") #replacing header with col0,col1,col2...
print(csv1)
print()

'''csv1=pd.read_csv("C:\\Users\\sanju\\OneDrive\\Desktop\\ml libraries\\pandas\\Test_new1.csv",dtype={"s":"float"}) #changing the datatype of column s to float
print(csv1)
print()


❌ What the error is saying (plain English)
ValueError: could not convert string to float: 'l'


This means:

👉 You told Pandas:

dtype={"s": "float"}


👉 But column s contains at least one value that is NOT a number
Specifically, it found a string 'l', which cannot be converted to float.

So Pandas stopped and raised an error.

Why this happens

Your CSV column s probably looks like one of these:

s
1
2
3
l   ← problem
5


or mixed data:

1, 2, 3, l, 5


⚠️ dtype conversion in read_csv() is STRICT
If even one value is invalid, it fails

'''
