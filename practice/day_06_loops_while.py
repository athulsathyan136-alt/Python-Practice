print('='*40)
print("COUNTDOWN TIMER")
print('='*40)

n = 5
while n>0:
    print(n)
    n -=1

print('='*40)
print("CONDITION")
print('='*40)   

num =input("Who are you :")
num=num.lower()
match num:
    case 'Athul'|'athul':
        print("You are a CSE student")
    case _ :
        print("You are not Athul")    
