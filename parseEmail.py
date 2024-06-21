import re
from bs4 import BeautifulSoup

def parseEmail(raw_email: str, email_id: str, user):
    '''
    This function will parse raw text of an email and return a dictionary with the following
    keys: 'Date', 'Seller', 'OrderNum', 'Total'.
    '''
    raw_email = raw_email.upper()
    headers = user.messages().get(userId="me", id=email_id, format='full').execute()['payload']['headers']

    for header in headers:
        if header['name'] == 'Content-Type':
            if header['value'] == 'text/html; charset="UTF-8"':
                soup = BeautifulSoup(raw_email, 'html.parser')
                raw_email = soup.get_text
            break
    # Find the total by splitting the raw email by "TOTAL"
    try:
        total = re.split(r"\b" + re.escape("TOTAL") + r"\b", raw_email)
        total = total[1].split("$")
        # print("Total: ", total[1])
        total = total[1].split('.')
        total = total[0] + '.' + total[1][0:2]
        print(total)
    except IndexError:
        print("Error finding total")
        total = -1

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
        print("Error finding order number")
        return -1

    # print(order_num[1])
    order_num = re.search(r'(?<!\\)[a-zA-Z0-9#][a-zA-Z0-9-]*', order_num[1])
    order_num = order_num.group(0)
    print(order_num)


    # Find the date
    date = headers[1]['value'].split(";")[-1].strip()
    print(date)

    # Find the seller
    if "FORWARDED MESSAGE" in raw_email:
        seller = raw_email.split("FROM:")[1].split("\n")[0].strip()
    else:
        for header in headers:
            if header['name'] == 'From':
                seller = header['value']
                break

    print(seller)


    pass