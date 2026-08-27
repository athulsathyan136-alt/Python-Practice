print('='*40)
print("MULTIPLICATION TABLE")
print('='*40)

num=int(input("Enter a number: "))
print(f"Multiplication table of {num}")

for i in range(1,11):
    print(f"{num} x {i} =", (num*i))