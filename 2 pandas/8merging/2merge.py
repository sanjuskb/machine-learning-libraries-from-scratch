import pandas as pd

var1 = pd.DataFrame({
    "A": [1, 2, 3, 4],
    "B": [11, 12, 13, 14]
})

var2 = pd.DataFrame({
    "A": [1, 2, 3, 5],
    "C": [21, 22, 23, 24]
})

#A is different in both dataframes
'''
output:
   A   B   C
0  1  11  21
1  2  12  22
2  3  13  23

A is printed only upto common values,and b,c printed according to the A
'''

print(pd.merge(var1, var2, on="A"))#order A,B,C
print()
print(pd.merge(var2, var1, on="A")) #order A,C,B.here by default, how is inner
print()
print("left")
print(pd.merge(var2, var1,how="left"))  #prints according to left which is var 2
'''
left
   A   C     B
0  1  21  11.0
1  2  22  12.0
2  3  23  13.0
3  5  24   NaN
'''
print()
print("right")
print(pd.merge(var2, var1,how="right")) #prints according to right which is var 1
'''
right
   A     C   B
0  1  21.0  11
1  2  22.0  12
2  3  23.0  13
3  4   NaN  14

'''

print()
print("outer")
print(pd.merge(var2, var1,how="outer")) #prints according to both
'''
outer
   A     C     B
0  1  21.0  11.0
1  2  22.0  12.0
2  3  23.0  13.0
3  4   NaN  14.0
4  5  24.0   NaN

'''
print()
print(pd.merge(var2, var1,how="outer",indicator=True)) 
print()
'''
   A     C     B      _merge
0  1  21.0  11.0        both
1  2  22.0  12.0        both
2  3  23.0  13.0        both
3  4   NaN  14.0  right_only
4  5  24.0   NaN   left_only
'''
print(pd.merge(var2, var1,left_index=True,right_index=True)) 

'''
prints both dataframes
   A_x   C  A_y   B
0    1  21    1  11
1    2  22    2  12
2    3  23    3  13
3    5  24    4  14
'''
print()
print(pd.merge(var2, var1,left_index=True,right_index=True,suffixes=["sanju","good"])) 

'''
suffixes are applied ONLY to column names that are COMMON in both DataFrames

   Asanju   B  Agood   C
0       1  11      1  21
1       2  12      2  22
2       3  13      3  23
3       4  14      5  24
'''


