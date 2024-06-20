

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

    raw_emails = getRawText(user, messages)
    

    #print("Raw emails: ", raw_emails[0])

    #parseEmail(raw_emails[0])

  except HttpError as error:
    # TODO(developer) - Handle errors from gmail API.
    print(f"An error occurred: {error}")


if __name__ == "__main__":
  main()
