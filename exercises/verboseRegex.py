import re

phoneNumRegex = re.compile(r'''
    (                       # group entire number
    \(?   (\d{3})?   \)?    # optional area code with or without parentheses (and group area code)
    (?:-|\.| )?             # optional dash, period, or space
    (    \d{3}              # first 3 numbers of main phone number (start group of main 7 digits)
    (?:-|\.| )?             # optional dash, period, or space
    \d{4})                  # last 4 numbers of main number
    )                       # close group
''', re.VERBOSE)

def searchForPhoneNumber():
    matchObject = phoneNumRegex.findall(input('Enter a phone number: '))
    print(matchObject)

    searchForPhoneNumber()

searchForPhoneNumber()

