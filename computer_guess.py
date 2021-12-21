import random
# this code can make the computer guess a secret number in your mind between 1 - 100
# by Chukwuma A. igboanusi


def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # it could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), or too low (L) or correct (C)??').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Yay the computer guessed your number, {guess}, correctly!')


computer_guess(100)