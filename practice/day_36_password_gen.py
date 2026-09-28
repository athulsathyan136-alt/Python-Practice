import secrets
import string

def generate_password(length=16,use_symbol = True,use_numer = True):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits if use_numer else ''
    symbol = "!@#$%^&*()_+-=[]{}|;:,.<>" if use_symbol else ''

    all_chars = lowercase + uppercase + digits + symbol

    password = [secrets.choice(lowercase),
                secrets.choice(uppercase)]

    if use_numer:
        password.append(secrets.choice(digits))
    if use_symbol:
        password.append(secrets.choice(symbol))

    remaining = length - len(password)
    password += [secrets.choice(all_chars) for _ in range(remaining)]

    secrets.SystemRandom().shuffle(password)
    return ''.join(password) 

def check_stength(password):
    score = 0
    feedback = []
    if len(password) >= 12 :
        score+=1
    if len(password) >= 16 :
        score+=1
    if any(c.islower() for c in password):
        score+=1
    if any(c.isupper() for c in password):
            score+=1
    if any(c.isdigit() for c in password):
            score+=1
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
         score+=1
         
    levels = {
        0: "🔴 Very Weak",
        1: "🟠 Weak",
        2: "🟠 Weak",
        3: "🟡 Fair",
        4: "🟢 Strong",
        5: "🟢 Very Strong",
        6: "💎 Extremely Strong" }

    return levels.get(score,"unknown"),score                        

def main():
    print("=" * 50)
    print("🔐 SECURE PASSWORD GENERATOR")
    print("=" * 50)

    while True:
         print('\nOptions: ')
         print('1.Generate a password')
         print('2.Generate multiple password')
         print('3.Quit')

         choice = input('\n Enter your choice (1-3)').strip()

         if choice == '1':
              length = int(input('Password length (default 16): ')or 16)
              password = generate_password(length)
              strength ,score = check_stength(password)
              print(f'\n🔑Your password {password}')
              print(f' Strength : {strength}')
         elif choice == '2':
              count = int(input('How many password: '))     
              length = int(input('Password length (default 16): ')or 16)
              print(f'\n🔑Generated {count} password')
              for i in range(1, count+1):
                   pwd = generate_password(length)
                   strength ,_ = check_stength(pwd)
                   print(f"    {i}. {pwd} [{strength}]")

         elif choice == '3':
              print('\n Stay secure')
              break
         else:
              print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()