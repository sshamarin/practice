bdays = {'Anna': '20.06.2014', 'Alexandra': '13.06.2009',\
        'Alevtina': '04.02.1986'}

while True:
    name = input('Enter a name (blank to quit): ')
    if name == '':
        break

    if name in bdays:
        print('birthday of ' + name + ' is ' + bdays[name])
    else:
        print('I haven\'t got ' + name + ' in my database')
        date = input('please type his(her) birthday: ')
        bdays[name] = date
        print('database successfully updated')

print(bdays)
