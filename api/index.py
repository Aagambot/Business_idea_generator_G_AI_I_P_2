# import os
# from fastapi import FastAPI, Depends  # type: ignore
# from fastapi.responses import StreamingResponse  # type: ignore
# from fastapi_clerk_auth import ClerkConfig, ClerkHTTPBearer, HTTPAuthorizationCredentials  # type: ignore
# from google import genai  # type: ignore

# app = FastAPI()

# # Clerk setup
# clerk_config = ClerkConfig(jwks_url=os.getenv("CLERK_JWKS_URL"))
# clerk_guard = ClerkHTTPBearer(clerk_config)

# # Gemini client (picks up GEMINI_API_KEY from env in Vercel)
# client = genai.Client()

# @app.get("/api")
# def idea(creds: HTTPAuthorizationCredentials = Depends(clerk_guard)):
#     user_id = creds.decoded["sub"]  # User ID from JWT
#     # You can use `user_id` to track usage, save ideas, etc.

#     contents = [
#         {
#             "parts": [
#                 {
#                     "text": "Reply with a new business idea for AI Agents, formatted with headings, sub-headings and bullet points"
#                 }
#             ]
#         }
#     ]
#     # Streaming response from Gemini
#     stream = client.models.stream_generate_content(
#         model="gemini-2.5-flash",
#         contents=contents,
#     )

#     def event_stream():
#         for event in stream:
#             if event.type == "token":
#                 text = event.token
#                 if text:
#                     yield f"data: {text}\n\n"

#     return StreamingResponse(event_stream(), media_type="text/event-stream")

import os
from fastapi import FastAPI, Depends, Request
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi_clerk_auth import ClerkConfig, ClerkHTTPBearer, HTTPAuthorizationCredentials
import google.generativeai as genai

app = FastAPI()

# CORS - works for both local and Vercel
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for simplicity
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Clerk configuration
clerk_config = ClerkConfig(jwks_url=os.getenv("CLERK_JWKS_URL"))
clerk_guard = ClerkHTTPBearer(clerk_config)

# Configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

@app.get("/api")
async def idea(creds: HTTPAuthorizationCredentials = Depends(clerk_guard)):
    user_id = creds.decoded["sub"]
    
    async def event_stream():
        try:
            model = genai.GenerativeModel("gemini-2.0-flash-exp")
            response = model.generate_content(
                "Reply with a new business idea for AI Agents, formatted with headings, sub-headings and bullet points",
                stream=True
            )
            
            for chunk in response:
                if chunk.text:
                    # Send text chunks as SSE
                    text = chunk.text
                    yield f"data: {text}\n\n"
                    
        except Exception as e:
            yield f"data: Error: {str(e)}\n\n"
    
    return StreamingResponse(
        event_stream(), 
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no"  # Important for Vercel
        }
    )