# def collatz(number):
#         if number % 2 == 0:
#             number = number // 2
#             print(number)
#             return number
#         elif number % 2 == 1:
#             number = 3 * number + 1
#             print(number)
#             return number


def collatz(number):
    if number % 2 == 0:
        number = number // 2
        print(number)
    elif number % 2 == 1:
        number = 3 * number + 1
        print(number)
    return number

print('Welcome to the Collatz Sequence')
print('Choose a number')
number = int(input())
print('You chose: ' + str(number))
print('...')
print('...')
print('...')
print('...')
print('Beginning Sequence...')
while number != 1:
    number = collatz(number)
print('Sequence Complete!')
print('Shutting Down...')