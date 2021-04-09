names = dict(name = 'bob', phone = '1234', email='bob@gmail.com')
print(names)

surname = names.setdefault('surname', 'bobyev')
print(surname)
print(names)
print

for key,value in names.items():
    print(key, value)

new = {'name': 'kv', 'phone': 9876}
names.update(new)
print(names)
print()
