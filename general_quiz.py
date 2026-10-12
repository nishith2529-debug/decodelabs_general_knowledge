def run_quiz():
    questions = [
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Venus", "Mars", "Jupiter", "Mercury"],
            "answer": 2,
        },
        {
            "question": "What is the capital city of France?",
            "options": ["Berlin", "Rome", "Paris", "Madrid"],
            "answer": 3,
        },
        {
            "question": "Which gas do plants absorb from the atmosphere?",
            "options": ["Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"],
            "answer": 3,
        },
        {
            "question": "Who wrote 'Hamlet'?",
            "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Leo Tolstoy"],
            "answer": 2,
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean"],
            "answer": 3,
        },
        {
            "question": "Which language is primarily spoken in Brazil?",
            "options": ["Spanish", "Portuguese", "French", "English"],
            "answer": 2,
        },
        {
            "question": "What is the chemical symbol for gold?",
            "options": ["Ag", "Au", "Gd", "Go"],
            "answer": 2,
        },
        {
            "question": "Which organ pumps blood throughout the human body?",
            "options": ["Lungs", "Liver", "Heart", "Kidney"],
            "answer": 3,
        },
        {
            "question": "Which year did the first human walk on the Moon?",
            "options": ["1965", "1969", "1972", "1959"],
            "answer": 2,
        },
        {
            "question": "What is the freezing point of water at sea level?",
            "options": ["0°C", "32°C", "100°C", "-10°C"],
            "answer": 1,
        },
    ]

    print("Welcome to the General Knowledge Quiz!")
    name = input("Enter your name: ").strip()
    if not name:
        name = "Player"

    score = 0

    for index, item in enumerate(questions, start=1):
        print(f"\nQuestion {index}: {item['question']}")

        for option_number, option in enumerate(item["options"], start=1):
            print(f"  {option_number}. {option}")

        while True:
            try:
                choice = int(input("Your answer (1-4): "))
                if 1 <= choice <= 4:
                    break
                print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number from 1 to 4.")

        if choice == item["answer"]:
            print("Correct! ✅")
            score += 1
        else:
            correct_option = item["options"][item["answer"] - 1]
            print(f"Wrong! ❌ The correct answer is: {correct_option}")

    total_questions = len(questions)
    percentage = (score / total_questions) * 100

    print("\nQuiz complete!")
    print(f"{name}, your final score is: {score}/{total_questions} ({percentage:.0f}%)")

    if percentage >= 80:
        print("Excellent! You are a true general knowledge expert.")
    elif percentage >= 60:
        print("Great job! You did very well.")
    elif percentage >= 40:
        print("Nice effort! Keep learning and try again.")
    else:
        print("Keep practicing — you'll improve with time!")


if __name__ == "__main__":
    run_quiz()
