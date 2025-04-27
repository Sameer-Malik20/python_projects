def generate_password(length=12):
    import random
    import string

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

while True:
    print("1. Generate Password")
    print("2. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        length = int(input("Enter password length (default is 12): ") or 12)
        password = generate_password(length)
        print(f"Generated Password: {password}")
    elif choice == '2':
        break
    else:
        print("Invalid choice! Please try again.")