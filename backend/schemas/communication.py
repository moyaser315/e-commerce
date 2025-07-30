from pydantic import BaseModel, ConfigDict
from enum import Enum

class CallStatus(str, Enum):
    QUEUED="queued"
    RINGING = "ringing"
    INITIATED = "initiated"
    IN_PROGRESS = "in-progress"
    COMPLETED = "completed"
    FAILED = "failed"
    BUSY = "busy"
    NO_ANSWER = "no-answer"
    CANCELED = "canceled"

class Message(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    SmsMessageSid: str
    NumMedia: int
    ProfileName: str
    MessageType: str
    SmsSid: str
    WaId: str
    SmsStatus: str
    Body: str
    To: str
    NumSegments: int
    ReferralNumMedia: int
    MessageSid: str
    AccountSid: str
    ChannelMetadata: dict
    From: str
    
class Call(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    Called: str
    CallerCountry: str
    Direction: str
    CallerState: str
    CallSid: str
    To: str
    CallerZip: str
    ToCountry: str
    CallStatus: CallStatus
    From: str
    AccountSid: str
    CalledCountry: str
    CallerCity: str
    FromCountry: str
    Caller: str
    FromCity: str
    FromZip: str
    FromState: str
