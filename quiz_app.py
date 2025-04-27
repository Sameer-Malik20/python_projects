def quiz_app():
    questions = {
        "What is the capital of France?": "Paris",
        "What is 2 + 2?": "4",
        "What is the largest planet in our solar system?": "Jupiter",
        "Who wrote 'Romeo and Juliet'?": "Shakespeare",
        "What is the chemical symbol for gold?": "Au"
    }

    score = 0

    for question, answer in questions.items():
        user_answer = input(question + " ")
        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {answer}.")

    print(f"Your final score is {score}/{len(questions)}.")
    if score == len(questions):
        print("Congratulations! You got all answers correct!")
    elif score >= len(questions) // 2:
        print("Good job! You passed the quiz.")
    else:
        print("Better luck next time!")

while True:
    print("1. Start Quiz")
    print("2. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        quiz_app()
    elif choice == '2':
        print("Exiting the quiz app.")
        break
    else:
        print("Invalid choice! Please try again.")

