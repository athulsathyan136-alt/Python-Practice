print('='*40)
print('1. CREATING A DICTIONARY')
print('='*40)

dic = {'name': 'Athul','age': 22,'job': 'AI Engineer'}
print(f'dictionary: {dic}')
print(f'Name: {'name'}')
print(f'Age: {'age'}')

print('='*40)
print('2. ADDING & UPDATING VALUES')
print('='*40)

email = {'name': 'Athul','age': 22,'job': 'AI Engineer'}
print(f'After adding email: {email}')
dic['email'] = 'athul@email.com'
print(f'After adding email : {dic}')


print('='*40)
print('3. LOOPING THROUGH DICTIONARY')
print('='*40)

contacts = {
    'amit':'96584758',
    'john':'556252455',
    'riya':'254633255'
}

name = input('Enter name to seach:')
if name in contacts:
    print(f'{name} number: {contacts[name]}')
else:
    print()

print('ALL CONTACT')
for name,number in contacts.items():
    print(f'{name}:{number}')    
    