# 1000 : 15 = mass : x
# x = 15 * mass / 1000

for_meal = {'salt': 10,
    'pepper': 8,
    'garlik': 20,
    'onion': 33
}

def species(name, total_weight):
    weight = for_meal.setdefault(name, 0) * total_weight / 1000
    return weight

for name in for_meal.keys():
    print(name + ' ' + str(species(name, total_weight=2000)))

print('cinnamon' + ' ' + str(species('cinnamon', 2000)))
print()
print(for_meal)

#
# ingridients = {
#     'salt': 20,
#     'pepper': 10,
#     'garlik': 50
# }
#
# def ingr_weight(ingr_mass, meat_mass):
#     return ingridients[ingr_mass] * meat_mass / 1000
#
# print(ingr_weight('garlik', 800))
