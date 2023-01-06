import re

numberTest = "On many websites the contact information is buried at least five links deep, because the company doesnt really want to hear from you. And when you find it, its a form or an e-mail address. We take the exact opposite approach. We put our phone number its 800-927-7671, in case youd like to call at the top of every single page of our website, because we actually want to talk to our customers. And we staff our call center 247"

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matchObject = phoneNumberRegex.search(numberTest)
print(matchObject.group())