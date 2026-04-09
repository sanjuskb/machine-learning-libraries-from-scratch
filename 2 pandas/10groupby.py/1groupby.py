import pandas as pd

var = pd.DataFrame({
    "Name": ["a","b","c","d","a","b","a","b","a","c","c","d"],
    "S_1": [12,13,14,12,13,14,15,23,25,16,10,11],
    "S_2": [23,24,25,26,27,28,29,30,25,34,35,27]
})
print(var)
print()

# groupby
var_new = var.groupby("Name")
print(var_new) # it prints like this <pandas.core.groupby.generic.DataFrameGroupBy object at 0x0000020CAE82B620>
'''
What it REALLY means (plain English)

“This variable stores a GroupBy object, not actual data.”

It is NOT an error
It is NOT your output data
It is just Python telling you what kind of object it is

Break it into parts
1️⃣ DataFrameGroupBy object

This tells you:

The object is created by groupby()

It contains grouped data

It is lazy (no computation yet)

2️⃣ 0x0000020CAE82B620

This is:

Memory address (RAM location)

Used internally by Python

Different every time you run

Completely useless for learning 😄

Why Pandas shows this instead of a table

Because you wrote:

var_new = var.groupby("Name")
var_new


And groupby does not compute anything by itself.

It only prepares groups.
'''

# iterating over groups
for x, y in var_new:
    print(x)
    print(y)
    print()

'''
a
  Name  S_1  S_2
0    a   12   23
4    a   13   27
6    a   15   29
8    a   25   25

b
  Name  S_1  S_2
1    b   13   24
5    b   14   28
7    b   23   30

c
   Name  S_1  S_2
2     c   14   25
9     c   16   34
10    c   10   35

d
   Name  S_1  S_2
3     d   12   26
11    d   11   27


'''
'''


## Step 0: Your DataFrame (mental picture)

Your data looks like this:

```
   Name  S_1  S_2
0   a    12   23
1   b    13   24
2   c    14   25
3   d    12   26
4   a    13   27
5   b    14   28
6   a    15   29
7   b    23   30
8   a    25   25
9   c    16   34
10  c    10   35
```

---

## Step 1: Creating the groupby object

```python
var_new = var.groupby("Name")
```

### What this does:

* **No calculation**
* **No output table**
* Just tells Pandas:

> “Group all rows that have the same `Name`”

So internally Pandas creates:

* Group `"a"` → rows `[0,4,6,8]`
* Group `"b"` → rows `[1,5,7]`
* Group `"c"` → rows `[2,9,10]`
* Group `"d"` → row `[3]`

That’s why printing `var_new` shows:

```
DataFrameGroupBy object
```

---

## Step 2: Looping over the groups

```python
for x, y in var_new:
    print(x)
    print(y)
```

This is the **key idea** 🔥

### `groupby` is iterable

Each iteration gives you:

```
x → group name (key)
y → sub-DataFrame (rows of that group)
```

---

## Step 3: What prints for each iteration

### First iteration

```
x = 'a'
y = rows where Name == 'a'
```

Printed output:

```
a
   Name  S_1  S_2
0   a    12   23
4   a    13   27
6   a    15   29
8   a    25   25
```

---

### Second iteration

```
x = 'b'
y = rows where Name == 'b'
```

Printed output:

```
b
   Name  S_1  S_2
1   b    13   24
5   b    14   28
7   b    23   30
```

---

### And so on for `c` and `d`

---

## One-line takeaway 🔥

> **`groupby()` creates groups, and iterating over it gives (group_name, group_dataframe)**

Y


'''
print(var_new.get_group("a"))

'''
  Name  S_1  S_2
0    a   12   23
4    a   13   27
6    a   15   29
8    a   25   25
'''
print(var_new.max())
print()
'''
Name
a      25   29
b      23   30
c      16   35
d      12   27

'''
print(var_new.min())
'''
      S_1  S_2
Name
a      12   23
b      13   24
c      10   25
d      11   26
'''
print()
print(var_new.mean())
print()
'''
            S_1        S_2
Name
a     16.250000  26.000000
b     16.666667  27.333333
c     13.333333  31.333333
d     11.500000  26.500000
'''
li=list(var_new)#converting the data into list
print(li)