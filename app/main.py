from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import httpx
from app.services.rag import answer_question

#I create a FastAPI app instance/application
app = FastAPI(
    title="ICT University AI chatbot",
    description="A Rag-Powered university chatbot using gemma 3 1B",
    version="1.0.0",
    contact={
        "name": "ICT University",
        "url": "https://www.ictuniversity.edu",
        "email": "info@ictuniversity.edu"
    }
)

#Thsi is to allow communication with the frontend...some how forgot this before..
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
                   "http://localhost:3000",
                   "https://127.0.0.1:3000"
                   ],  # Adjust this to your frontend's origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Defines the incomming chat request
class ChatRequest(BaseModel):
    question: str = Field(
        min_length=2, 
        max_length=2000,
        description="The user's question to the chatbot."
    )
    
# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "Welcome to the ICT University AI Chatbot API. Use the /chat endpoint to interact with the chatbot.",
        "status": "running"
    }
    
# Health check endpoint
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "message": "The ICT University AI Chatbot API is running smoothly.",
        "application": "ICT University AI Chatbot",
        "version": "1.0.0"
    }
    
# Chat endpoint
@app.post("/api/chat")
async def chat(request: ChatRequest):
    
    try:
        # Call the RAG pipeline to answer the question
        result = await answer_question(request.question)
        
        return {
            "question": request.question,
            "answer": result["answer"],
            "confidence": result["confidence"],
            "sources": result["sources"]
        }
        
    except httpx.HTTPError as error:
        raise HTTPException(
            status_code=502,
            detail=f"An error occurred while processing the request."
        ) from error
        
    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred."
        ) from error