print('='*40)
print('BASIC FUNCTION')
print('='*40)

def hello():
    print("Hello Athul!")
hello()
hello()

print('='*40)
print('FUNCTION WITH PARAMETERS')
print('='*40)

def fun(name):
    print(f'Hello {name}')
fun("Athul")
fun("Swetha")

print('='*40)
print('FUNCTION WITH RETURN VALUE')
print('='*40)

def re(a,b):
    return a + b
result = re(2,3)
print(f'Result: {result}')

def cal(a,b,op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    else:
        return 'Invalid operator'

print(f"5 + 3 = {cal(5,3,'+')}")
print(f"10 - 2 = {cal(10,2,'+')}")
print(f"2 * 6 = {cal(2,6,'+')}")
print(f"6 / 3 = {cal(6,3,'+')}")
    