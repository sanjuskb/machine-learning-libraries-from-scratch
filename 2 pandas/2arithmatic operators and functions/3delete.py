import pandas as pd

# Create DataFrame
var = pd.DataFrame({
    "A": [1, 2, 3, 4, 5],
    "B": [9, 8, 7, 6, 5],
    "c": [2, 4, 5, 3, 6]
})

# Display DataFrame
print(var)
print()
var1=var.pop("c")
print(var1)#prints deleted column
print()
print(var)#prints dataframe after deletion of column
print()

#also we can use
del var['A']
print(var)
