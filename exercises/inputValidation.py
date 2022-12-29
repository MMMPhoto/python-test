print('How many cats do you own?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That is a lot of cats!')
    elif int(numCats) >= 0:
        print('That is not that many cats.')
    elif int(numCats) < 0:
        print('You must enter a postive number.')
except ValueError:
    print('You did not enter an integer.')
