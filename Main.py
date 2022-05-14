from Balance import generateBalance
from Print import printAll
from ReadData import readData
from Util import *
from ClassVar import *
from Register import *


def printAllRawData():
    for date in Ledger.transactionsDictionaries:
        print(date)
        for concept in Ledger.transactionsDictionaries[date]:
            print(concept, Ledger.transactionsDictionaries[date][concept])


readData()
generateBalance()
printRegister()
printAll()