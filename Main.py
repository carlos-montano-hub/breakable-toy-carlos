from Balance import generateBalance
from FileRead import FileRead
from Print import printAll
from ReadData import readData
from Util import *
from ClassVar import *
from Register import *
import click


def printAllRawData():
    for date in Ledger.transactionsDictionaries:
        print(date)
        for concept in Ledger.transactionsDictionaries[date]:
            print(concept, Ledger.transactionsDictionaries[date][concept])


@click.command()
@click.argument("function", type=str)
@click.option("-f", "--file", default="data.dat")
def chooseFunction(function, file):

    if function == "Balance":
        FileRead(file)
        readData()
        generateBalance()

    if function == "Register" or function == "Reg":
        FileRead(file)
        readData()
        printRegister()

    if function == "Print":
        FileRead(file)
        readData()
        printAll()


if __name__ == '__main__':
    chooseFunction()
