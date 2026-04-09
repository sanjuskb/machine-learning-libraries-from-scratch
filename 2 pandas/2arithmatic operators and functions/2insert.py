import pandas as pd

# Create DataFrame
var = pd.DataFrame({
    "A": [1, 2, 3, 4, 5],
    "B": [9, 8, 7, 6, 5]
})

# Display DataFrame
var

# Insert a new column at position 1
var.insert(1, "python", var["A"])#inserting a new column named python and giving the values what are present in A column


# Display updated DataFrame
var
var.insert(2, "python1", [2,6,2,7,5])
print(var)
print()

#if we want to create a column upto certain values of A

var['python12']=var['A'][:3]
print(var)

