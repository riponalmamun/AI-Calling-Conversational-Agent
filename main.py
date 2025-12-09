from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from datetime import datetime
import uvicorn

# Models import
from models.conversation import ConversationRequest, ConversationResponse, CallHistory
from services.ai_service import AIService
from services.call_service import CallService

app = FastAPI(
    title="AI Calling / Conversational Agent API",
    description="AI-powered calling and conversational agent with voice capabilities",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
ai_service = AIService()
call_service = CallService()

# In-memory storage (production e database use korben)
call_history: List[CallHistory] = []

@app.get("/", tags=["Root"])
async def root():
    """Root endpoint - API status check"""
    return {
        "message": "AI Calling Agent API",
        "status": "active",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.post("/api/v1/conversation", response_model=ConversationResponse, tags=["Conversation"])
async def create_conversation(request: ConversationRequest):
    """
    AI conversation endpoint - Text-based interaction
    """
    try:
        response = await ai_service.generate_response(
            user_message=request.message,
            conversation_history=request.history,
            context=request.context
        )
        
        return ConversationResponse(
            response=response["text"],
            intent=response.get("intent"),
            confidence=response.get("confidence", 0.95),
            timestamp=datetime.now().isoformat()
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Conversation error: {str(e)}")

@app.post("/api/v1/call/initiate", tags=["Call"])
async def initiate_call(
    phone_number: str = Field(..., description="Phone number to call"),
    purpose: str = Field(..., description="Purpose of the call"),
    background_tasks: BackgroundTasks = None
):
    """
    Initiate an AI-powered call
    """
    try:
        call_id = call_service.create_call_session(phone_number, purpose)
        
        # Background task e call process korben
        if background_tasks:
            background_tasks.add_task(call_service.process_call, call_id)
        
        return {
            "call_id": call_id,
            "status": "initiated",
            "phone_number": phone_number,
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Call initiation error: {str(e)}")

@app.get("/api/v1/call/{call_id}", tags=["Call"])
async def get_call_status(call_id: str):
    """
    Get status of a specific call
    """
    call_data = call_service.get_call_status(call_id)
    if not call_data:
        raise HTTPException(status_code=404, detail="Call not found")
    return call_data

@app.get("/api/v1/history", response_model=List[CallHistory], tags=["History"])
async def get_call_history(limit: int = 10):
    """
    Get call history (recent calls)
    """
    return call_history[-limit:]

@app.post("/api/v1/voice/text-to-speech", tags=["Voice"])
async def text_to_speech(
    text: str = Field(..., description="Text to convert to speech"),
    voice: str = Field(default="alloy", description="Voice type")
):
    """
    Convert text to speech
    """
    try:
        audio_url = await ai_service.text_to_speech(text, voice)
        return {
            "audio_url": audio_url,
            "text": text,
            "voice": voice
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"TTS error: {str(e)}")

@app.post("/api/v1/voice/speech-to-text", tags=["Voice"])
async def speech_to_text(audio_data: str = Field(..., description="Base64 encoded audio")):
    """
    Convert speech to text
    """
    try:
        text = await ai_service.speech_to_text(audio_data)
        return {
            "text": text,
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"STT error: {str(e)}")

@app.get("/health", tags=["Health"])
async def health_check():
    """
    Health check endpoint
    """
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "services": {
            "ai_service": "active",
            "call_service": "active"
        }
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)