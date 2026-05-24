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
        