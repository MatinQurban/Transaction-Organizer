import base64


def getRawText(user, messages: list):
    
    raw_emails = []
    for message in messages:
        msg_raw = user.messages().get(userId="me", id=message["id"], format='raw').execute()['raw']
        decoded_msg = base64.urlsafe_b64decode(msg_raw).decode('utf-8')
        
        boundary = decoded_msg.split("boundary=\"")[1]
        boundary = boundary.split("\"")[0]
        #print("Boundary: ", boundary)
        parsed_msg = decoded_msg.split(boundary)[2]
        #print("Message decoded: ", parsed_msg) #['payload']['parts']
        
        raw_emails.append(parsed_msg)
   
    return raw_emails
    