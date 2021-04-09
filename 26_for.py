# case: get list with names and years
# and sort it by years

family = ['anna_2014', 'alexandra_2009', 'alevtina_1986', 'Sergey_1977']

family_s = ' '.join(family).lower()
print(family_s)

family_l = sorted(family_s.split(' '), reverse=True)
print(family_l)

# family_names = []
#
# for i in family_l:
#     name = i.split('_')[0].title()
#
#     if name.startswith('S'):
#         continue
#
#     family_names.append(name)
#
# print(sorted(family_names))
