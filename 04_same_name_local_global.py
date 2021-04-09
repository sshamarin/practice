def spam():
    global eggs
    eggs = 'spam' # this is the global

def bacon():
    eggs = 'bacon' # this is a local, cause we made assignment statement

def ham():
    print(eggs) # this is the global, cause we don't made assignment statement

eggs = 42 # this is the global
spam()
print(eggs)
print()
