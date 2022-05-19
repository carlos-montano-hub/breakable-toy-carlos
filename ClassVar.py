class Ledger:  # I use this class to store global variables

    data = open('ledger-sample-files/Income.ledger', 'r')  # the file to be readed

    # initialice this variable as a dictionary. to store everything, as a nested dictionary
    transactionsDictionaries = {}

    listedDates = []  # init this variable as a list. to store the dates

    state = ""  # init the state variable as a null string

    balanceValue = float(0)

    currentDateKey = ""
    currentComment = ""

    conceptCounter = int(10)

    dateCounter = int(10)

    listedValues = []
    
    taxableValue = "" #usually income
    taxName = ""  #usually tithe
    taxConcept = "" #usually liabilities:tithe
    taxValue = float(0) #percentage ussually .12

    path = ""