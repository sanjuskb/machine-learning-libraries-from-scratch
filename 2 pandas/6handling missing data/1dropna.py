import pandas as pd
csv1=pd.read_csv("C:\\Users\\sanju\\OneDrive\\Desktop\\ml libraries\\pandas\\Test_new123.csv")
print(csv1)
'''
output:
     a    b     c
0  1.0  NaN  11.0
1  NaN  2.0  22.0
2  3.0  5.0   3.0
3  4.0  6.0  44.0
4  5.0  NaN  55.0
5  6.0  6.0   NaN

here missing values are shown as nan .to get rid of that missing values

'''
print(csv1.dropna())# it removes the enitre row containg the missing values
print()

print(csv1.dropna(axis=0)) #removes the row .same as above
print()
print(csv1.dropna(axis=1)) #removes the entire column that containing missing values
print()

#if i have missing values of an entire row and i only wanted to remove those missing values which has missing v alues in entire row then 
print(csv1.dropna(how="all"))#it only removes that row which contains all the missing values and those rows are not removed which doesnot contain all missing values
print()
print(csv1.dropna(subset="c"))#it removes  missing values that are only present in column c
print()

print(csv1.dropna(thresh=2))
'''
thresh=1 → keep row if at least 1 value is not NaN

thresh=2 → keep row if at least 2 values are not NaN

thresh=3 → keep row if at least 3 values are not NaN

Rows that don’t meet this condition are dropped
'''
print()

csv1.dropna(inplace=True)#it modifies the original dataframe by removing all null values
print(csv1)#now csv1 is changed