import random


def select_difficulty():
    print("""Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)""")

    while True:
        user_level_choice = input("Enter your choice: ")

        if user_level_choice not in ("1", "2", "3"):
            print("Invalid choice! Please select 1, 2, or 3.")
            continue
        break

    if user_level_choice == "1":
        difficulty_name = "Easy"
        max_attempts = 10

    elif user_level_choice == "2":
        difficulty_name = "Medium"
        max_attempts = 5

    else:
        difficulty_name = "Hard"
        max_attempts = 3

    print(f"You selected {difficulty_name}")
    print(f"You have {max_attempts} chances to guess the number.")

    return difficulty_name, max_attempts


def play_game(secret_number, max_attempts):
    attempts = 0

    while max_attempts > attempts:
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if user_guess < 1 or user_guess > 100:
            print("Invalid guess! Enter a number between 1 and 100.")
        else:
            attempts += 1
            remaining_attempts = max_attempts - attempts

            if user_guess == secret_number:
                print(
                    "Congratulations! You guessed the correct number! "
                    f"Total guesses: {attempts}."
                )
                break
            elif user_guess > secret_number:
                print("The secret number is smaller.")
            else:
                print("The secret number is bigger.")

            if remaining_attempts == 0:
                print("Game over! You've run out of chances.")
                print(f"The correct number was {secret_number}.")


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

secret_number = random.randint(1, 100)

difficulty_name, max_attempts = select_difficulty()

play_game(secret_number, max_attempts)
