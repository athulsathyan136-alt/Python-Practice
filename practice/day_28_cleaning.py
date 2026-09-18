import pandas as pd
import numpy as np

print('='*50)
print('MESSY DATA')
print('='*50)

data = {
    "Name": ["Athul", "Riya", "John", "Athul", "Sam", "Priya", None],
    "Marks": [95, 88, np.nan, 95, 82, 91, 76],
    "Subject": ["AI", "ML", "Cloud", "AI", "DevOps", None, "Data Science"],
    "City": ["Chengannur", "Delhi", "Mumbai", "Chengannur", "Bangalore", "Chennai", "Mumbai"]
}

df = pd.DataFrame(data)
print('Original Messy data: ')
print(df)

print('='*50)
print('MISSING DATA')
print('='*50)

print('Missing value per column: ')
print(df.isnull().sum())

print(f'\nToatl missing values: {df.isnull().sum().sum()}')

print('='*50)
print('DROP MISSING DATA')
print('='*50)

drop = df.dropna()
print('After dropping row with missing values:')
print(drop)
print(f'Rows: {len(df)} -> {len(drop)}')

print('='*50)
print('FILLING MISSING DATA')
print('='*50)

df_fill = df.copy()
df_fill['Marks'] = df_fill['Marks'].fillna(df_fill['Marks'].mean())
df_fill['Name'] = df_fill['Name'].fillna('Unkown')
df_fill['Subject'] = df_fill['Subject'].fillna('General')

print('After filling missing values')
print(df_fill)

print('='*50)
print('REMOVING DUPLICATES')
print('='*50)

df_clean = df_fill.drop_duplicates()
print('After removing duplicates: ')
print(df_clean)
print(f'Rows: {len(df_fill)} -> {len(df_clean)}')

print('='*50)

print(f'Final shape {df_clean.shape}')
print(f'Missing values remainig : {df_clean.isnull().sum().sum()}')
print('\nCLeaned dataset')
print(df_clean)

print('='*50)
print('SAVE CLEANED DATA')
print('='*50)

df_clean.to_csv('cleaned_students.csv',index = False)
print("✅ Saved to cleaned_students.csv")

loaded = pd.read_csv('cleaned_students.csv')
print(f'verified : {len(loaded)} rows loaded back')