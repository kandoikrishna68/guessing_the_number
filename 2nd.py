import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    attempts = 0

    while True:
        # Get user input for a guess
        user_guess = int(input("Guess the number (between 1 and 100): "))
        
        # Increment the number of attempts
        attempts += 1

        # Check if the guess is correct
        if user_guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts.")
            break
        elif user_guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

if __name__ == "__main__":
    guess_the_number()
