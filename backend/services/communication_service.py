#TODO: Implement Twilio methods
from backend.config import settings
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
class CommunicationService:
    def __init__(self):
        self.client =  Client(settings.twilio_phone, settings.twilio_auth)
        self.phone = settings.twilio_phone

    def twilio_convo(self, friendly_name:str):
        #TODO: search for convos and create if not existent
        pass
    

    def twilio_send_sms(self,msg:str, pnumber:str,schedule_type:str=None, time:str=None):
        message = self.client.messages.create(
            to=pnumber,
            from_=self.phone,
            body=msg,
            send_at=time,
            schedule_type=schedule_type
        )
        print(f"message {message.sid} status: {message.status}")

    def twilio_receive_sms(self,msgs: list[str], redirect:list[str] = None, medi: dict[int, str] = None):
        response=MessagingResponse()
        for i in range(len(msgs)):
            msg = response.message(msgs[i])
            if medi and i in medi:
                msg.media(medi[i])
        if redirect:
            for r in redirect:
                response.redirect(r)
        
        return str(response)
        
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