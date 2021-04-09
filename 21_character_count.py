import pprint
message = 'type any phrase to count it\'s symbols, or blank to quit: '
dict = {}

for i in message:
	dict.setdefault(i, 0)
	dict[i] = dict[i] + 1

pprint.pprint(dict)

