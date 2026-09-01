print("=" * 40)
print("1. CREATING TUPLES")
print("=" * 40)


person = ("Athul", 22, "AI Engineer")
print(f"Tuple: {person}")
print(f"Name: {person[0]}")
print(f"Age: {person[1]}")
print(f"Type: {type(person)}")

print("\n" + "=" * 40)
print("2. TUPLE UNPACKING")
print("=" * 40)

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Job: {job}")

print("\n" + "=" * 40)
print("3. IMMUTABILITY (Cannot Change)")
print("=" * 40)

coordinates = (10, 20)
print(f"Coordinates: {coordinates}")
# Trying to change will cause an error
try:
    coordinates[0] = 50  # This will fail
except TypeError as e:
    print(f"Error: {e}")