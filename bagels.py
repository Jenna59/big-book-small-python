import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print('''Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com
I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:    That means:
    Pico         One digit is correct but in the wrong position.
    Fermi        One digit is correct and in the right position.
    Bagels       No digit is correct.
For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.'''.format(NUM_DIGITS))
    while True:
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print(' You have {} guesses to get it.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            #numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secretNum))

        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')

def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)

    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)

if __name__ == '__main__':
    main()


''' EXPLORE THE PROGRAM

    What happens if you set NUM_DIGITS to a number larger than 10?
    You get an IndexError because the list index is out of range in the getSecretNum function.
    
    What error message do you get if you delete or comment out numGuesses = 1?
    UnboundLocalError: cannot access local variable 'numGuesses' where it is not associated with a value
    
    What happens if you delete or comment out random.shuffle(numbers)?
    The numbers don't get shuffled and you get the first three numbers in the list, from index 0 to 2.
    
    What happens if you delete or comment out if guess == secretNum: on line 74 and return 'You got it!'?
    It skips printing out the return statement and goes into the for loop with the clues and then breaks out of the while loop on line 34
    
    What happens if you comment out numGuesses += 1?
    The number of guesses on line 26 doesn't get updated and numGuesses never exceeds MAX_GUESSES on line 35, so the loop keeps iterating continuously until you guess the correct number
'''
