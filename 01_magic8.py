import random

# def get_answer(number):
#     if number == 0:
#         return 'not today'
#     elif number == 1:
#         return 'yes'
#     elif number == 2:
#         return 'no'
#     else:
#         return 'maybe'
#
# number = random.randint(0,3)
# fortune = get_answer(number)
# print(fortune)

messages = ['not today', 'yes', 'no', 'maybe']
print(random.choice(messages))
# the same, without random.choice
print(messages[random.randint\
(0, len(messages) - 1)])
