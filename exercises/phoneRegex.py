import re

phoneNumRegex = re.compile(r'\(?(\d{3})?\)?(?:-|\.| )?(\d{3}(?:-|\.| )?\d{4})')

()
def searchForPhoneNumber():
    matchObject = phoneNumRegex.findall(input('Enter a phone number: '))
    print(matchObject)
    # if matchObject != None:
    #     print('Phone number found:')
    #     i = 0
    #     groups = len(matchObject.groups())
    #     for i in range(groups + 1):
    #         print(matchObject.group(i))
    # else:
    #     print('No phone number found')
    searchForPhoneNumber()

searchForPhoneNumber()
