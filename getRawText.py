import base64
import re


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
        parsed_msg = re.sub(r'https?:\/\/.*?>', 'LINK>', parsed_msg, flags=re.DOTALL) #\/\/.*[\r\n]* # ?(?=>) # r'https?:\/\/.*?>'
        email_obj = {'id': message['id'], 'text': parsed_msg}
        raw_emails.append(email_obj)
   
    return raw_emails
    