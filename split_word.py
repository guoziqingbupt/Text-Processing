import nltk


def splitWords(fileName):
    """

    :param fileName:
    :return: a set that contains different words
    """

    words = set()

    # word rule
    patt = "[A-Za-z]\w+"

    with open(fileName, "r") as fileObj:
        for paragraph in fileObj:
            temp = nltk.RegexpTokenizer(patt).tokenize(paragraph)
            words.update(temp)
    return words