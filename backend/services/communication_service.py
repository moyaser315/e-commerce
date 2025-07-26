#TODO: Implement Twilio methods
from backend.config import settings
from twilio.rest import Client
class CommunicationService:
    def __init__(self):
        self.client =  Client(settings.twilio_phone, settings.twilio_auth)
        self.phone = settings.twilio_phone

    def twilio_wp(self):
        pass
    

    def twilio_sms(self,msg:str, pnumber:str):
        message = self.client.messages.create(
            to=pnumber,
            from_=self.phone,
            body=msg
        )
        print(f"message {message.sid} status: {message.status}")
        
    def twilio_list_sms(self, pnumber:str):
        messages =self.client.messages.list(pnumber)
        for m in messages:
            print(f"message {m.sid} status: {m.status}")
    

    def twilio_mail(self):
        pass
    

    def twilio_call(self):
        pass
    

    def twilio_video(self):
        pass
    

    def twilio_flex_task(self):
        pass


if __name__ == "__main__":
    comm = CommunicationService()
    # comm.twilio_sms("testing sms")
    # comm.twilio_list_sms()