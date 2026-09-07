print('='*40)
print('*ARGS')
print('='*40)

def sum_all(*args):
    total = 0
    for i in args:
        total+=i
    return total
print(f"Sum of all: {sum_all(1,2,3)}")
print(f"Sum of all: {sum_all(1,2,3,5)}")
print(f"Sum of all: {sum_all(10,25,36)}")

print('='*40)
print('*ARGS WITH OTHER PARAMETER')
print('='*40)

def greet(greetig,*names):
    for name in names:
        print(f"{greetig} {name}!")

greet('Hello',"Athul","Swetha")
greet('Good night','Amal','Hari',"indhu")


print('='*40)
print('*KWARGS')
print('='*40)

def user(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
user(name='Athul',age=23,job='AI Engineer')
user(email='athulsathyan@emil',phone= 996547852,Gender= 'M/F')        
