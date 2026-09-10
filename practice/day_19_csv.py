import csv
import os

print('='*40)
print('WRITE DATA TO A CSV FILE')
print('='*40)
students = [
    ["Name", "Marks", "Subject"],  #
    ["Athul", 95, "AI"],
    ["Riya", 88, "ML"],
    ["John", 76, "Cloud"],
    ["Sam", 82, "DevOps"]
]

with open('students.csv','w',newline = '') as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("File 'students.csv' created sucessfully")

print('='*40)
print('READ DATA FROM CSV FILE')
print('='*40)

with open('students.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print('='*40)
print('READ AS DICTIONARIES')
print('='*40)        

with open('students.csv','r') as file:
    reader = csv.DictReader(file)
    print('Student Records: ')
    for row in reader:
        print(f"{row['Name']}  scored {row['Marks']} in {row['Subject']}")


print('='*40)
print('ADD A NEW STUDENT')
print('='*40)

newname = input('Enter student name: ')
newmark = int(input('Enter marks: '))
newsubject = input('Enter subject: ')

with open('students.csv','a') as file:
    writer = csv.writer(file)
    writer.writerow([newname,newmark,newsubject])

print(f"\n{newname} added successfully!")

print('='*40)
print('UPDATED STUDENT LIST')
print('='*40)

if os.path.exists("students.csv"):
    with open('students.csv','r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"{row['Name']} scored {row['Marks']} in {row['Subject']}")
else:
    print("student.csv not found")