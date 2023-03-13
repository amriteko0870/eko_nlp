import os
import pickle
# Gmail API utils
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
# for encoding/decoding messages in base64
from base64 import urlsafe_b64decode, urlsafe_b64encode
# for dealing with attachement MIME types
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from mimetypes import guess_type as guess_mime_type

def sendEmailFunc(send_to,send_subject,send_text):
    send_from = 'nps@ekoinfomatics.com'
    SCOPES = ['https://mail.google.com/']
    def gmail_authenticate():
        creds = None
        if os.path.exists("token.pickle"):
            with open("token.pickle", "rb") as token:
                creds = pickle.load(token)
        # if there are no (valid) credentials availablle, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('cred.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # save the credentials for the next run
            with open("token.pickle", "wb") as token:
                pickle.dump(creds, token)
        return build('gmail', 'v1', credentials=creds)

    # get the Gmail API service
    service = gmail_authenticate()
    message = MIMEMultipart('alternative')
    message['to'] = send_to
    message['from'] = send_from
    message['subject'] = send_subject
    text = """<head>
                <meta charset="UTF-8" />
                <meta http-equiv="X-UA-Compatible" content="IE=edge" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <title>Everside</title>
            </head>
                <a href="{}">{}</a>
            </html>""".format(send_text,send_text)
    mime_type = MIMEText(text, 'html')
    message.attach(mime_type)
    body = {'raw': urlsafe_b64encode(message.as_bytes()).decode()}
    sent_status = service.users().messages().send(
                                                    userId="me",
                                                    body=body
                                                    ).execute()
    if sent_status['labelIds'][0] == 'SENT':
        return True
    else:
        return False
    