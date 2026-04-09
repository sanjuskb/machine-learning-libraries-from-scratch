import pandas as pd

data = {
    "order_id": [101, 102, 103],
    "date": ["2024-01-15", "2024-02-10", "2023-12-30"]
}

df = pd.DataFrame(data)
print(df)
print()

df["date"] = pd.to_datetime(df["date"])#converting string into 
print()
df.info()
print()


# Extract Year
df["year"] = df["date"].dt.year
print()

# Extract Month

df["month"] = df["date"].dt.month
print()


# Extract Day

df["day"] = df["date"].dt.day
print(df)
print()
'''
   order_id       date  year  month  day
0       101 2024-01-15  2024      1   15
1       102 2024-02-10  2024      2   10
2       103 2023-12-30  2023     12   30
'''
print()

print(df.sort_values("date"))
'''

   order_id       date  year  month  day
2       103 2023-12-30  2023     12   30
0       101 2024-01-15  2024      1   15
1       102 2024-02-10  2024      2   10

'''