print('='*40)
print("SQUARE NUMBERS")
print('='*40)

x = [1,2,3,4,5]
print('Original: ',x)
square = [x**2 for x in range(1,6)]
print('Square: ',square)
print()
print()
print('='*40)
print("EVEN OR ODD NUMBERS")
print('='*40)

x = [1,2,3,4,5,7,8,9,10]
even = [x for x in range(10) if x%2==0 ]
print('Original:',x)
print('Even number:',even)