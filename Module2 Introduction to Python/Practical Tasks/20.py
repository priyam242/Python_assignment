# 20.Mini project :
# Problem Statement : Password Generator
# Make a program to generate a strong password using the input given by the user. To generate a password, randomly take some words from the user input and then include numbers, special characters and capital letters to generate the password. Also, keep a check that password length is more than 8 characters. Note: Include Exception handling wherever required. Also, make a ‘User’ class and store the details like user id, name and password of each user as a tuple.

import random

class User:
    def __init__(self, user_id, name, password):
        self.user_id = user_id
        self.name = name
        self.password = password
    
    def display(self):
        print(f"User ID: {self.user_id}")
        print(f"Name: {self.name}")
        print(f"Password: {self.password}")

def generate_password(user_input):
    # Take some words from user input
    words = user_input.split()
    password_parts = []
    
    # Add 2-3 words from the input
    for i in range(min(2, len(words))):
        word = random.choice(words)
        # Randomly capitalize
        if random.choice([True, False]):
            word = word.upper()
        else:
            word = word.lower()
        password_parts.append(word)
    
    # Add a number
    password_parts.append(str(random.randint(0, 9)))
    
    # Add a special character
    special_chars = "!@#$%&*"
    password_parts.append(random.choice(special_chars))
    
    # Shuffle all parts
    random.shuffle(password_parts)
    
    # Combine into a password
    password = "".join(password_parts)
    
    # Make sure it's at least 8 characters
    while len(password) < 8:
        password = password+str(random.randint(0, 9))
    
    return password

# Main program
try:
    print("--- Password Generator ---")
    user_id = input("Enter your ID: ")
    name = input("Enter your name: ")
    
    # Get some words from user to create password
    user_words = input("Enter some words (separated by spaces): ")
    
    # Generate password
    password = generate_password(user_words)
    print(f"Your generated password is: {password}")
    
    # Create user object
    user = User(user_id, name, password)
    
    print("\n--- User Details ---")
    user.display()

except Exception as e:
    print(f"Something went wrong: {e}")