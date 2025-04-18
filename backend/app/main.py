# FastAPI entry point
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn as uv

from app.api.v1.routes.chat import chatRouter

def create_app() -> FastAPI:
    app = FastAPI(
        title="Swift-Trader-System",
        description="Backend of Swift-Trade",
        version="1.0.0"
    )
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
    
    app.include_router(chatRouter, prefix="/chat", tags=["chat"])
    
    return app

app = create_app()

if __name__ == "__main__":
    uv.run(
        "main:app"
    )
