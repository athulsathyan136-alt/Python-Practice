print('='*40)
print('LAMBDA FUNCTION')
print('='*40)

def sum(a,b):
    return a + b
sum_total = lambda a,b: a + b
print(f"Sum: {sum(2,5)}")
print(f"Sum: {sum_total(3,6)}")

print('='*40)
print('MAP FUNCTION')
print('='*40)

numbers = [1,2,3,4,5]
num = list(map(lambda x: x**2 ,numbers))
print(numbers)
print(num)

print('='*40)
print('FILTER')
print('='*40)

num2 = [1,2,3,4,5,6,7,8,9,10]
num3 = list(filter(lambda x: x%2==0 , num2))
print(f"List 1: {num2}")
print(f"List 2: {num3}")

