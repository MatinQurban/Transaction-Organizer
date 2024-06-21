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
    # cred_file = "credentials.json"
    # token_file = "token.json"
    # service = connectToGoogle(token_file, cred_file, SCOPES)


    # user = service.users()
    
    # messages = getEmails(user)

    # raw_emails = getRawText(user, messages)

    # with open('emails.csv', mode='w') as email_file:
    #     email_writer = csv.DictWriter(email_file, fieldnames=['id', 'text'])
    #     email_writer.writeheader()
    #     email_writer.writerows(raw_emails)

    # TODO Create a function called getAndSaveEmails that will get the emails and save them to a csv file 

    email_information = []

    # for i in range(len(raw_emails)):
    #   info = parseEmail(raw_emails[i]['text'], messages[i]['id'], user)
    #   if info == -1:
    #     print("ID check: ")
    #     print(messages[i])
    #   else:
    #     email_information.append(info)
    # with open('email_info.csv', mode='w') as email_info_file:
    #     email_info_writer = csv.DictWriter(email_info_file, fieldnames=['Date', 'Seller', 'OrderNum', 'Total', 'EmailId'])
    #     email_info_writer.writeheader()
    #     email_info_writer.writerows(email_information)

    # Read data from the file
    with open("email_info.csv", 'r') as file:
      reader = csv.DictReader(file)
      data = [row for row in reader]


  
  except HttpError as error:
    # TODO(developer) - Handle errors from gmail API.
    print(f"An error occurred: {error}")


if __name__ == "__main__":
  main()
