class Ledger:  # I use this class to store global variables

    data = open('data.dat', 'r')  # the file to be readed

    # initialice this variable as a dictionary. to store everything, as a nested dictionary
    transactionsDictionaries = {}

    listedDates = []  # init this variable as a list. to store the dates

    state = ""  # init the state variable as a null string

    balanceValue = float(0)

    currentDateKey = ""

    conceptCounter = int(10)

    dateCounter = int(10)

    listedValues = []
