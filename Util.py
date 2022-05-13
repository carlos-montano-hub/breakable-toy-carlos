def spaceListLine(Line):
    # split the line readed into a list, taking the spaces as separators. \s may also be used but I find this way more readable
    listedLine = Line.split(" ")
    return listedLine


def dllListLine(line):
    # print(line)
    searcher = r"$"
    # split the line readed into a list, taking the "$" as separators "re.split(r"$",line)" just does not work ¯\_(ツ)_/¯
    listedLine = line.split(searcher)
    # print(listedLine)
    return listedLine

def pointsListConcept(concept):
    searcher = r":"
    listedConcept = concept.split(searcher)
    return listedConcept
