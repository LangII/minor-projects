


paragraph = """One example would be to take this paragraph of text and return a list of alphabetized unique words. After each word tell me how many times the word appeared and in what sentance(s) the word appreared in."""



def main():

    sentences = getSentences(paragraph)
    print("\n--- SENTENCES ---")
    for sentence in sentences:  print(sentence)

    words = getWords(paragraph)
    print("\n--- WORDS ---")
    for word in words:  print(word)

    occurences = getOccurences(sentences, words)
    print("\n --- OCCURRENCES ---")
    prettyPrintOccurences(occurences)



def getSentences(_para):
    """ Get list of sentences from original paragraph. """

    return [ i.strip() for i in paragraph.split('.') if i ]

def getWords(_para):
    """ Get list of words from original paragraph. """

    _para = _para.replace('.', '')

    return set([ i.strip() for i in _para.split(' ') ])

def getOccurences(_sentences, _words):
    """
    input:  _sentences = List of sentences from getSentences().
            _words = List of words from getWords().
    output: Return occurrences_, a list of lists.  First column of nested lists is each word from
            words, proceeding columns are occurences of preceeded word within each sentence.
    """

    occurrences_ = []
    for word in _words:
        line = [word]
        for i, sentence in enumerate(_sentences):
            count = 0
            for separate in sentence.split(' '):
                if word == separate:  count += 1
            line += [count]
        occurrences_ += [line]

    return occurrences_

def prettyPrintOccurences(_occurences):
    """ Print occurences in easier to read format. """

    for occur in _occurences:
        for o in occur:  print(str(o).ljust(16), end="")
        print("")



main()
