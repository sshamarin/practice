nfl_team = []
print('lets create list of nfl teams!')
while True:
    name = input('type the name of team ' + str(len(nfl_team) + 1) + ' or press enter to quit: ')

    if name == '':
        break
    nfl_team = nfl_team + [name]

print('the list is:')
for name in nfl_team:
    print(name)
