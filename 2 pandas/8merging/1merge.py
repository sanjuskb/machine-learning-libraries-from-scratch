import pandas as pd

var1 = pd.DataFrame({
    "A": [1, 2, 3, 4],
    "B": [11, 12, 13, 14]
})

var2 = pd.DataFrame({
    "A": [1, 2, 3, 4],
    "C": [21, 22, 23, 24]
})

print(pd.merge(var1, var2, on="A"))#order A,B,C,it is not required to write (on A)
print()
print(pd.merge(var2, var1, on="A")) #order A,C,B
'''
What merge() does (one-line definition)

merge() combines two DataFrames based on a common column

Step-by-step explanation
🔹 var1
A	B
1	11
2	12
3	13
4	14
🔹 var2
A	C
1	21
2	22
3	23
4	24
🔹 on="A"

This tells Pandas:

“Join both tables where column A values match”

Final output
A	B	C
1	11	21
2	12	22
3	13	23
4	14	24

✔ Column A is used once
✔ Data from both tables is combined row-wise

Important thing you should notice

This is an INNER JOIN by default.

Meaning:

Only rows where A exists in both DataFrames are kept

'''