# list comprehentions

jack  = {'name': 'jack',
        'car': 'bmw'}

john = {'name': 'john',
        }

oleg = {'name': 'oleg',
        'car': 'volvo'}

users = ['jack', 'john', 'oleg']

# var1
users_s = [x for x in users if x.startswith('o')]
print(users_s)

# var2
users_s_new = []

for x in users:
    if x.startswith('j'):
        users_s_new.append(x)

print(users_s_new)
