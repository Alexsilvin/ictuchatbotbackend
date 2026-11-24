from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#this is the fastapi application here!!!
app = FastAPI(
    title="ICT University AI Chatbot",
    description="A university chatbot powered by RAG and gemma3:1b",
    version = "1.0.0"
)

#This one connect the next.js frontedn with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins  = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get("/")
async def root():
    return {
        "message": "Welcome to the ICT University AI Chatbot API. This API is designed to provide intelligent responses to user queries using advanced AI techniques. You can interact with the chatbot by sending requests to the appropriate endpoints.",
        "status": "running"
    }
    
@app.get("/health")
async def health():
    return {
        "message": "The ICT University AI Chatbot API is healthy and operational.",
        "status": "healthy",
        "application": "ICTU Chatbot"
    }