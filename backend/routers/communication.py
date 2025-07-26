from fastapi import APIRouter, HTTPException, Request, Response, status
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