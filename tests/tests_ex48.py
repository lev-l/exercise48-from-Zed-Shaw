from nose.tools import *
from ex48 import lexicon, parser


def test_directions():
	assert_equal(lexicon.scan("north"), [('direction', 'north')])
	result = lexicon.scan("north south east")
	assert_equal(result, [('direction', 'north'),
						('direction', 'south'),
						('direction', 'east')])
	result = lexicon.scan("west down up left right back foward")
	assert_equal(result, [('direction', 'west'),
						('direction', 'down'),
						('direction', 'up'),
						('direction', 'left'),
						('direction', 'right'),
						('direction', 'back'),
						('direction', 'foward')])

def test_verbs():
	assert_equal(lexicon.scan("go"), [('verb', 'go')])
	result = lexicon.scan("Go kill eat stop run open")
	assert_equal(result, [('verb', 'go'),
						('verb', 'kill'),
						('verb', 'eat'),
						('verb', 'stop'),
						('verb', 'run'),
						('verb', 'open')])


def test_stops():
	assert_equal(lexicon.scan("the"), [('stop', 'the')])
	result = lexicon.scan("The in of from at it to")
	assert_equal(result, [('stop', 'the'),
						('stop', 'in'),
						('stop', 'of'),
						('stop', 'from'),
						('stop', 'at'),
						('stop', 'it'),
						('stop', 'to')])


def test_nouns():
	assert_equal(lexicon.scan("bear"), [('noun', 'bear')])
	result = lexicon.scan("Bear princess door cabinet i")
	assert_equal(result, [('noun', 'bear'),
						('noun', 'princess'),
						('noun', 'door'),
						('noun', 'cabinet'),
						('noun', 'i')])

def test_numbers():
	assert_equal(lexicon.scan("1234"), [('number', 1234)])
	result = lexicon.scan("3 91234 13 56")
	assert_equal(result, [('number', 3),
						('number', 91234),
						('number', 13),
						('number', 56)])


def test_errors():
	assert_equal(lexicon.scan("ASDFADFASDF"),
					[('error', 'asdfadfasdf')])
	result = lexicon.scan("bear IAS princess")
	assert_equal(result, [('noun', 'bear'),
						('error', 'ias'),
						('noun', 'princess')])

def test_sentence():
	result = lexicon.scan("Bear open the door to the cabinet ,adf")
	assert_equal(result,[('noun', 'bear'),
					('verb', 'open'),
					('stop', 'the'),
					('noun', 'door'),
					('stop', 'to'),
					('stop', 'the'),
					('noun', 'cabinet'),
					('error', ',adf')])
	
	sentence = parser.return_sentence(result)
	assert_equal(sentence.subject, "bear")
	assert_equal(sentence.verb, "open")
	assert_equal(sentence.object, "door")
	
	result = lexicon.scan('open the door')
	sentence = parser.return_sentence(result)
	assert_equal(sentence.subject, "player")
	assert_equal(sentence.verb, "open")
	assert_equal(sentence.object, "door")
	
	result = lexicon.scan('go north')
	sentence = parser.return_sentence(result)
	assert_equal(sentence.subject, "player")
	assert_equal(sentence.verb, "go")
	assert_equal(sentence.object, "north")
	
	result = lexicon.scan('Kill bear')
	sentence = parser.return_sentence(result)
	assert_equal(sentence.subject, "player")
	assert_equal(sentence.verb, "kill")
	assert_equal(sentence.object, "bear")
