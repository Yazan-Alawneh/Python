import random


def play_game():
    low_num = input('Enter the starting number:\n')
    high_num = input('Enter the maximum number:\n')
    x = random.randint(int(low_num), int(high_num))
    print('chosen number =', x)
    print('Guess the number between', low_num, 'and', high_num)
    attempt = 1
    while True:
        guess = int(input())
        if guess > x:
            print('Too high! Try again.')
            attempt += 1
        elif guess < x:
            print('Too low! Try again.')
            attempt += 1
        else:
            print('You got it!   took you', attempt,'attempts')
            break


play_game()
while input("Do you want to play again? (yes/no):\n").lower() == 'yes':
    play_game()