import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv('twilio.env')

def textmyself(message):
    twilio_cli = Client(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN'])
    twilio_cli.messages.create(body=message, from_=os.environ['TWILIO_NUMBER'], to=os.environ['CELL_NUMBER'])