from Balance import generateBalance
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
@click.argument("function" , type= str)
def chooseFunction(function):
    if function == "Balance":
        readData()
        generateBalance()
    if function ==  "Register":
        readData()
        printRegister()
    if function ==  "Print":
        readData()
        printAll()
    
    
if __name__ == '__main__':
    chooseFunction()



