"""Exercise 48 - Advenced Input - Unit test for lexicon."""


from nose.tools import *
from ex48 import lexicon

def test_directions():
    assert_equal(lexicon.scan("north"), [('direction', 'north')])
    result = lexicon.scan("north south east")
    assert_equal(result, [('direction', 'north'),
                         ('direction', 'south'),
                         ('direction', 'east')])


def test_verbs():
    assert_equal(lexicon.scan("go"), [('verb', 'go')])
    result = lexicon.scan("go kill eat")
    assert_equal(result, [('verb', 'go'),
                          ('verb', 'kill'),
                          ('verb', 'eat')])


def test_stops():
    assert_equal(lexicon.scan("the"), [('stop', 'the')])
    result = lexicon.scan("the in of")
    assert_equal(result, [('stop', 'the'),
                          ('stop', 'in'),
                          ('stop', 'of')])


def test_nouns():
    assert_equal(lexicon.scan("bear"), [('noun', 'bear')])
    result = lexicon.scan("bear princess")
    assert_equal(result, [('noun', 'bear'),
                          ('noun', 'princess')])


def test_numbers():
    assert_equal(lexicon.scan("1234"), [('number', 1234)])
    result = lexicon.scan("3 91234")
    assert_equal(result, [('number', 3),
                          ('number', 91234)])


def test_errors():
    assert_equal(lexicon.scan("adfafdsafdas"), [('error', 'adfafdsafdas')])
    result = lexicon.scan("bear IAS princess")
    assert_equal(result, [('noun', 'bear'),
                          ('error', 'IAS'),
                          ('noun', 'princess')])

def test_sentence():
    sentence1 = lexicon.scan("open door")
    sentence2 = lexicon.scan("open the door")
    sentence3 = lexicon.scan("go THROUGH the door")
    sentence4 = lexicon.scan("punch bear")
    sentence5 = lexicon.scan("Punch the Bear in the FACE")
    sentence6 = lexicon.scan("run north")

    assert_equal(sentence1, [('verb', 'open'),
                             ('noun', 'door')])
    assert_equal(sentence2, [('verb', 'open'),
                             ('stop', 'the'),
                             ('noun', 'door')])
    assert_equal(sentence3, [('verb', 'go'),
                             ('error', 'THROUGH'),
                             ('stop', 'the'),
                             ('noun', 'door')])
    assert_equal(sentence4, [('verb', 'punch'),
                            ('noun', 'bear')])
    assert_equal(sentence5, [('verb', 'Punch'),
                             ('stop', 'the'),
                             ('noun', 'Bear'),
                             ('stop', 'in'),
                             ('stop', 'the'),
                             ('noun', 'FACE')])
    assert_equal(sentence6, [('verb', 'run'),
                             ('direction', 'north')])
