print("--- Password Strength Checker ---")

password = input("Enter your password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False
special_characters = "!@#$%^&*"

for char in password:
     if char.isupper():
        has_upper = True
    if char.islower():
        has_lower = True
    if char.isdigit():
        has_digit = True
    if char in special_characters:
        has_special = True
missing = []

if len(password) < 8:
    missing.append("at least 8 characters")
if not has_upper:
    missing.append("uppercase letter")
if not has_lower:
    missing.append("lowercase letter")
if not has_digit:
    missing.append("digit")
if not has_special:
    missing.append("special character (!@#$%^&*)")

print("\nPassword:", password)
if len(missing) == 0:
       print("Result  : Strong Password")
else:
    print("Result  : Weak Password")
    print("Missing :", ", ".join(missing))