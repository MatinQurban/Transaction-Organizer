def getEmails(user):
    '''
    Args:
    user: str - the user to get the emails from
    service: googleapiclient.discovery.Resource - the service to use for the google api

    Returns:
    messages: list - the list of messages for the user
    '''
    results = []
    messages = user.messages()
    print("User profile: ")
    print(user.getProfile(userId="me").execute())

    search_query = "in:inbox -category:(promotions OR social) subject:Order"
    message_list = messages.list(userId="me", q=search_query).execute().get("messages", [])

    for message in message_list:
        headers = user.messages().get(userId="me", id=message["id"], format='full').execute()['payload']['headers']
        subject = [item['value'] for item in headers if item['name'] == 'Subject']
        # print("Subject: ", subject)
        if "ORDER" in subject[0].upper():
            results.append(message)
            # print("Appending")


    return results