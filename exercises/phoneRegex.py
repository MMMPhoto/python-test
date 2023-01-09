import re

phoneNumRegex = re.compile(r'(\(?\d\d\d\)?)?(-|\.)?(\d\d\d)(-|\.)?(\d\d\d\d)')


def searchForPhoneNumber():
    matchObject = phoneNumRegex.search(input('Enter a phone number: '))
    if matchObject != None:
        print(f'Phone number found: {matchObject.group()}')
    else:
        print('No phone number found')
    searchForPhoneNumber()

searchForPhoneNumber()
