"""Exercise 48 - Advenced Input - Unit test for lexicon."""


from nose.tools import *
from ex48 import lexicon

def test_directions():
    assert_equal(lexicon.scan("north"), [('direction', 'north')])

