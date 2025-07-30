#TODO: Implement Twilio methods
import re
from backend.config import settings
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from twilio.twiml.voice_response import VoiceResponse
from sqlalchemy.orm import Session
class CommunicationService:
    def __init__(self):
        self.client =  Client(settings.twilio_sid, settings.twilio_auth)
        self.phone = settings.twilio_phone
        # print(self.get_failed_content())


    def get_phone_number(self, phone: str):
        return re.sub(r'[^\d+]', '', phone)

    def get_convo(self):
        self.client.conversations.conversations.get()

    def twilio_send_sms(self,msg:str, phone:str,schedule_type:str=None, time:str=None):
        message = self.client.messages.create(
            to=phone,
            from_=self.phone,
            body=msg,
            send_at=time,
            schedule_type=schedule_type
        )
        print(f"message {message.sid} status: {message.status}")
        
    def twilio_send_wp(self,msg:str, phone:str,schedule_type:str=None, time:str=None):
        message = self.client.messages.create(
            to='whatsapp:'+phone,
            from_='whatsapp:'+self.phone,
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
        
    def twilio_list_sms(self, phone:str):
        messages =self.client.messages.list(phone)
        for m in messages:
            print(f"message {m.sid} status: {m.status}")
            
            
    def get_failed_content(self, phone:str):
        messages =self.client.messages.list(phone)
        for m in messages:
            if m.status == 'failed':
                print(f"Message sid: {m.sid}\n From:{m.from_}\n To: {m.to} \n content: {m.body}\n date: {m.date_sent}")

    def twilio_mail(self):
        pass
    

    def twilio_send_call(self, phone:str):
        content = VoiceResponse()
        # print("start")
        content.say("Welcome to mo e-commerce, please enter number")
        content.redirect("https://f0c0940f2ba7.ngrok-free.app/comm/call")
        call = self.client.calls.create(to=phone,from_=self.phone,twiml=str(content))
        return call.status

    def twilio_video(self):
        pass
    

    def twilio_flex_task(self):
        pass


if __name__ == "__main__":
    comm = CommunicationService()
    # comm.twilio_send_sms("hello world")
    # comm.twilio_list_sms()
    # comm.twilio_list_sms()