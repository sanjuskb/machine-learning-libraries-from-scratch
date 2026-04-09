import pandas as pd

#using dictionaries
d={"name":["python","cpp","c","java"],"rank":[1,2,4,3],"diff":[1,4,2,3]}
print(pd.Series(d)) #here we get data type as object because it contains mix of strings,numbers
print(type(d))

print()
a=pd.Series(12)
print(a)#single data can also be given
print(type(a))
print()

#if we want to print a single data value for multiple times

a=pd.Series(12,index=[1,2,3,4,5,6])
print(a)
print()
a=pd.Series(12,index=[1,2,3,4,5,6])
b=pd.Series(12,index=[1,2,3,4])

print(a+b) #in case of numpy if we wanted to add two arrays it shows broadcasting error but here there will be no error and it will add upto given values and remaining are considered as nan
