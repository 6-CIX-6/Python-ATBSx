import sys

def collatz(number):
    if number % 2 == 0:
        number = number // 2
        print(number)
    elif number % 2 == 1:
        number = 3 * number + 1
        print(number)
    return number

print('Welcome to the Collatz Sequence')
tryAgain = 'y'
while tryAgain == 'y':
    print('Choose a number')
    try:
        number = input()
        number = int(number)
        print('You chose: ' + str(number))
        print('...')
        print('...')
        print('...')
        print('...')
        print('Beginning Sequence...')
        while number != 1:
            number = collatz(number)
        print('Sequence Complete!')
    except ValueError:
        print(number + ' is not a number, fool!')
    print('Try again? (y or n)')
    tryAgain = input()
    if tryAgain == 'n':
        break
    elif tryAgain != ('y' or 'n'):
        print('You seem to have a problem following basic instructions.')
        print("I don't have time for this")
        sys.exit()
print('Shutting Down...')