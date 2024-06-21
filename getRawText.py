import base64
import re
from bs4 import BeautifulSoup


def getRawText(user, messages: list):
    raw_emails = []
    for message in messages:
        msg = user.messages().get(userId="me", id=message["id"], format='raw').execute()
        email_obj = {}
        msg_raw = msg['raw']
        headers = user.messages().get(userId="me", id=message['id'], format='full').execute()['payload']['headers']
        decoded_msg = base64.urlsafe_b64decode(msg_raw).decode('utf-8')
        # print("Decoded message: ", decoded_msg)
        
        
        for header in headers:
            if header['name'] == 'Content-Type':
                if 'text/html;' in header['value']:
                    soup = BeautifulSoup(decoded_msg, 'html.parser')
                    raw_email = soup.get_text()
                    email_obj = {'id': message['id'], 'text': repr(raw_email)}
                break
        if email_obj:
            raw_emails.append(email_obj)
            # print("Email object: ", email_obj)
            continue


        try:
            boundary = decoded_msg.split("boundary=")[1]
            boundary = boundary.split("\n")[0]
            if boundary[0] == '\"':
                boundary = boundary.split("\"")[1]
            # print("Boundary: ", boundary)

            parsed_msg = decoded_msg.split(boundary)[2]
            # print("Message decoded: ", parsed_msg)
            parsed_msg = re.sub(r'https?:\/\/.*?>', 'LINK>', parsed_msg, flags=re.DOTALL) #\/\/.*[\r\n]* # ?(?=>) # r'https?:\/\/.*?>'

            email_obj = {'id': message['id'], 'text': repr(parsed_msg)[1:-1]}
            raw_emails.append(email_obj)
        except IndexError:
            print("getRawText.py: Error parsing message, no boundary found ", message['id'])
            # print("Message: ", repr(decoded_msg))
            # print("Message: ", decoded_msg.split("Content-Transfer-Encoding")[2])
            raw_emails.append({'id': message['id'], 'text': "NO BOUNDARY FOUND - FULL MESSAGE: " + repr(decoded_msg)})
            
   
    return raw_emails
    