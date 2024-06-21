import csv

from connectToGoogle import connectToGoogle
from parseEmail import parseEmail
from getEmails import getEmails
from getRawText import getRawText
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


def main():
  """
  Shows basic usage of the Gmail API.
  Lists the user's Gmail labels.
  """
  try:
    # Call the Gmail API
    service = connectToGoogle("token.json", "credentials.json", SCOPES)
    user = service.users()
    
    messages = getEmails(user)
    # for item in header:
    #     if item['name'] == 'Date':
    #        date = item['value']
    print(len(messages))
    
    # seller = user.messages().get(userId="me", id=messages[0]['id'], format='full').execute()['payload']['headers']
    # print(seller)

    raw_emails = getRawText(user, messages)


    # with open('emails.csv', mode='w') as email_file:
    #     email_writer = csv.DictWriter(email_file, fieldnames=['id', 'text'])
    #     email_writer.writeheader()
    #     email_writer.writerows(raw_emails)

    # TODO Create a function called getAndSaveEmails that will get the emails and save them to a csv file 
    # print("Raw emails: ", raw_emails[0])

    # print(raw_emails[15]['id'])
    # print(messages[15])

    # trouble_id = '18d81ca9f1bc2cfa'
    # for message in raw_emails:
    #   if message['id'] == trouble_id:
    #     parseEmail(message['text'], trouble_id, user)
    #     break


    email_information = []
    for i in range(len(raw_emails)):
      info = parseEmail(raw_emails[i]['text'], messages[i]['id'], user)
      if info == -1:
        print("Error parsing email")
        print(messages[i])
      else:
        email_information.append(info)
    with open('email_info.csv', mode='w') as email_info_file:
        email_info_writer = csv.DictWriter(email_info_file, fieldnames=['Date', 'Seller', 'OrderNum', 'Total', 'EmailId'])
        email_info_writer.writeheader()
        email_info_writer.writerows(email_information)

  
  except HttpError as error:
    # TODO(developer) - Handle errors from gmail API.
    print(f"An error occurred: {error}")


if __name__ == "__main__":
  main()
