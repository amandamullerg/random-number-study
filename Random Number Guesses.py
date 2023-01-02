# Random Number Guesses
import random # Imports the random module to use the random.randint()
r_number = random.randint(1,20) # the random number generated is stored

print('I am thinking of a number between 1 and 20')

# Ask the player to guess 6 times
for guesses in range(1,7):
    print('Take a guess, you have 6 chances')
    guess = int(input()) # the FOR loop will loop acording to the set range (6 times) as long as it doesn't reach the break

    if guess < r_number:
        print('Your guess is too low.')
    elif guess > r_number:
        print('Your guess is too high') # check if the guess is higher or lower and prints a hint
    else:
        break # This condition is the correct guess, if the guess is not higher nor lower then it is the correct guess!

if guess == r_number:
    print('Good job! You guessed my number in ' + str(guesses) + ' guesses!')

else:
    print('Nope, the number I was thinking of was ' + str(r_number))