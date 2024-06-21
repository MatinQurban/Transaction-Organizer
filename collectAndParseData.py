from getEmails import getEmails
from getRawText import getRawText
from parseEmail import parseEmail

def collectAndParseData(service):
    """
    Args:
    service: googleapiclient.discovery.Resource - the service to use for the google api

    Returns:
    email_information: list - the list of email information
    """
    user = service.users()
    
    messages = getEmails(user)
    
    raw_emails = getRawText(user, messages)

    email_information = []
    for i in range(len(raw_emails)):
        info = parseEmail(raw_emails[i]['text'], messages[i]['id'], user)
        if info == -1:
            print("ID check: ")
            print(messages[i])
        else:
            email_information.append(info)
    with open('email_info.csv', mode='w') as email_info_file:
        email_info_writer = csv.DictWriter(email_info_file, fieldnames=['Date', 'Seller', 'OrderNum', 'Total', 'EmailId'])
        email_info_writer.writeheader()
        email_info_writer.writerows(email_information)
    return email_information