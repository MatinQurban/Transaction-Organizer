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

    #print("Raw emails: ", raw_emails[0])

    for email in raw_emails:
      if email['id'] == '18d81ca9f1bc2cfa':
        print(email['text'])


    parseEmail(raw_emails[15]['text'], messages[15]['id'], user)

  except HttpError as error:
    # TODO(developer) - Handle errors from gmail API.
    print(f"An error occurred: {error}")


if __name__ == "__main__":
  main()
