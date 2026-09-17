import pandas as pd

print('='*50)
print('CREATING A DATAFRAME')
print('='*50)

data = {
    "Name": ["Athul", "Riya", "John", "Sam", "Priya"],
    "Marks": [95, 88, 76, 82, 91],
    "Subject": ["AI", "ML", "Cloud", "DevOps", "Data Science"],
    "City": ["Chengannur", "Delhi", "Mumbai", "Bangalore", "Chennai"]
}
df = pd.DataFrame(data)
print(df)

print('='*50)
print('BASIC INSPECTION')
print('='*50)

print(f"shape: {df.shape}")
print(f"Columns: {list(df.columns)}")
print(f"Data Types: {df.dtypes}")
print(f"\nFirst 3 rows: {df.head(3)}")
print(f"\n Statistics: {df.describe()}")

print('='*50)
print('SELECTING DATA')
print('='*50)

print('Names column')
print(df['Name'])

print('\nName and Marks')
print(df[["Name","Marks"]])

print(f"\n Row 0: {df.iloc[0].to_dict()}")
print(f"\n Row 1: {df.iloc[1].to_dict()}")


print('='*50)
print('FILTERING DATA')
print('='*50)

high = df[df["Marks"]> 85]
print('Students with marks > 85:')
print(high) 

ai = df[df['Subject']== 'AI']
print('\n AI students')
print(ai)

print('='*50)
print('SORTING')
print('='*50)

sorted_df = df.sort_values("Marks" ,ascending=False)
print("Sorted by marks")
print(sorted_df)

print('='*50)
print('ADDING NEW COLUMN')
print('='*50)

df['Grades'] = df["Marks"].apply(lambda m:"A" if m>=90 else "B"if m<=80 else "c")
print(df)


print('='*50)
print('GROUPING AND AGGREGATION')
print('='*50)

print(f'Average Marks: {df["Marks"].mean():.2f}')
print(f"Highest Marks: {df["Marks"].max()}")
print(f"Lowest Marks: {df["Marks"].min()}")
print(f"Total Students: {len(df)}")
