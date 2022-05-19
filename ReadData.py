import re
from ClassVar import Ledger
from Util import *


def getState(line):  # get the state of the program. may be redundancy

    # ^ states that it has to be the start of the line, [0-9] is the range of the char, making what the variable says
    startWithNumbers = "^\d{4}"

    # print(Ledger.state)

    if line == "\n":
        Ledger.state = "nothing"  # null state for change o element

    # I need the next state only when a date key has been defined and the line starts with a "  " and a letter and the state is correct
    if (re.search("^  [A-Za-z]", line) or re.search("^	[A-Za-z]", line)) and Ledger.state == "accountReady":
        Ledger.state = "accountConcepts"

    # if the line starts with a number, it probably is a date, so start a movement
    if re.search(startWithNumbers, line):
        Ledger.state = "accountStarted"


def searchTax(line):
    search = r"= /^"
    if search in line:
        Ledger.taxableValue = line.split(r"/^")[1][:-2]
        taxConcept = Ledger.data.readline()
        taxConcept = taxConcept.replace(" ", "")
        taxConcept = taxConcept.replace(r"(", "")
        taxConcept = taxConcept.replace("\n", "")
        taxConcept = taxConcept.split(r")")
        Ledger.taxValue = float(taxConcept[1])
        Ledger.taxConcept = taxConcept[0] + "99"
        Ledger.taxName = taxConcept[0].split(r":")[-1]


def defineDateKey(line):
    Ledger.balanceValue = float(0)
    
    commentSplited = ""  # initialice the variable, may be redundant. to test later

    listedLine = spaceListLine(line)  # return a list separated by spaces

    if str(listedLine[0]):  # to avoid a null being listed or a function called on it
        dateKey = str(listedLine[0]) + r"(" + str(Ledger.dateCounter) + r")"

        # initialice the dictionary for the first key
        Ledger.transactionsDictionaries[dateKey] = {}

        for i in range(1, len(listedLine)):
            # append everything else on the variable adding spaces between the elements because, the spaces were removed on the split
            commentSplited += str(listedLine[i]) + " "

        # remove the last 2 elements, which always are \n and " "
        commentSplited = commentSplited[:-2]

        if not Ledger.transactionsDictionaries[dateKey]:
            # add the comment with the "comment" key to the dictionary with the datekey
            Ledger.transactionsDictionaries[dateKey] = {"comment": commentSplited}

        commentSplited = ""  # null the comment so it can be used again
        # append the date to a list to be stored in the class
        Ledger.listedDates.append(dateKey)
        Ledger.dateCounter = Ledger.dateCounter + 1
        # print for testing
        # print(dateKey)
        Ledger.state = "accountReady"  # set state ready to init the concepts

    else:  # in case that a null is listed
        print("null en: " + listedLine)
        print("estado en null: " + Ledger.state)

    Ledger.currentDateKey = dateKey


def readData():
    while True:

        line = Ledger.data.readline()  # read each line
        searchTax(line)
        # return the state of the program and execute its respective function
            
        
        getState(line)

        if Ledger.state == "accountStarted":
            defineDateKey(line)

        if Ledger.state == "accountConcepts" and (re.search("^  [A-Za-z]", line) or re.search("^	[A-Za-z]", line)):
            defineCashFlow(line)

        if not line:  # if nothing else to read: finish the program
            Ledger.data.close()
            break
    if Ledger.taxConcept != "":
        Ledger.transactionsDictionaries["Tax"] = {}
        Ledger.transactionsDictionaries["Tax"][Ledger.taxConcept] = Ledger.taxValue


def defineCashFlow(line):
    # remove all spaces from the line, to be make processing easier
    line = line.replace(" ", "")
    # return a list separated by the $ or dollar sing
    listedLine = dllListLine(line)
    # the firs element is the concept of the transaction and if there is a \n, it is removed

    concept = listedLine[0].replace("\n", "")

    if len(listedLine) > 1:

        if re.search(r";", listedLine[1]):
            listedLine2 = listedLine[1].split(r";")
            value = listedLine2[0]

        else:
            value = listedLine[1]

        value = float(value.replace("\n", "").replace(
            " ", "").replace(r",", ""))
        Ledger.balanceValue = Ledger.balanceValue - value

    else:
        value = Ledger.balanceValue
        Ledger.balanceValue = float(0)

    concept = concept + str(Ledger.conceptCounter)

    Ledger.transactionsDictionaries[Ledger.currentDateKey][concept] = value
    Ledger.conceptCounter += 1
    Ledger.listedValues.append(str(value))

    # print(Ledger.transactionsDictionaries[Ledger.currentDateKey])

