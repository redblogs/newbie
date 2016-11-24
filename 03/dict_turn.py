res_dict = {'!': 1, '.': 1, 'Bob': 1, 'I': 2, 'a': 1, 'am': 2, 'boy': 1}

new = {}

for k ,v in res_dict.items():
	if v not in new.keys():
		new[v] = [k]
	else :
		new[v].append(k)


print new
