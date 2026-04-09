import pandas as pd
csv1=pd.read_csv("C:\\Users\\sanju\\OneDrive\\Desktop\\ml libraries\\pandas\\Test_new123.csv")
'''
     a    b     c
0  NaN  NaN  11.0
1  NaN  2.0   2.0
2  3.0  5.0   3.0
3  4.0  6.0   4.0
4  NaN  NaN  55.0
5  6.0  6.0   NaN

'''
print(csv1)
print()
print(csv1.fillna("python")) #fills the all null values with python
print()
print(csv1.fillna({'a':"python"}))#replaces all the null values in column a with python
print()
print(csv1.fillna({'a':'python','b':'cpp','c':'java'}))#replaces all the null values in column a with python,column b with cpp,column c with java
print()
print(csv1.fillna(method="ffill"))#replaces all the null values with its previous row data
print()
print(csv1.fillna(method="bfill"))#replaces all the null values with its next row data
print()
print(csv1.fillna(method="ffill",axis=1))#replaces all the null values with its previous column data
print()
print(csv1.fillna(method="bfill",axis=1))#replaces all the null values with its next column data
print()
print(csv1.fillna(26,limit=1))#fill only the first value(by default axis=0) that means vertical.column wise
print()
print(csv1.fillna(26,limit=1,axis=1))#fill only first value of row elements
print()
csv1.fillna(27,inplace=True)#changes the original dataframe
print(csv1)