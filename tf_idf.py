from split_word import cleanWord
import os
import math


def fre_count(fileName):
    """

    :param fileName:
    :return: a dictionary, key is word, value is it's term frequency

    """

    stopWords = []
    with open("stop_words.txt", "r") as fileObj:
        for stopWord in fileObj:
            stopWords.append(stopWord[:-1])

    result = {}

    with open(fileName, "r") as fileObj:
        for paragraph in fileObj:
            temp = paragraph.split(" ")
            for word in temp:
                word = cleanWord(word)
                if word and word not in stopWords:
                    word = word.lower()
                    if word not in result:
                        result[word] = 1
                    else:
                        result[word] += 1

    return result


def tf(fileName):
    """

    :param fileName:
    :return: a dictionary without order

    * key: word
    * value: tf weight factor

    """

    result = fre_count(fileName)
    max_fre = max(result.values())

    for key in result:
        result[key] = 0.4 + 0.6 * result[key]/max_fre

    return result


def weightGen(fileSetName):
    """

    :param fileSetName:
    :return: a dictionary that denotes weight info

    * idf: a dictionary as {keyword1: idf1, keyword2: idf2, ....}
    * tfi: a dictionary denotes document i, show as {keyword1: tf1, keyword2: tf2, ....}
    * weight: weight info of whole file set
        ** key: fileName
        ** value: a dictionary show as weight info of keywords
            *** form: {keyword1: tfi[keyword1] * idf[keyword1], ....}

    """

    fileList = os.listdir(fileSetName)[1:]
    idf = {}
    N = len(fileList)
    weight = {}

    # after 2 rounds iteration, we get document frequency, but not be inversed
    for fileName in fileList:
        tfi = tf(fileSetName + "/" + fileName)
        weight[fileName] = tfi
        for keyword in tfi:
            if keyword not in idf:
                idf[keyword] = 1
            else:
                idf[keyword] += 1

    # get inversed document frequency
    for keyword in idf:
        idf[keyword] = math.log((N / idf[keyword]), math.e)

    for fileName in weight:
        for keyword in weight[fileName]:
            # tf * idf
            weight[fileName][keyword] *= idf[keyword]

    return weight