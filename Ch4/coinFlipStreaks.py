import random
numberOfStreaks = 0
# streak = False
# x = 0
# y = 6
for experimentNumber in range(10000):

    # Code that creates a list of 100 'heads' or 'tails' values.
    coinFlip = []
    tempFlip = ''
    # random.choice(['H','T'])
    for i in range(100):
        tempFlip = random.choice(['H','T'])
        coinFlip.append(str(tempFlip))
    # print(coinFlip)

    # Code that checks if there is a streak of 6 heads or tails in a row.
    x = 0
    for x in range(100):
        if coinFlip[x:x+6] == ['T', 'T', 'T', 'T', 'T', 'T']:
            numberOfStreaks += 1
            break
        elif coinFlip[x:x + 6] == ['H', 'H', 'H', 'H', 'H', 'H']:
            numberOfStreaks += 1
            break
        else:
            x += 1


# Example:  ['T', 'T', 'T', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'T', 'T']
# print(coinFlip)

print(len(coinFlip))
print(numberOfStreaks)
print('Chance of streak: %s%%' % (numberOfStreaks / 100))