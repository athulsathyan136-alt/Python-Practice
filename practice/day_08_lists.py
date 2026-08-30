print('='*40)
print('CREATING A LIST')
print('='*40)

x = ['Apple','Banana','Mango','Grapes']
print(f"initial list: {x}")
print(f'First fruit: {x[0]}')
print(f'Last fruit: {x[3]}')

print('='*40)
print('ADDING ITEMS')
print('='*40)

x.append('Orange')
print(f"After append: {x}")
print()
x.insert(1,"Strawberry")
print(f"After inser: {x}")

print('='*40)
print('LOOPING THROUGH A LIST')
print('='*40)

x = ['Apple','Banana','Mango','Grapes']
for i in x:
    print(i)