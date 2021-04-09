bdays = {'Anna': '20.06.2014', 'Alexandra': '13.06.2009',\
        'Alevtina': '04.02.1986'}

for i in bdays.values():
    print(i)
print()

for i in bdays.keys():
    print(i)
print()

for i in bdays.items():
    print(i)
print()

for i,ii in bdays.items():
    print('key is ' + i + ', value is ' + ii)
print()

sbwins = {'steelers': 6, 'pats': 6}

for i,ii in sbwins.items():
    print(str(i) + ' wins sb ' + str(ii) + ' times')
print()

print(sbwins['steelers'])

print('steelers' + ' win sb ' + str(sbwins.get('steelers', 0)) + ' times')
print('browns' + ' win sb ' + str(sbwins.get('browns', 0)) + ' times')
print()

sbwins['pats'] = 0
print(sbwins.items())
