from numpy import random 

# Enter lower and upper number
lower_bound = int(input("Input lower bound: "))
upper_bound = int(input("Input upper bound: "))

random_number = random.randint(lower_bound, upper_bound)

allowedChances = 7
guessCounter = 0

while guessCounter < allowedChances:
    guessCounter += 1
    guess = int(input("Enter your guess: "))

    if guess == random_number:
        print(f"You have guessed correctly in {guessCounter} chances")
        break
    
    elif guessCounter >= allowedChances and guess != random_number:
        print(f"You have run out of guesses, the number is {random_number}")
    
    elif guess < random_number:
        print("Too low try again")
    
    elif guess > random_number:
        print("Too high, try again")
   



"""
Algorithm
1. Accept lower and upper bounds from the user.
2. Generate a random number in the selected range.
3. Calculate the maximum allowed guesses using the binary search formula.
4. Run a loop to take user guesses:
   a. If the guess is too high, print: "Try Again! You guessed too high."
   b. If the guess is too low, print: "Try Again! You guessed too small."
   c. If the guess is correct, print: "Congratulations!" and exit the loop.
   d. If the user runs out of chances, display the correct number and a 
      message: "Better Luck Next Time!"
"""