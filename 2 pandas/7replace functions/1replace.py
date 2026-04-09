import pandas as pd
csv1=pd.read_csv("C:\\Users\\sanju\\OneDrive\\Desktop\\ml libraries\\pandas\\Test_new12.csv")
print(csv1)
'''
a,b,c
1,1,11
2,2,22
3,5,33
4,6,44
5,5,55
6,6,66
'''
print()
print(csv1.replace(to_replace=2,value=27)) #replacing 2 with 27
print()
print(csv1.replace([1,2,3,4,5,6],26))
print()
csv1.replace("[A-Za-z]", "python", regex=True)#it replaces all the alphabets with word python
csv1.replace({'a':"[a-z]"},27,regex=True)#replacing the letters of coumn a with 27

print(csv1.replace(6,method="ffill")) #replacing 6 with its previous data
print()
print(csv1.replace(1,method="bfill")) #replacing one with its next data
print()
print(csv1.replace(1,method="bfill",limit=2)) #replacing only first  two ones with its next data (by default axis will be 0 so column wise it will check and replaces first  two occurances of one)

csv1.replace(1,method="bfill",limit=2,inplace=True) #changes the original dataframe
'''

What is regex? (simple definition)

Regex = Regular Expression

A regex is a pattern used to find, match, or replace text.

Think of it as:

a search rule, not an exact word

a way to say:
👉 “match anything that looks like this”

Why regex exists (real reason)

Normal search:

Find: "apple"


→ matches only apple

Regex search:

Find: any word with only letters


→ matches apple, cat, DOG, python, ML

So regex is used when:

data is messy

you don’t know exact values

you want patterns, not exact text
csv1.replace("[A-Za-z]", "python", regex=True)
What this means (plain English)
Replace every alphabet letter (A–Z or a–z)
with the word "python"

🔍 Let’s break the regex part
[A-Za-z]
This is a regular expression pattern:

A-Z → all capital letters

a-z → all small letters

[ ] → “any one character from this set”

So:


[A-Za-z] = any alphabet character
regex=True
Tells Pandas:

“Treat the first argument as a pattern, not a literal value”

Without regex=True, Pandas would look for the exact string [A-Za-z].

🧠 What happens to text columns
Example value:


"ALPHAGEO"
Replacement process:


A → python
L → python
P → python
H → python
A → python
G → python
E → python
O → python
Result:


pythonpythonpythonpythonpythonpythonpythonpython
That’s why the output looks repeated.

⚠️ Important behavior to remember
replace() works cell by cell

With regex, it works character by character

That’s why each letter is replaced individually
'''