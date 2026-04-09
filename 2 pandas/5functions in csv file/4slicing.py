import pandas as pd
csv1=pd.read_csv("C:\\Users\\sanju\\OneDrive\\Desktop\\ml libraries\\pandas\\Test_new12.csv")
print(csv1[:3]) #gives rows upto index 2
print()
print(csv1[3:6]) #gives data from row 3 to 5
print()
print(csv1.index.array)#we get an array of all the index
print()
print(csv1.to_numpy()) #creates a 2d array of all data and it doesnot include index and column names
print()
#also we can create numpy array like 
import numpy as np
print(np.asarray(csv1)) #same as above