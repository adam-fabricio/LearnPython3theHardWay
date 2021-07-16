"""Exercise 49 test."""


from nose.tools import *
from ex48 import lexicon, parser


def test_parser():
    sentence_list = lexicon.scan("run north")
    sentence = parser.parse_sentence(sentence_list)
    result = [sentence.subject, sentence.verb, sentence.object]
    assert_equal(result, ['player', 'run', 'north'])

    sentence_list = lexicon.scan("bear eat the honey")
    sentence = parser.parse_sentence(sentence_list)
    result = [sentence.subject, sentence.verb, sentence.object]
    assert_equal(result, ['bear', 'eat', 'honey'])


