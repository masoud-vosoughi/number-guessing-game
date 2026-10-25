# 🎯 Number Guessing Game

A simple command-line number guessing game built with Python.

The computer randomly selects a number between 1 and 100, and the player must guess the correct number within a limited number of attempts.

After each incorrect guess, the game provides feedback to help the player find the secret number.

This project is based on the [Number Guessing Game challenge from roadmap.sh](https://roadmap.sh/projects/number-guessing-game).

## ✨ Features

- **Random Number Generation:** Generates a secret number between 1 and 100.
- **Three Difficulty Levels:**
  - Easy — 10 attempts
  - Medium — 5 attempts
  - Hard — 3 attempts
- **Interactive CLI:** Players interact with the game through the terminal.
- **Guess Feedback:** Indicates whether the secret number is higher or lower than the player's guess.
- **Input Validation:** Handles invalid difficulty selections, non-integer inputs, and guesses outside the allowed range.
- **Attempt Tracking:** Counts valid guesses without penalizing invalid inputs.
- **Win/Loss Detection:** Displays a congratulatory message when the player wins or reveals the secret number when attempts run out.

## 🛠️ Tech Stack

- **Python 3.12** — Main programming language
- **Python Standard Library** — Random number generation
- **Ruff** — Python linting and formatting
- **Pre-commit** — Automated code quality checks
- **Git** — Version control

The game does not require any third-party runtime dependencies.

## 🚀 Getting Started

### Prerequisites

Make sure Python 3.12 is installed.

Check your Python version:

```bash
python3 --version
```

### Installation

1. Open the project directory:

```bash
cd number-guessing-game
```

2. Create a virtual environment:

```bash
python3 -m venv .venv
```

3. Activate the virtual environment (macOS/Linux):

```bash
source .venv/bin/activate
```

4. Run the game:

```bash
python main.py
```

Installing development dependencies is optional and only required for development and code quality checks.

```bash
python -m pip install -r requirements-dev.txt
```

## 🎮 How to Play

1. Start the game using `python main.py`.
2. Select a difficulty level (1, 2, or 3).
3. Enter an integer between 1 and 100.
4. Use the game's feedback to adjust your next guess.
5. Guess the secret number before running out of attempts.

### Example Gameplay

```text
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)

Enter your choice: 2
You selected Medium
You have 5 chances to guess the number.

Enter your guess: 50
The secret number is smaller.

Enter your guess: 25
The secret number is bigger.

Enter your guess: 42
Congratulations! You guessed the correct number! Total guesses: 3.
```

The secret number changes each time a new game is started.

## 📁 Project Structure

```text
number-guessing-game/
├── main.py
├── README.md
├── pyproject.toml
├── requirements-dev.txt
├── .pre-commit-config.yaml
└── .gitignore
```

### File Descriptions

- `main.py` — Contains the main game logic, input validation, and CLI interaction.
- `README.md` — Project documentation and usage instructions.
- `pyproject.toml` — Ruff configuration.
- `requirements-dev.txt` — Development dependencies.
- `.pre-commit-config.yaml` — Automated Git hooks for code quality checks.
- `.gitignore` — Excludes virtual environments, cache files, and unnecessary files from version control.

## 🏗️ Code Organization

The application uses three main functions:

- `select_difficulty()` — Displays the difficulty menu, validates the player's selection, and returns the selected difficulty and maximum attempts.
- `play_game(secret_number, max_attempts)` — Handles guessing, input validation, attempt tracking, and win/loss conditions.
- `main()` — Initializes the game and coordinates its execution.

The application uses the `if __name__ == "__main__":` entry point to prevent the game from automatically starting when the module is imported.

## ✅ Code Quality

This project uses Ruff and Pre-commit to maintain consistent code quality.

Run the linter:

```bash
ruff check .
```

Check formatting:

```bash
ruff format --check .
```

Install Git hooks:

```bash
pre-commit install
```

Run all configured checks manually:

```bash
pre-commit run --all-files
```

Pre-commit hooks also run automatically before each Git commit.

## 🔮 Future Improvements

Potential future enhancements include:

- Allowing players to play multiple rounds without restarting the application.
- Adding a timer to measure completion time.
- Implementing a hint system.
- Tracking high scores for each difficulty level.

These features are not included in the current version.

## 📚 Learning Outcomes

This project provides practical experience with:

- Python variables and data types
- Conditional statements
- While loops
- Functions and return values
- Function parameters and local scope
- Exception handling with `try/except`
- Input validation
- Code refactoring
- Git and automated code quality tools

## 📄 License

No license has been assigned yet.
