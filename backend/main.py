from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

load_dotenv()

# Verificar que la API key esté configurada
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY no está configurada en el archivo .env")

app = FastAPI(title="AI Document Reader API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configurar Gemini con la API key
genai.configure(api_key=api_key)
print(f"✅ Gemini configurado con API key: {api_key[:10]}...")

class ChatMessage(BaseModel):
    message: str
    conversation_history: list = []

@app.get("/")
async def root():
    return {"message": "AI Document Reader API is running"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.get("/test-gemini")
async def test_gemini():
    try:
        model = genai.GenerativeModel('gemini-2.0-flash')
        response = model.generate_content("Di 'Hola, funciono correctamente' en español")
        return {
            "status": "success",
            "message": "Gemini está funcionando correctamente",
            "response": response.text
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

@app.post("/chat")
async def chat_with_ai(chat_data: ChatMessage):
    try:
        model = genai.GenerativeModel('gemini-2.0-flash')
        
        conversation_context = ""
        for msg in chat_data.conversation_history:
            conversation_context += f"User: {msg.get('user', '')}\nAssistant: {msg.get('assistant', '')}\n"
        
        full_prompt = f"{conversation_context}User: {chat_data.message}\nAssistant:"
        
        response = model.generate_content(full_prompt)
        
        return {
            "response": response.text,
            "status": "success"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/chat/stream")
async def chat_stream(chat_data: ChatMessage):
    try:
        model = genai.GenerativeModel('gemini-2.0-flash')
        
        conversation_context = ""
        for msg in chat_data.conversation_history:
            conversation_context += f"User: {msg.get('user', '')}\nAssistant: {msg.get('assistant', '')}\n"
        
        full_prompt = f"{conversation_context}User: {chat_data.message}\nAssistant:"
        
        def generate_response():
            try:
                response = model.generate_content(full_prompt, stream=True)
                for chunk in response:
                    if chunk.text:
                        data = {
                            "content": chunk.text,
                            "done": False
                        }
                        yield f"data: {json.dumps(data)}\n\n"
                
                final_data = {"content": "", "done": True}
                yield f"data: {json.dumps(final_data)}\n\n"
            except Exception as e:
                error_data = {"error": str(e), "done": True}
                yield f"data: {json.dumps(error_data)}\n\n"
        
        return StreamingResponse(
            generate_response(),
            media_type="text/plain",
            headers={
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "Content-Type": "text/event-stream",
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)