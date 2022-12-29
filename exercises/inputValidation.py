print('How many cats do you own?')
numCats = input()
try:
    if int(numCats) <= 0:
        raise Exception('No numbers below zero.')
    elif int(numCats) >= 4:
        print('That is a lot of cats!')
    else:
        print('That is not that many cats.')
except ValueError:
    print('You did not enter an integer.')
