import json
from typing import List, Dict, Optional
from datetime import datetime
import base64

class AIService:
    """AI Service for conversation and voice processing"""
    
    def __init__(self):
        self.system_prompt = """You are a helpful AI calling assistant. 
        You can help with appointments, customer support, and general inquiries.
        Be polite, professional, and concise in your responses."""
    
    async def generate_response(
        self, 
        user_message: str, 
        conversation_history: List[Dict] = None,
        context: Dict = None
    ) -> Dict:
        """
        Generate AI response based on user message
        Production e OpenAI/Anthropic API use korben
        """
        # Intent detection
        intent = self._detect_intent(user_message)
        
        # Simple response generation (demo purpose)
        # Production e actual API call korben
        response_text = self._generate_demo_response(user_message, intent)
        
        return {
            "text": response_text,
            "intent": intent,
            "confidence": 0.92,
            "timestamp": datetime.now().isoformat()
        }
    
    def _detect_intent(self, message: str) -> str:
        """Detect user intent from message"""
        message_lower = message.lower()
        
        if any(word in message_lower for word in ["appointment", "book", "schedule"]):
            return "booking_request"
        elif any(word in message_lower for word in ["cancel", "reschedule"]):
            return "modification_request"
        elif any(word in message_lower for word in ["help", "support", "problem"]):
            return "support_request"
        elif any(word in message_lower for word in ["hello", "hi", "hey"]):
            return "greeting"
        else:
            return "general_inquiry"
    
    def _generate_demo_response(self, message: str, intent: str) -> str:
        """Generate demo response based on intent"""
        responses = {
            "booking_request": "I'd be happy to help you book an appointment. Could you please tell me your preferred date and time?",
            "modification_request": "I can help you with that. Can you provide your booking reference number?",
            "support_request": "I'm here to help! Please describe the issue you're facing.",
            "greeting": "Hello! How can I assist you today?",
            "general_inquiry": "I understand. Let me help you with that."
        }
        return responses.get(intent, "I'm here to help. Could you please provide more details?")
    
    async def text_to_speech(self, text: str, voice: str = "alloy") -> str:
        """
        Convert text to speech
        Production e OpenAI TTS API use korben
        """
        # Demo implementation
        # Production code:
        # response = await openai.audio.speech.create(
        #     model="tts-1",
        #     voice=voice,
        #     input=text
        # )
        # return response.audio_url
        
        return f"https://api.example.com/audio/{voice}/{hash(text)}.mp3"
    
    async def speech_to_text(self, audio_data: str) -> str:
        """
        Convert speech to text
        Production e OpenAI Whisper API use korben
        """
        # Demo implementation
        # Production code:
        # audio_bytes = base64.b64decode(audio_data)
        # response = await openai.audio.transcriptions.create(
        #     model="whisper-1",
        #     file=audio_bytes
        # )
        # return response.text
        
        return "Transcribed text from audio (demo)"
    
    def analyze_sentiment(self, text: str) -> Dict:
        """Analyze sentiment of the text"""
        # Simple demo sentiment analysis
        positive_words = ["good", "great", "excellent", "happy", "thanks"]
        negative_words = ["bad", "poor", "unhappy", "problem", "issue"]
        
        text_lower = text.lower()
        positive_count = sum(1 for word in positive_words if word in text_lower)
        negative_count = sum(1 for word in negative_words if word in text_lower)
        
        if positive_count > negative_count:
            sentiment = "positive"
        elif negative_count > positive_count:
            sentiment = "negative"
        else:
            sentiment = "neutral"
        
        return {
            "sentiment": sentiment,
            "confidence": 0.85
        }