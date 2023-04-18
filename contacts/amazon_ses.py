import boto3
from botocore.exceptions import ClientError

import configparser

class Email():
    def __init__(self, name, phone, email, subject, message):
        self.name = name
        self.phone = phone
        self.email = email
        self.subject = subject
        self.message = message

    def send(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        client = boto3.client('ses',
        region_name = config['AWS']['region'],
        aws_access_key_id = config['AWS']['access'],
        aws_secret_access_key = config['AWS']['secret_access']
        )

        SENDER = "Portfolio Messenger <user1@nhformtest1.co.uk>"
        RECIPIENT = "nathan.harris.1@outlook.com"
        CHARSET = "UTF-8"

        SUBJECT = f"New contact from {self.name} via nathanharris.co.uk"
        BODY_TEXT = ("Amazon SES Test (Python)\r\n"
                    "This email was sent with Amazon SES using the "
                    "AWS SDK for Python (Boto)."
                    )
        BODY_HTML = ("<html><head></head><body>"
        f"<h1> New 'Get in touch' from {self.name}</h1>"
        f"<p>email:  </p>"
        f"<p>number: </p>"
        f"<p>subject:  </p>"
        f"<p>message:  </p>"
        "</body></html>"
                     )

        try:
            response = client.send_email(
                Destination={
                    'ToAddresses': [
                        RECIPIENT,
                    ],
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': CHARSET,
                            'Data': BODY_HTML,
                        },
                        'Text': {
                            'Charset': CHARSET,
                            'Data': BODY_TEXT,
                        },
                    },
                    'Subject': {
                        'Charset': CHARSET,
                        'Data': SUBJECT,
                    },
                },
                Source=SENDER,
            )
        # Display an error if something goes wrong.	
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print("Email sent! Message ID:"),
            print(response['MessageId'])

if __name__ == "__main__":
    email = Email()