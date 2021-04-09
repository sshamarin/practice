def sort(name):
    for i in range(0, len(name) - 2):
        print(str(name[i]) + ', ', end = '')
    print(str(name[-2]) + ' ', end = '')
    print('and' + ' ' + str(name[-1]))

spam = []

while True:
    i1 = input('add new element to your list or type quit to exit: ')
    if i1 == 'quit':
        break
    elif i1 == '':
        continue
    else:
        spam.append(i1)
try:
    sort(spam)
except IndexError:
    print('error. your list is empty')
