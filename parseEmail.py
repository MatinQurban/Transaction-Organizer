
def parseEmail(raw_email: str):
    '''
    This function will parse raw text of an email and return a dictionary with the following
    keys: 'Date', 'Seller', 'OrderNum', 'Total'.
    '''

    # Split the email by the word "total"
    total = raw_email.upper().split("TOTAL")
    print("Total: ", total[1])

    pass