#! /usr/bin/env python3
import re, pyperclip

# Create a regex for phone numbers
phoneNumRegex = re.compile(r'''
    \(?   (?:\d{3})?   \)?  # optional area code with or without parentheses
    (?:-|\.| )?             # optional dash, period, or space
    \d{3}                   # first 3 numbers of main phone number
    (?:-|\.| )              # dash, period, or space
    \d{4}                   # last 4 numbers of main number
''', re.VERBOSE)

# Create a regex for emails
emailRegex = re.compile(r'''
    [^\s@]+     # name in email - no spaces or at signs (group this)
    @           # @ sign
    [^\s@]+     # name of domain - no spaces or at signs (group this)
''', re.VERBOSE)


# matchObject = emailRegex.findall('max.mcdonough@gmail.com, john@josh.co.uk, Jesus456@google.us')
# print(matchObject)

# Get text off of clipboard
text = pyperclip.paste()

# Extract the email/phone from this text
allPhoneNumbers = phoneNumRegex.findall(text)
allEmailAddresses = emailRegex.findall(text)

print(allPhoneNumbers)
print(allEmailAddresses)

# Copy the extracted email/phone to the clipboard
joinPhoneNumbers = '\n'.join(allPhoneNumbers)
joinEmailAddresses = '\n'.join(allEmailAddresses)
results = f'{joinPhoneNumbers}\n{joinEmailAddresses}'
pyperclip.copy(results)