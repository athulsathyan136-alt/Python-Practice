print('='*40)
print('CREATING SETS')
print('='*40)

sets = {'graphes','apple','mango','banana'}
print('Set:',sets)
print(f'Type:{type(sets)}')

lists = [1,2,2,3,4,4,5]
print(f'Original list: {lists}')
unique = set(lists)
print(f'Set (unique): {unique}')

print('='*40)
print('SET OPERATIONS')
print('='*40)

num1 = {1,2,3,4,5}
num2 = {4,5,6,7,8}
print(f'Set A: {num1}')
print(f'Set B: {num2}')

print('Union (A U B): ',num1|num2)
print(f'Intersection (A ∩ B): {num1&num2}')
print(f'Difference (A - B): {num1-num2}')
print(f'Difference (B - A): {num2-num1}')