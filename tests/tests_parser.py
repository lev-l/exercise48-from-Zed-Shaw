from nose.tools import *
from ex48 import parser

def test_SENTENCE():
	sen = parser.SENTENCE("i", "like", "you")
	assert_equal(sen.subject, "i")
	assert_equal(sen.verb, "like")
	assert_equal(sen.object, "you")

def test_peek():
	list = []
	N = parser.peek(list)
	assert_equal(N, None)
	list = [("noun", "player"), ("verb", "go"), ("direction", "north")]
	T = parser.peek(list)
	assert_equal(T, "noun")

def test_match():
	list = [("verb", "go"), ("direction", "north")]
	word = parser.match(list, "verb")
	assert_equal(word, ('verb', 'go'))

def test_verb():
	list = [("verb", "go"), ("direction", "north")]
	word = parser.parse_verb(list)
	assert_equal(word, ('verb', 'go'))
	
	list = [("noun", "player"), ("verb", "go"), ("direction", "north")]
	assert_raises(parser.ParseError, parser.parse_verb, list)

def test_object():
	list = [("stop", "to"), ("direction", "north")]
	word = parser.parse_object(list)
	assert_equal(word, ('direction', 'north'))
	
	list = [("stop", "the"), ("noun", "door")]
	word = parser.parse_object(list)
	assert_equal(word, ('noun', 'door'))
	
	list = [("verb", "go"), ("direction", "north")]
	assert_raises(parser.ParseError, parser.parse_object, list)

def test_subject():
	list = [("verb", "go"), ("stop", "to"), ("stop", "the"), ("noun", "door")]
	word = parser.parse_subject(list)
	assert_equal(word, ('noun', 'player'))
	
	list = [('noun', 'bear'), ('verb', 'eat'), ('stop', 'the'), ('noun', 'princess')]
	word = parser.parse_subject(list)
	assert_equal(word, ('noun', 'bear'))
	
	list = [("direction", "north"), ("verb", "go")]
	assert_raises(parser.ParseError, parser.parse_subject, list)

def test_sentence():
	list = [("verb", "go"), ("stop", "to"), ("stop", "the"), ("noun", "door")]
	sent = parser.return_sentence(list)
	assert_equal(sent.subject, 'player')
	assert_equal(sent.verb, 'go')
	assert_equal(sent.object, 'door')
	
	list = [("verb", "go"), ("error", "tro"), ("stop", "the"), ("noun", "door")]
	sent = parser.return_sentence(list)
	assert_equal(sent, None)
