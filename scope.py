eggs = 34

def spam():
    global eggs
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam()
print(eggs)