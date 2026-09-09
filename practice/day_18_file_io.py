print('='*40)
print('WRITE TO A FILE')
print('='*40)

with open('notes.txt','w') as file:
    file.write('Hello, this is my first file\n')
    file.write('Pyhton is awesome \n')
    file.write('Day 18: file \n')

print("File 'note.txt' created and written sucessfully!")

print('='*40)
print('READ A FILE')
print('='*40)

with open('notes.txt','r') as file:
    content = file.read()
    print('File content:')
    print(content)

print('='*40)
print('READ LINE BY LINE')
print('='*40)    

with open('notes.txt','r') as file:
    print('read line by line')
    for line in file:
        print(f"{line.strip()}")

print('='*40)
print('WRITE USER INPUT TO FILE')
print('='*40)        

user = input('Enter some text')
with open('notes.txt','w') as file:
    file.write(user)

print('Your text has been saved')

with open('notes.txt','r') as file:
    print(f"You write : {file.read()}")