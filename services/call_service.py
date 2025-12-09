import uuid
from typing import Dict, Optional
from datetime import datetime
import asyncio

class CallService:
    """Service for managing AI calls"""
    
    def __init__(self):
        self.active_calls: Dict[str, Dict] = {}
    
    def create_call_session(self, phone_number: str, purpose: str) -> str:
        """Create a new call session"""
        call_id = f"call_{uuid.uuid4().hex[:12]}"
        
        self.active_calls[call_id] = {
            "call_id": call_id,
            "phone_number": phone_number,
            "purpose": purpose,
            "status": "initiated",
            "created_at": datetime.now().isoformat(),
            "transcript": [],
            "duration": 0
        }
        
        return call_id
    
    async def process_call(self, call_id: str):
        """
        Process the call (background task)
        Production e Twilio/Vonage API use korben
        """
        if call_id not in self.active_calls:
            return
        
        call_data = self.active_calls[call_id]
        
        try:
            # Update status to in-progress
            call_data["status"] = "in-progress"
            
            # Simulate call processing
            await asyncio.sleep(2)
            
            # Demo transcript
            call_data["transcript"] = [
                {"speaker": "AI", "text": "Hello, this is AI assistant. How can I help you?"},
                {"speaker": "User", "text": "I'd like to book an appointment."},
                {"speaker": "AI", "text": "Sure, I can help with that. What date works for you?"}
            ]
            
            # Complete the call
            call_data["status"] = "completed"
            call_data["completed_at"] = datetime.now().isoformat()
            call_data["duration"] = 120  # seconds
            
        except Exception as e:
            call_data["status"] = "failed"
            call_data["error"] = str(e)
    
    def get_call_status(self, call_id: str) -> Optional[Dict]:
        """Get status of a specific call"""
        return self.active_calls.get(call_id)
    
    def end_call(self, call_id: str) -> bool:
        """End an active call"""
        if call_id in self.active_calls:
            self.active_calls[call_id]["status"] = "ended"
            self.active_calls[call_id]["completed_at"] = datetime.now().isoformat()
            return True
        return False
    
    def get_transcript(self, call_id: str) -> Optional[list]:
        """Get transcript of a call"""
        call_data = self.active_calls.get(call_id)
        if call_data:
            return call_data.get("transcript", [])
        return None