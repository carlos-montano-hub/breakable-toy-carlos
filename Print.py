from xml.etree.ElementTree import Comment
from ClassVar import Ledger


def printAll():
    workList = []
    workArray = []

    for date in Ledger.transactionsDictionaries:
        for concept in Ledger.transactionsDictionaries[date]:
            value = Ledger.transactionsDictionaries[date][concept]

            if concept == "comment":

                workList.append("\n" + date[:-4] + " " + value)
                workList.append(" ")
                workArray.append(workList)
                workList = []

            elif concept != Ledger.taxConcept:

                workList.append("  " + concept[:-2])
                workList.append(r"$" + str(value))
                workArray.append(workList)
                workList = []

    for row in workArray:
        print(f"{row[0]: <35} {row[1]: >10}")
