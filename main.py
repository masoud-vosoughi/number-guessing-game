import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

secret_number = random.randint(1, 100)

print("""Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)""")

user_level_choice = input("Enter your choice: ")

if user_level_choice in ("1", "2", "3"):
    attempts = 0
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

    while max_attempts > attempts:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        user_guess = input("Enter your guess: ")
        user_guess = int(user_guess)
        if user_guess == secret_number:
            print(
                f"Congratulations! You guessed the correct number in {attempts} attempt."
            )
            break
        elif user_guess > secret_number:
            print("secret num is smaller")
        else:
            print("secret num is bigger")
        if remaining_attempts == 0:
            print("you lost")

else:
    print("your choice is not valid")
