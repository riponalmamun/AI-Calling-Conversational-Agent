from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from datetime import datetime

class Message(BaseModel):
    """Single message in conversation"""
    role: str = Field(..., description="Role: 'user' or 'assistant'")
    content: str = Field(..., description="Message content")
    timestamp: Optional[str] = None

class ConversationRequest(BaseModel):
    """Request model for conversation"""
    message: str = Field(..., description="User's message", min_length=1)
    history: Optional[List[Message]] = Field(default=[], description="Conversation history")
    context: Optional[Dict] = Field(default={}, description="Additional context")
    
    class Config:
        json_schema_extra = {
            "example": {
                "message": "Hello! Can you help me book an appointment?",
                "history": [
                    {"role": "user", "content": "Hi there"},
                    {"role": "assistant", "content": "Hello! How can I help you?"}
                ],
                "context": {"user_id": "123", "session_id": "abc"}
            }
        }

class ConversationResponse(BaseModel):
    """Response model for conversation"""
    response: str = Field(..., description="AI's response")
    intent: Optional[str] = Field(None, description="Detected intent")
    confidence: Optional[float] = Field(None, description="Confidence score")
    timestamp: str = Field(..., description="Response timestamp")
    
    class Config:
        json_schema_extra = {
            "example": {
                "response": "Of course! I'd be happy to help you book an appointment.",
                "intent": "booking_request",
                "confidence": 0.95,
                "timestamp": "2024-11-16T10:30:00"
            }
        }

class CallHistory(BaseModel):
    """Call history record"""
    call_id: str
    phone_number: str
    purpose: str
    status: str = Field(..., description="Status: initiated, in-progress, completed, failed")
    duration: Optional[int] = Field(None, description="Call duration in seconds")
    transcript: Optional[str] = None
    created_at: str
    completed_at: Optional[str] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "call_id": "call_123456",
                "phone_number": "+8801711223344",
                "purpose": "Customer support",
                "status": "completed",
                "duration": 180,
                "transcript": "Full conversation transcript...",
                "created_at": "2024-11-16T10:00:00",
                "completed_at": "2024-11-16T10:03:00"
            }
        }