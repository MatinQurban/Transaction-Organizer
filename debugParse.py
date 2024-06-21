from parseEmail import parseEmail


def debugParse(raw_emails: list, email_id: str, user):
    for message in raw_emails:
        if message['id'] == email_id:
            parseEmail(message['text'], email_id, user)
            break
    return