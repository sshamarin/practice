family = ['anna_2014', 'alexandra_2009', 'alevtina_1986', 'Sergey_1977']
#print(family)

# list --> string, then lower
family_string = (' '.join(family)).title()
#print(family_string)

# string --> list, then sort
family_sorted = sorted(family_string.split(' '))
print(family_sorted)

def by_year(name):
    year = name.split('_')[-1]
    return year

#print(by_year(family_sorted[0]))

family_fin = sorted(family_sorted, key = by_year)
print(family_fin)
