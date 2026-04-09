import pandas as pd

d = {
    "a": [1, 2, 3, 4, 5],
    "s": [1, 2, 3, 4, 5],
    "d": [1, 2, 3, 4, 5],
    1:   [1, 2, 3, 4, 5]
}
#size of elements should be same in all keys else we get error
#here a,s,d,1 are column names

var1 = pd.DataFrame(d)

print(type(var1))
print(var1) #index values will be numbers from 0 to 4

var1 = pd.DataFrame(
    d,
    columns=["a", 1],
    index=["a", "s", "d", "f", "g"]
) #here we are only printing the column and a ,1 and changes there indices

print()
print(var1)

#we can also use lists and series to create dataframes



# Creating DataFrame from list
list_1 = [
    [1, 2, 3, 4, 5],
    [11, 12, 13, 14, 15]
]

var2 = pd.DataFrame(list_1) #when lists are used they are printed horizontally

print(type(var2))
print(var2)


# Creating DataFrame from dictionary of series

sr = {
    "s": pd.Series([1, 2, 3, 4]),
    "r": pd.Series([1, 2, 3, 4])
}

var3 = pd.DataFrame(sr)

print(type(var3))
print(var3)

'''
Why your list prints horizontally
list_1 = [
    [1, 2, 3, 4, 5],
    [11, 12, 13, 14, 15]
]

df = pd.DataFrame(list_1)
print(df)

Pandas logic (rule):

Each inner list = one ROW

So Pandas reads it as:

	0	1	2	3	4
0	1	2	3	4	5
1	11	12	13	14	15

👉 That’s why values appear horizontally.

How to print elements vertically (3 correct ways)
✅ Method 1: Use a list of single-element lists (BEST for beginners)
list_1 = [[1], [2], [3], [4], [5]]
df = pd.DataFrame(list_1)
print(df)


Output:

   0
0  1
1  2
2  3
3  4
4  5


📌 Each inner list = one row → one column → vertical

✅ Method 2: Use transpose() (smart trick)
list_1 = [[1, 2, 3, 4, 5]]
df = pd.DataFrame(list_1).T
print(df)


.T = transpose → rows ↔ columns

✅ Method 3: Convert list to Series (most natural)
list_1 = [1, 2, 3, 4, 5]
s = pd.Series(list_1)
print(s)


Output:

0    1
1    2
2    3
3    4
4    5


📌 Series is naturally vertical

Why dict / dict of Series prints vertically
pd.DataFrame({"a": [1, 2, 3, 4, 5]})


Rule:

Dictionary keys → columns

So Pandas builds columns first, not rows.

Core rule (VERY IMPORTANT — remember this)
Input type	                 Pandas treats it as
List of lists	                Rows
Dict of lists	                Columns
Dict of Series	                Columns (aligned by index)
Series	Single                  column
'''