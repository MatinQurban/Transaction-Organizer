import re

def parseEmail(raw_email: str):
    '''
    This function will parse raw text of an email and return a dictionary with the following
    keys: 'Date', 'Seller', 'OrderNum', 'Total'.
    '''
    raw_email = raw_email.upper()

    # Find the total by splitting the raw email by "TOTAL"
    total = re.split(r"\b" + re.escape("TOTAL") + r"\b", raw_email)
    total = total[1].split("$")
    # print("Total: ", total[1])
    total = total[1].split('.')
    total = total[0] + '.' + total[1][0:2]
    print(total)

    # Find the order number
    if "ORDER NUMBER" in raw_email:
        print("Order number found")
        order_num = raw_email.split("ORDER NUMBER") #re.split(r"\b" + re.escape("ORDER") + r"\b", raw_email)
    elif "ORDER NUM" in raw_email:
        print("Order num found")
        order_num = raw_email.split("ORDER NUM")
    elif "ORDER #" in raw_email:
        print("Order # found")
        order_num = raw_email.split("ORDER #")
    elif "ORDER NO" in raw_email:
        print("Order no. found")
        order_num = raw_email.split("ORDER NO")
    else:
        print("Order number not found")

    # print(order_num[1])
    order_num = re.search(r'[a-zA-Z0-9#][a-zA-Z0-9-]*', order_num[1])
    order_num = order_num.group(0)
    print(order_num)

    pass