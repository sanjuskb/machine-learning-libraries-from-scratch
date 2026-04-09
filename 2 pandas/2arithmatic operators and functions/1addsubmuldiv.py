import pandas as pd

# Create DataFrame
var1 = pd.DataFrame({
    "A": [10, 20, 30, 40],
    "B": [15, 16, 17, 18]
})

#performing arithmatic operations
var1["c"]=var1["A"]+var1["B"]
var1 #need not to use print 
#after creating a new column c ,now var 1 has column c .that means original is effected
var1["d"]=var1["A"]-var1["B"]
var1
var1["e"]=var1["A"]*var1["B"]
var1
var1["f"]=var1["A"]/var1["B"]
var1

# Create new columns using conditions
var1["Python"] = var1["A"] <= 20 #returns boolean values
var1["python_1"] = var1["B"] >= 16

# Display DataFrame
print(var1)

#to remain original unaffected
'''
If you DON’T want to change the original DataFrame
✅ Option 1: Create a copy (BEST PRACTICE)
var2 = var1.copy()
var2["c"] = var2["A"] + var2["B"]


Now:

var1 → unchanged

var2 → modified
'''

