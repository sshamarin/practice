# case: get the list with full names
# and return a list wiht single name

family = ['anna shamarina', 'alexandra shamarina', 'alevtina shamarina', 'sergey shamarin']

# list --> str, then title
family_s = (', '.join(family)).title()
print(family_s)

# str --> list, then sorted
family_l = family_s.split(', ')
family_l = sorted(family_l)
print(family_l)

family_fin = []

for i in family_l:
    name = i.split(' ')[0]
    family_fin.append(name)

print(family_fin)

# nflteams = ['ARIZONA CARDINALS', 'ATLANTA FALCONS', 'BUFFALO BILLS', 'BALTIMORE RAVENS', 'CAROLINA PANTHERS', 'CINCINNATI BENGALS', 'CLEVELAND BROWNS', 'CHICAGO BEARS', 'DALLAS COWBOYS', 'DENVER BRONCOS', 'DETROIT LIONS', 'GREEN BAY PACKERS', 'HOUSTON TEXANS', 'INDIANAPOLIS COLTS', 'KANSAS CITY CHIEFS', 'LOS ANGELES CHARGERS', 'LOS ANGELES RAMS', 'JACKSONVILLE JAGUARS',
# 'MIAMI DOLPHINS', 'MINNESOTA VIKINGS', 'NEW ENGLAND PATRIOTS', 'NEW ORLEANS SAINTS', 'NEW YORK GIANTS', 'NEW YORK JETS', 'OAKLAND RAIDERS', 'PHILADELPHIA EAGLES',
# 'SAN FRANCISCO 49ERS', 'SEATTLE SEAHAWKS', 'PITTSBURGH STEELERS', 'TAMPA BAY BUCCANEERS', 'TENNESSEE TITANS', 'WASHINGTON REDSKINS']
# print(nflteams)
#
# # list --> string
# nflteams_str = (', '.join(nflteams)).title()
# print(nflteams_str)
# # string --> list
# nflteams_list = nflteams_str.split(', ')
# print(nflteams_list)
#
# nflteams_single = []
#
# for i in nflteams_list:
#     ii = i.split(' ')[-1]
#     nflteams_single.append(ii)
#
# nflteams_fin = sorted(nflteams_single)
# print(nflteams_fin)
