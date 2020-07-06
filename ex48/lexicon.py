words = {'direction': ('north', 'south', 'east', 'west',
					'down', 'up', 'left', 'right', 'back',
					'foward'),
		'verb': ('go', 'stop', 'kill', 'eat', 'run', 'open'),
		'stop': ('the', 'in', 'of', 'from', 'at', 'it', 'to'),
		'noun': ('door', 'bear', 'princess', 'cabinet', 'i')}


def scan(symbols):
	global words
	# word division
	smallSymbols = symbols.lower()
	word = smallSymbols.split()
	# definition of word types
	i = 0
	sentence = []
	for i in word:
		appended = 0
		for type in words:
			# check number
			if i.isdecimal():
				# creating tuples with the number and number's type
				sentence.append(('number', int(i)))
				appended = 1
				break
			elif i in words[type]:
				# creating tuples with a word type and a word
				sentence.append((type, i))
				appended = 1
				break
		#append the error type
		if appended == 0:
			sentence.append(('error', i))
	# return of the offer in the form of a list
	# with lists with previously created tuples
	return sentence
