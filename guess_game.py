def guess_the_number():
    import random

    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Welcome to the Guess the Number Game!")
    print(f"I'm thinking of a number between 1 and 100. You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    if attempts == max_attempts:
        print(f"Sorry! You've used all your attempts. The number was {number_to_guess}.")

while True:
    print("1. Play Guess the Number")
    print("2. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        guess_the_number()
    elif choice == '2':
        print("Exiting the game.")
        break
    else:
        print("Invalid choice! Please try again.")