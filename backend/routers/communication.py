from fastapi import APIRouter, HTTPException, Response, status
from fastapi.params import Form
from backend.services.communication_service import CommunicationService
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