import random
import string

def generate_password(length, complexity):
    password = ''
    if complexity == 'low':
        characters = string.ascii_letters
    elif complexity == 'medium':
        characters = string.ascii_letters + string.digits
    elif complexity == 'high':
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        return "Invalid complexity level! Please choose from 'low', 'medium', or 'high'."

    for _ in range(length):
        password += random.choice(characters)

    return password

length = int(input("Enter the desired length of the password: "))
complexity = input("Enter the complexity level (low/medium/high): ")

print("Generated Password:", generate_password(length, complexity))
