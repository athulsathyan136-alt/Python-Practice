print("="*40)
print("REVERSE STRING")
print("="*40)

text = input("Enter a word: ")
text1 = text[::-1]
print("Orginal ",text )
print("reversed ",text1)

print("\n" + "=" * 40)
print("3. PALINDROME CHECKER")
print("=" * 40)

word = input("Enter a word: ")
clean_word = word.replace(" ", "").lower()
if clean_word == clean_word[::-1]:
    print(f"'{word}' is a Palindrome! ✅")
else:
    print(f"'{word}' is NOT a Palindrome ❌")