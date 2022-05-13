from ClassVar import Ledger


def printRegister():
    workArray = []
    workList = []
    sum = float(0)
    for date in Ledger.transactionsDictionaries:

        for concept in Ledger.transactionsDictionaries[date]:
            value = str(Ledger.transactionsDictionaries[date][concept])

            if concept == "comment":

                workList.append(date[:-4] + " " + value)

            elif concept != Ledger.taxConcept:

                if len(workList) == 0:
                    workList.append(" ")

                workList.append(concept[:-2])
                workList.append(str(value))
                sum += float(value)
                workList.append(sum)
                workArray.append(workList)
                workList = []

                if concept[:-2].split(r":")[0] == Ledger.taxableValue:
                    if len(workList) == 0:
                        workList.append(" ")
                    workList.append("(" + Ledger.taxConcept[:-2] + ")")
                    workList.append(
                        str(round(float(value) * float(Ledger.taxValue), 1)))
                    sum += float(float(value) * float(Ledger.taxValue))
                    workList.append(sum)
                    workArray.append(workList)
                    workList = []

    for row in workArray:
        print(f"{row[0]: <40} {row[1]: <35} {row[2]: >10} {row[3]: >10}")