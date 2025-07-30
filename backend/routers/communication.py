from fastapi import APIRouter, HTTPException, Request, Response, status
from fastapi.params import Form
import urllib
from twilio.twiml.voice_response import Gather, VoiceResponse
from backend.services.communication_service import CommunicationService
from backend.schemas.communication import Message,Call


router = APIRouter(prefix="/comm", tags=["communication"])
services = CommunicationService()

@router.post("whatsapp/reply", status_code=status.HTTP_200_OK)
async def reply_to_message(Body: Message = Form(...)):
    
    if "hello" in Body.Body.lower():
        resp = services.twilio_receive_sms([f"Hello{Body.ProfileName}! How can I assist you today?"])
    elif "goodby" in Body.Body.lower():
        resp = services.twilio_receive_sms(["Have a greatday!"])
    elif "help" in Body.Bodylower():
        resp = services.twilio_receive_sms(["Hello, customer", "here's our faq page"],["localhost:8000/faq"])
    else:
        resp = services.twilio_receive_sms(["I'm not sure how to respond to that., please choose one of those texts","hello", "goodbye", "help"])
        
    return Response(content=resp, media_type="application/xml")



@router.post('/call', status_code=status.HTTP_200_OK)
async def call(request: Request):
    print(request)
    print(request.headers)
    print(f"Method: {request.method}")
    print(f"URL: {request.url}")
    # print(f"f: {From}\t {To}\n\n\n")
    # Print request headers
    print("Headers:")
    for header_name, header_value in request.headers.items():
        print(f"  {header_name}: {header_value}")
    pressed_number = Gather(num_digits=1)
    print(f"number pressed: {pressed_number}")

    resp.append(pressed_number)
    try:
        body = await request.body()
        decoded = body.decode('utf-8')
        parsed = dict(urllib.parse.parse_qsl(decoded))
        print("body:")
        for i, j in parsed.items():
            print(f"  {i}: {j}")
    except Exception as e:
        print(f"Could not read body: {e}")

    resp = VoiceResponse()
    resp.say("thanks for calling")
    resp.hangup()
    return Response(content=str(resp), media_type='text/xml')
        
@router.get("/call/start", status_code=status.HTTP_201_CREATED)
async def make_call(phone:str = "+201096905593"):
    print(f"Making call to {phone}")
    status = services.twilio_send_call(phone=phone)
    return {"status": status, "message": "Call initiated successfully."}

    