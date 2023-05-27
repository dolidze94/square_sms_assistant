from twilio.rest import Client
import configs

def send_sms(sms_to, sms_body):
    client = Client(configs.twilio_account_sid, configs.twilio_auth_token)
    message = client.messages.create(
        messaging_service_sid=configs.twilio_messaging_service_sid,
    body=sms_body,
    to=sms_to
    )

    print(message.sid)