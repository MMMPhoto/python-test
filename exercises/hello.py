# This program says hello and asks for my name

print('Hello World')

print('What is your name?') # ask for their name
myName = input()
print(f'It is good to meet you, {myName}')
print(f'The length of your name is {len(myName)}')

print('What is your age?') # ask for their age
myAge = input()
print(f'You will be {str(int(myAge) + 1)} in a year.')