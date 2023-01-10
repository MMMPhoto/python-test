import re

phoneNumRegex = re.compile(r'(\(?(\d{3})?\)?(?:-|\.| )?(\d{3}(?:-|\.| )?\d{4}))')

def searchForPhoneNumber():
    matchObject = phoneNumRegex.findall(input('Enter a phone number: '))
    print(matchObject)
    searchForPhoneNumber()
 
searchForPhoneNumber()
