import pandas as pd
csv1=pd.read_csv("C:\\Users\\sanju\\OneDrive\\Desktop\\ml libraries\\pandas\\Test_new12.csv")
print(csv1.head())#gives the top 5 rows data
print()
print(csv1.head(2))#gives the rows data upto index 1 (that is upto 2 rows)
print()
print(csv1.tail())#gives the rows data upto index 4 from bottom (that is upto 5 rows)
print()
print(csv1.tail(3))#gives the rows data upto index 2 from bottom (that is upto 3 rows)
