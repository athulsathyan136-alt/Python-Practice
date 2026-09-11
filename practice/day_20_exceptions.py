# Day 20: Exception Handling (try / except)
print("=" * 40)
print("1. BASIC TRY / EXCEPT")
print("=" * 40)

try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print(f"100 / {num} = {result}")
except ValueError:
    print("❌ Error: That's not a valid number!")
except ZeroDivisionError:
    print("❌ Error: Cannot divide by zero!")

print("\n" + "=" * 40)
print("2. TRY / EXCEPT / ELSE / FINALLY")
print("=" * 40)

try:
    num = int(input("Enter a number: "))
    result = 100 / num
except ZeroDivisionError:
    print("❌ Cannot divide by zero!")
except ValueError:
    print("❌ Please enter a valid number!")
else:
    print(f"✅ Success! Result = {result}")
finally:
    print("🏁 This always runs (cleanup code)")

print("\n" + "=" * 40)
print("3. CATCHING ALL ERRORS")
print("=" * 40)

try:
    numbers = [1, 2, 3]
    print(numbers[10])  # Index out of range
except Exception as e:
    print(f"❌ Something went wrong: {e}")

print("\n" + "=" * 40)
print("4. BULLETPROOF CALCULATOR")
print("=" * 40)

def safe_divide(a, b):
    """Divide two numbers safely"""
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero"
    except TypeError:
        return "Error: Invalid input type"

print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")
print(f"10 / 'a' = {safe_divide(10, 'a')}")

print("\n" + "=" * 40)
print("5. FILE NOT FOUND HANDLING")
print("=" * 40)

try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("❌ File not found. Creating a new one...")
    with open("nonexistent.txt", "w") as file:
        file.write("Created by exception handler!")
    print("✅ File created successfully.")