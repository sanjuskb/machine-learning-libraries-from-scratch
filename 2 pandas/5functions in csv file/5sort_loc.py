import pandas as pd
csv1=pd.read_csv("C:\\Users\\sanju\\OneDrive\\Desktop\\ml libraries\\pandas\\Test_new12.csv")
print(csv1.sort_index(axis=0,ascending=False)) #here we are sorting index of rows which are vertical so axis =0 and printing the data in reverse that is descending orders
print()

#to change the any value in the data
csv1.loc[0,"a"]=5#changing the value of a at 0 row to 5
print(csv1)
print()
csv1.loc[[2,3],["a","c"]] #getting the values of a and c at index of row 2 and 3
print(csv1)
print()
csv1.loc[:,["a","c"]] #getting all  the values of a and c 
print(csv1)
print()
csv1.loc[[2,3],:] #getting all the data of all columns at index of row 2 and 3
print(csv1)
print()
csv1.iloc[2,2]#getting the data at index 2 of row and index 2 of fcolumn
print(csv1)
print()
csv2=csv1.drop("a",axis=1)#removes the a column from the data
print(csv2)
print()
csv2=csv1.drop(0,axis=0) #removes the 0th row from the data
print(csv2)