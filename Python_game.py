import random

class Game:
    def __init__(self):
        self.player_name = input("Enter your name: ")
        print(f"⭐ Welcome! {self.player_name} ⭐. \nSelect the game you want to play or press 3 to quit.")

    def start(self):
        while True:
            print("1. Number Guessing Game 🤷")
            print("2. High Low Game 🔢")
            print("3. Quit")
            select = input("Enter your choice: ")

            if select == "1":
                game = NumberGuessingGame()
                game.play_game()  # Call the appropriate method for this game
                break
            elif select == "2":
                game = HighLowGame()
                game.start()  # Call the appropriate method for this game
                break
            elif select == "3" or select == "quit" .strip() .lower():
                print("Thank you for playing. Goodbye! 👋")
                break
            else:
                print("⚠️ Invalid choice. Please try again.")


class HighLowGame:
    def __init__(self, number_of_rounds=5):  # Initialize attributes in __init__
        """
        Initialize the High-Low game with the number of rounds.
        """
        self.number_of_rounds = number_of_rounds
        self.current_rounds = 0
        self.get_score = 0

    def generate_numbers(self):
        """
        Generate random numbers for the user and the computer.
        """
        self.user_number = random.randint(1, 100)
        self.computer_number = random.randint(1, 100)

    def get_choice(self):
        """
        Get the user's choice: higher or lower.
        """
        while True:
            user_choice = input("Do you think your number is higher or lower than the computer's number? (higher/lower): ").strip().lower()
            if user_choice in ["higher", "lower"]:
                return user_choice
            else:
                print("Invalid choice. Please enter 'higher' or 'lower'.")

    def compare_numbers(self, user_choice):
        """
        Compare the user's number with the computer's number and determine if the guess is correct.
        """
        if self.user_number > self.computer_number and user_choice == "higher":
            print(f"✅ Correct! Your number ({self.user_number}) is higher than the computer's number ({self.computer_number}).")
            self.get_score += 1
        elif self.user_number < self.computer_number and user_choice == "lower":
            print(f"✅ Correct! Your number ({self.user_number}) is lower than the computer's number ({self.computer_number}).")
            self.get_score += 1
        else:
            print(f"❌You are wrong. Your number was {self.user_number}, and the computer's number was {self.computer_number}.")

    def play_round(self):
        """
        Play a single round of the High-Low game.
        """
        self.generate_numbers()
        print(f"\nRound {self.current_rounds + 1} of {self.number_of_rounds}")
        print(f"Your number is: {self.user_number}")
        user_choice = self.get_choice()
        self.compare_numbers(user_choice)

    def start(self):
        """
        Start the High-Low game.
        """
        print("Welcome to the High-Low Game!")
        print("_" * 27)

        while self.current_rounds < self.number_of_rounds:
            self.play_round()
            self.current_rounds += 1

        print("")
        print("\nGame Over! Thanks for playing.")
        print(f"You final score is: {self.get_score} ")

        if self.get_score == self.number_of_rounds:
            print(f"🎉 Congratulations! You won the game! 🎉")
        else:
            print(f"Better luck next time! Try again to improve your score.")


class NumberGuessingGame:
    def __init__(self):
        self.random_number = random.randint(1, 100)

    def play_game(self):
        attempts = 5
        print("Welcome to the Number Guessing Game!")
        print(f"You have {attempts} attempts to guess the correct number.")

        while attempts > 0:
            try:
                player_number = int(input(f"Attempt {6 - attempts}/5: Guess the correct number (1-100): "))

                if player_number == self.random_number:
                    print("🎉 Congratulations! You guessed the correct number! 🎉")
                    break
                elif player_number < self.random_number:
                    print("Too low! Try again.")
                elif player_number > self.random_number:
                    print("Too high! Try again.")

                attempts -= 1  # Decrement attempts after each guess

                if attempts == 0:
                    print(f"Sorry, you've used all your attempts. The correct number was {self.random_number}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
game = Game()  # Create an instance of the Game class
game.start()

