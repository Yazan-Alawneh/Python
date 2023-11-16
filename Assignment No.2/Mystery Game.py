import random
# old function doesn't provide you with last letter on last attempt
# def create_space(word):
#    chars = len(word)
#    if chars > 3:
#        return word[0] + ' _ ' + word[2] +' ' + ' '.join(['_' for _ in range(3, chars)])
#    else:
#        return word[0] + ' ' + ' '.join(['_' for _ in range(1, chars)])


def create_space(word, attempt):
    chars = len(word)
    space = ''
    for i in range(chars):
        if i == 0 or (attempt == 1 and i == chars - 1) or (i == 2 and chars > 3):
            space += word[i]
        else:
            space += '_'
        if i < chars - 1:
            space += ' '
    return space

def game():
    list1 = ['key', 'dawn', 'red', 'higher', 'rocket', 'seek', 'summer', 'doom', 'edge', 'vend']
    list2 = ['sea', 'bone', 'bed', 'fire', 'socket', 'peak', 'hummer', 'room', 'ledge', 'bend']
    x = random.choice(list1)
    x_pos = list1.index(x)
    hint = list2[x_pos]

    attempt = 3
    while attempt > 0:
        chars = create_space(x, attempt)
        print('\n\n                  YOUR WORD IS:')
        print('                  ', chars)
        print('Attempts left:', attempt)

        if attempt == 2:
            while True:
                help = input('Would you like me to give you a hint?  [yes/no]\n')
                if help.lower() == 'yes':
                    print('                  ', chars)
                    print('     [Hint] THE WORD SOUNDS LIKE:', hint)
                    print('Attempts left:', attempt)
                    break
                elif help.lower() == 'no':
                    print('                  ', chars)
                    print('Attempts left:', attempt)
                    break
                else:
                    print("Please answer with 'yes' or 'no'")

        guess = input('Enter your guess:  ')
        if guess == x:
            print('Congratulations!! you guessed the word in', 4 - attempt, 'attempts')
            break
        attempt -= 1

    if attempt == 0:
        print('You Lost, the word was:', x)


game()

restart = input("\nDo you want to play again? [yes/no] ")
if restart.lower() == 'yes':
    game()