languages = {
	'Python': 'Guido van Rossum',
	'Ruby': 'Yukihiro Matsumoto',
	'PHP': 'Rasmus Lerdorf',
	}
keys = languages.keys()
for key in keys:
	print(key + " was created by {}".format(languages[key]))
