from curses.ascii import NUL
import importlib
import re
from Balance import generateBalance
from ReadData import readData
from Util import *
from ClassVar import *


def printAllRawData():
    for date in Ledger.transactionsDictionaries:
        print(date)
        for concept in Ledger.transactionsDictionaries[date]:
            print(concept, Ledger.transactionsDictionaries[date][concept])


readData()
# print(Ledger.transactionsDictionaries)
generateBalance()
