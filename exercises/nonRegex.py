# Non regex phone number test function
def isPhoneNumber(text):
    if len(text) != 12:
        # print('not right length')
        return False # not correct length of phone number
    for i in range(0, 3):
        if not text[i].isdecimal():
            # print('not number')
            return False # no area code in first three digits
    if text[3] != '-' and text[3] != '.':
        # print('no dash or dot')
        return False # missing dash or dot
    for i in range(4, 7):
        if not text[i].isdecimal():
            # print('not number')
            return False # no area code in next three digits
    if text[7] != '-' and text[7] != '.':
        # print('no dash or dot')
        return False # missing dash or dot
    for i in range(8, 12):
        if not text[i].isdecimal():
            # print('not number')
            return False # no area code in last four digits
    return True

phoneNumberTest = "On many websites the contact information is buried at least five links deep, because the company doesnt really want to hear from you. And when you find it, its a form or an e-mail address. We take the exact opposite approach. We put our phone number its 80-927-7671, in case youd like to call at the top of every single page of our website, because we actually want to talk to our customers. And we staff our call center 247"

foundNumber = False
# Loop through to text to look for phone number
for i in range(len(phoneNumberTest)):
    if phoneNumberTest[i].isdecimal():
        chunk = phoneNumberTest[i:i+12]
        if isPhoneNumber(chunk):
            foundNumber = True
            print(f'Found phone number: {chunk}')
if not foundNumber:
    print('No phone numbers found')


# print(isPhoneNumber("On many websites the contact information is buried at least five links deep, because the company doesnt really want to hear from you. And when you find it, its a form or an e-mail address. We take the exact opposite approach. We put our phone number its 800-927-7671, in case youd like to call at the top of every single page of our website, because we actually want to talk to our customers. And we staff our call center 247"))



    
