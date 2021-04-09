a = 'FIVE TEN TRAILCROSS MID PRO'
a_s = a.split(' ')
a_1 = a_s[0:2]
a_1 = (' '.join(a_1)).title()
a_2 = (a_s[2:])
a_2 = (' '.join(a_2)).lower()
print(a_1, a_2)
