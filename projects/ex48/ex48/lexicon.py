"""Exercise 48 - Advenced Input - lexicon."""

    
def scan(sentence):
    """Recebe uma palavre e retorna uma tupla com o tipo delae ela."""
    words = sentence.split(' ')
    tuples = []
    for word in words:
        tuples.append(Is_a_direction(
        Is_a_verb(
        Is_a_stop(
        Is_a_noum(
        Is_a_number(
        Error()
        ))))).check(word))
    return tuples


class Is_a_direction(object):
    """Verifica se a aplavra representa uma direcao."""

    def __init__(self, next_check):
        self.__next_check = next_check
    
    def check(self, word):
        """check if word is directions."""
        __directions = ['north', 'south', 'east', 'weast', 
                        'down', 'up', 'left','right','back']
        if word in __directions:
            return ('direction', word)
        else:
            return self.__next_check.check(word) 



class Is_a_verb(object):
    """Verifica se a palavra e um verbo."""
    
    def __init__(self, next_check):
        self.__next_check = next_check

    def check(self, word):
        """check if word is a verb."""
        __verbs = ['go', 'stop', 'kill', 'eat']

        if word in __verbs:
            return ('verb', word)
        else:
            return self.__next_check.check(word)


class Is_a_stop(object):
    """Verifica se a palavra e uma palavra de parada."""

    def __init__(self, next_check):
        self.__next_check = next_check

    def check(self, word):
        """Check if word is a stop word."""
        __stop_words = ['the', 'in', 'of', 'from', 'at', 'it']

        if word in __stop_words:
            return ('stop', word)
        else:
            return self.__next_check.check(word)



class Is_a_noum(object):
    """Verifica se e um substantivo."""

    def __init__(self, next_check):
        self.__next_check = next_check

    def check(self, word):
        """Check if word is a noum."""
        __noums = ['door', 'bear', 'princess', 'cabinet']

        if word in __noums:
            return ('noum', word)
        else:
            return self.__next_check.check(word)


class Is_a_number(object):
    """Verfica se e um numero."""

    def __init__(self, next_check):
        self.__next_check = next_check

    def check(self, word):
        try:
            return ('number', int(word))

        except ValueError:
            return self.__next_check.check(word)


class Error(object):
    """Caso nao seja os casos anteriores apresenta a tag error."""

    def check(self, word):
        return ('error', word)


