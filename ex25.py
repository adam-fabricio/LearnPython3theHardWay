"""Exercise 25 - Even More Oractice."""


def break_words(stuff):
    """This finction will brak up words for us."""
    words = stuff.split(' ')
    return words


def sort_words(words):
    """Sorts the words."""
    return sorted(words)


def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)


def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)


def sort_setence(setence):
    """Takes in a full setence and returns the sorted words."""
    words = break_words(setence)
    return sort_words(words)


def print_first_and_last(setence):
    """Print the first word and the last word of setence."""
    words = break_words(setence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(setence):
    """Sorts the words then prints the first and last one."""
    words = sort_setence(setence)
    print_first_word(words)
    print_last_word(words)
