import random

print("=" * 45)
print("      WELCOME TO NUMBER GUESSING GAME")
print("=" * 45)

while True:
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\nI have selected a number between 1 and 100.")
    print("Can you guess it?")

    while True:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            if guess < secret_number:
                print("Too Low! Try Again.")

            elif guess > secret_number:
                print("Too High! Try Again.")

            else:
                print("\n🎉 Congratulations!")
                print(f"You guessed the number {secret_number} correctly.")
                print(f"Attempts Taken: {attempts}")
                break

        except ValueError:
            print("Invalid input! Please enter a number.")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nThank you for playing!")
        break