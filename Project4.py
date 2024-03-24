import random
import string

def generate_password(length):
   
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''
    for i in range(length):
        password += random.choice(characters)
    return password

num_passwords = int(input("How many passwords would you like to generate? "))
password_length = int(input("Enter the length for each password: "))

print("\nGenerating Passwords:")
for i in range(num_passwords):
    password = generate_password(password_length)
    print(f"Password {i+1}: {password}")