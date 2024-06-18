def getEmails(user):
    '''
    Args:
    user: str - the user to get the emails from
    service: googleapiclient.discovery.Resource - the service to use for the google api

    Returns:
    messages: list - the list of messages for the user
    '''
    messages = user.messages()
    print("User profile: ")
    print(user.getProfile(userId="me").execute())
    
    message_list = messages.list(userId="me").execute().get("messages", [])

    return message_list