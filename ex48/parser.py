words = {'direction': ('north', 'south', 'east', 'west',
					'down', 'up', 'left', 'right', 'back',
					'foward'),
		'verb': ('go', 'stop', 'kill', 'eat', 'run', 'open'),
		'stop': ('the', 'in', 'of', 'from', 'at', 'it', 'to'),
		'noun': ('door', 'bear', 'princess', 'cabinet', 'i')}


class ParseError(Exception):
	pass

class SENTENCE(object):
	
	def __init__(self, subject, verb, object):
		self.subject = subject
		self.verb = verb
		self.object = object
	
def peek(word_list):
	if word_list:
		word = word_list[0]
		return word[0]
	else:
		return None

def match(word_list, expecting):
	if word_list:
		word = word_list.pop(0)
		
		if word[0] == expecting:
			return word
		else:
			return None
	else:
		return None

def skip(word_list, word_type):
	while peek(word_list) == word_type:
		match(word_list, word_type)

def parse_verb(word_list):
	skip(word_list, 'stop')
	
	if peek(word_list) == 'verb':
		return match(word_list, 'verb')
	else:
		raise ParseError("Expected a verb next.")

def parse_object(word_list):
	skip(word_list, 'stop')
	next_word = peek(word_list)
	
	if next_word == 'noun':
		return match(word_list, 'noun')
	elif next_word == 'direction':
		return match(word_list, 'direction')
	else:
		raise ParseError("Expected a noun or direction next.")

def parse_subject(word_list):
	skip(word_list, 'stop')
	next_word = peek(word_list)
	
	if next_word == 'noun':
		return match(word_list, 'noun')
	elif next_word == 'verb':
		return ('noun', 'player')
	else:
		raise ParseError("Expected a verb next.")

def return_sentence(sentence):
	try:
		subj = parse_subject(sentence)
		verb = parse_verb(sentence)
		obj = parse_object(sentence)
		
		return SENTENCE(subj[1], verb[1], obj[1])
	except ParseError:
		print("You have writen a wrong text.\nPlease try again.")
		return None
