
def splitWords(fileName):
    """

    :param fileName:
    :return: a set that contains different words
    """

    words = set()

    with open(fileName, "r") as fileObj:
        # count = 0
        for paragraph in fileObj:
            # count += 1
            # print(count)
            temp = paragraph.split(" ")
            for word in temp:
                word = cleanWord(word)
                if word:
                    words.add(word.lower())

    return words


def cleanWord(word):
    """

    :param word:
    :return: a clean word without irrelevant symbols
    """
    stopSymbol = (",", ":", "!", "'", '"', ".", "/", "\\", "@", "?", "\n",
                  "_", "-", "(", ")", "<", ">", "{", "}", "[", "]", ";", "*")
    left, right = 0, len(word) - 1

    while left < right and word[left] in stopSymbol:
        left += 1
    while left < right and word[right] in stopSymbol:
        right -= 1
    if left == right:
        if word[left] not in stopSymbol:
            return word[left]
        else:
            return None

    return word[left: right + 1]