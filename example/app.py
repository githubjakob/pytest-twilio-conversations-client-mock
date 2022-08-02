from twilio.rest import Client

account_sid = ""
auth_token = ""

twilio_client = Client(account_sid, auth_token)


def create_a_twilio_conversation():
    return twilio_client.conversations.v1.conversations.create()
