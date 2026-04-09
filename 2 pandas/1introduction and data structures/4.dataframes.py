import pandas as pd
var1=pd.Series([1,2,3,4,5])
var=pd.DataFrame([1,2,3,4,5])
print(var1)
print(var)

#output
'''0    1
1    2
2    3
3    4
4    5
dtype: int64
   0
0  1
1  2
2  3
3  4
4  5
-----------------------------------------------------------------------------------

Your DataFrame output
   0
0  1
1  2
2  3
3  4
4  5


Let’s rewrite it as a table:

	0
0	1
1	2
2	3
3	4
4	5

🔴 This top 0 is NOT a value
🟢 It is the column name

Step 2: Compare with Series (side by side)
Series
0    1
1    2
2    3
3    4
4    5


This is logically:

index	value
0	1
1	2
2	3
3	4
4	5

🟥 NO column name exists

DataFrame
   0
0  1
1  2
2  3
3  4
4  5


This is logically:

row_index	column_0
0	1
1	2
2	3
3	4
4	5

🟩 Column exists (named 0)

Step 3: The ONE LOGIC RULE (remember this)

If column labels exist → it is a DataFrame
If only index + values → it is a Series

Your DataFrame has:

Row index → left 0,1,2,3,4

Column index → top 0

Your Series has:

Only index → 0,1,2,3,4

No column label

'''