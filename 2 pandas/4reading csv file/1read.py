import pandas as pd
csv1=pd.read_csv("C:\\Users\\sanju\\OneDrive\\Desktop\\ml libraries\\pandas\\Test_new1.csv")
print(csv1)
print()

csv2=pd.read_csv("C:\\Users\\sanju\\OneDrive\\Desktop\\ml libraries\\pandas\\Test_new1.csv",nrows=2)#reading only first two rows
print(csv2)

csv3=pd.read_csv("C:\\Users\\sanju\\OneDrive\\Desktop\\ml libraries\\pandas\\Test_new1.csv",usecols=["a"])#reading only column with name a
print()
print(csv3)

csv4=pd.read_csv("C:\\Users\\sanju\\OneDrive\\Desktop\\ml libraries\\pandas\\Test_new1.csv",usecols=[1,2])#passing indices of columns .the colums with these indices will be printed
print()
print(csv4)
csv5=pd.read_csv("C:\\Users\\sanju\\OneDrive\\Desktop\\ml libraries\\pandas\\Test_new1.csv",skiprows=[1,3])#skips those rows
print(csv5)#after skipping those rows ,at 1st row the 2nd row will be come and now its index will be 1
print()


#to make any one of the column in the csv as index of rows 

csv6=pd.read_csv("C:\\Users\\sanju\\OneDrive\\Desktop\\ml libraries\\pandas\\Test_new1.csv",index_col='a')
print(csv6)