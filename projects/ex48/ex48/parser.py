"""Exercise 49 - Making Sentences."""


class ParserError(Exception):
    """Create a error with the sentence does not make a sence."""
    pass


class Sentence_my(object):
    """A class for Sentence."""
    def __init__(self, sentence):
        self.subject = self.is_a_subject(sentence)
        self.verb = self.is_a_verb(sentence)
        self.object = self.is_a_object(sentence)

    def is_a_subject(self, list_sentence):
        """Check if in the sentence have a subject."""
        if list_sentence[0][0] == 'noun':
            return list_sentence[0][1]
        else:
            return 'player'

    def is_a_verb(self, list_sentence):
        """Check if in setence have a verb."""
        for word_type, word in list_sentence:
            if word_type == 'verb':
                return word


    def is_a_object(self, list_sentence):
        """Check if in the sentence have a object."""
        for index, sentence in enumerate(list_sentence):
            if sentence[0] == 'noun' and index != 0:
                return sentence[1]
            elif sentence[0] == 'direction':
                return sentence[1]
        return None

def parse_sentence_my(sentence):
    """Return a object with a three atribute."""
    return Sentence_my(sentence)

# Renomeado parse_sentence para parse_sentence_my
# Renomeado Sentencne para sentece_my
# Book Resolution - 




class Sentence(object):

    def __init__(self, subject, verb, obj):
        # remember we take ('noum', 'princess') and convert then.
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]

def peek(word_list):
    """Verifica se existe a lista de palavras e retorna
    O primeiro elemento da primeira tupla.
    Caso nao exista retorna None."""
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None


def match(word_list, expecting):
    """Caso a primeira tupla da lista seja o tipo esperado retorne a tupla e 
    remove a tupla da lista ou retorna None."""
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None


def skip(word_list, word_type):
    """Retorna lista de tuplas, menos as do tipo especificada."""
    while peek(word_list) == word_type:
        match(word_list, word_type)

def parse_verb(word_list):
    """Se a proxima lista de palavra for um verbo retorna a tupla ou 
    aoresenta erro de esperar que seja um verbo."""
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")

def parse_object(word_list):
    """Verifica se a proxima palavra for um objeto retorna a tupla ou
    apresenta erro."""
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")


def parse_subject(word_list):
    """Se a primeira palavra for um nome, entao ele sera o sujeito.
    Se for um verbo, entao o sujeito sera o player.
    Caso contrario dara erro."""
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player')
    else:
        raise ParserError("Expeced a verb next.")



def parse_sentence(word_list):
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subj, verb, obj)


