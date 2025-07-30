from fastapi import APIRouter, HTTPException, Request, Response, status
from fastapi.params import Form
import urllib
from backend.services.communication_service import CommunicationService
from twilio.twiml.voice_response import Gather, VoiceResponse
router = APIRouter(prefix="/comm", tags=["communication"])
services = CommunicationService()

@router.post("/reply", status_code=status.HTTP_200_OK)
async def reply_to_message(Body: str = Form(...), From:str = Form(...), To:str = Form(...)):
    # print("entered here")
    if "hello" in Body.lower():
        resp = services.twilio_receive_sms(["Hello! How can I assist you today?"])
    elif "goodby" in Body.lower():
        resp = services.twilio_receive_sms(["Have a greatday!"])
    elif "help" in Body.lower():
        resp = services.twilio_receive_sms(["Hello, customer", "here's our faq page"],["localhost:8000/faq"])
    else:
        resp = services.twilio_receive_sms(["I'm not sure how to respond to that., please choose one of those texts","hello", "goodbye", "help"])
        
    return Response(content=resp, media_type="application/xml")

@router.post("/support", status_code=status.HTTP_200_OK)
async def customer_support(request: Request):
    form_data = await request.form()
    event_type = form_data.get("EventType")
    
    #TODO: Make a simple LLM and convert to convos
    if event_type == "onMessageAdded":
        conversation_sid = form_data.get("ConversationSid")
        author = form_data.get("Author")
        message_body = form_data.get("Body")

        if author == "LLM":
            return {"status": "ignored"}
        if "hello" in message_body.lower():
            reply = "Hi! How can I help you?"
        elif "help" in message_body.lower():
            reply = "You can ask me about opening hours, pricing, or booking."
        else:
            reply = "Sorry, I didn’t understand that. Try 'hello' or 'help'."

        # client.conversations.conversations(conversation_sid).messages.create(
        #     author="AI Bot",
        #     body=reply
        # )

    return {"status": "ok"}


@router.post('/wp',status_code=status.HTTP_200_OK)
async def reply_wp(request: Request, Body: str = Form(...), From: str = Form(...), To: str = Form(...)):
    # print(Body)
    print(request)
    print(request.headers)
    print(f"Method: {request.method}")
    print(f"URL: {request.url}")
    # print(f"f: {From}\t {To}\n\n\n")
    # Print request headers
    print("Headers:")
    for header_name, header_value in request.headers.items():
        print(f"  {header_name}: {header_value}")

    # try:
    #     body = await request.body()
    #     decoded = body.decode('utf-8')
    #     parsed = dict(urllib.parse.parse_qsl(decoded))
    #     print("body:")
    #     for i, j in parsed.items():
    #         print(f"  {i}: {j}")
    # except Exception as e:
    #     print(f"Could not read body: {e}")
    if "hello" in Body.lower():
        resp = services.twilio_receive_sms(["Hello! How can I assist you today?"])
    elif "goodby" in Body.lower():
        resp = services.twilio_receive_sms(["Have a greatday!"])
    elif "help" in Body.lower():
        resp = services.twilio_receive_sms(["Hello, customer", "here's our faq page"],["localhost:8000/faq"])
    else:
        resp = services.twilio_receive_sms(["I'm not sure how to respond to that., please choose one of those texts","hello", "goodbye", "help"])
    
    print("\n\n\n")
    print(resp)
    # resp = MessagingResponse()
    # resp.message("The Robots are coming! Head for the hills!")

    return Response(content=resp, media_type='text/xml')

'''
Headers:
  host: 
  user-agent: TwilioProxy/1.1
  content-length: 553
  accept: */*
  content-type: application/x-www-form-urlencoded
  i-twilio-idempotency-token: 
  x-forwarded-for: 54.82.85.97
  x-forwarded-host: 
  x-forwarded-proto: https
  x-home-region: us1
  x-twilio-signature: 
  accept-encoding: gzip
body:
  SmsMessageSid: 
  NumMedia: 0
  ProfileName: Mo Yaser
  MessageType: text
  SmsSid: 
  WaId: 
  SmsStatus: received
  Body: .
  To: whatsapp:
  NumSegments: 1
  ReferralNumMedia: 0
  MessageSid: 
  AccountSid: 
  ChannelMetadata: {"type":"whatsapp","data":{"context":{"ProfileName":"Mo Yaser","WaId":""}}}
  From: whatsapp:
  ApiVersion: 2010-04-01

'''


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


'''
Headers:
  host: 
  user-agent: TwilioProxy/1.1
  content-length: 456
  accept: */*
  content-type: application/x-www-form-urlencoded; charset=UTF-8
  i-twilio-idempotency-token: 
  x-forwarded-for: 13.222.192.44
  x-forwarded-host: 
  x-forwarded-proto: https
  x-home-region: us1
  x-twilio-service-flow-event: %7B%22flow_id%22%3A%22voice_twimlverb_01k1cc4q18eqzv3r6x15fh024e%22%2C%22type%22%3A%22api_event%22%2C%22action%22%3A%22twiml_fetch%22%2C%22sub_action%22%3A%22completed%22%2C%22result%22%3A%22success%22%2C%22metadata%22%3A%7B%22transfer_type%22%3A%22call_transfer_url%22%7D%7D
  x-twilio-signature: 
  accept-encoding: gzip
number pressed: <?xml version="1.0" encoding="UTF-8"?><Gather numDigits="1" />
body:
  Called: 
  CallerCountry: US
  Direction: outbound-api
  CallerState: MN
  CallSid: 
  To: 
  CallerZip: 56091
  ToCountry: EG
  ApiVersion: 2010-04-01
  CallStatus: in-progress
  From: 
  AccountSid: 
  CalledCountry: EG
  CallerCity: WALDORF
  FromCountry: US
  Caller: 
  FromCity: WALDORF
  FromZip: 56091
  FromState: MN

'''
    