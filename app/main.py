from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from app.database import test_connection
from app.routers import forms
load_dotenv()


app = FastAPI(
    title=os.getenv("API_TITLE", "KPA assignment API"),
    version=os.getenv("API_VERSION", "1.0.0"),
    description=os.getenv("API_DESCRIPTION"),
    docs_url="/docs",
    redoc_url="/redoc"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(forms.router)


@app.get("/", tags=["root"])
async def root():
    return {
        "success": True,
        "message": "welcome to KPA forms API",
        "data": {
            "title": "KPA assignment",
            "version": "1.0.0",
            "docs": "/docs",
            "redoc": "/redoc",
            "endpoints": {
                "wheel_specifications": {
                    "POST": "/api/forms/wheel-specifications",
                    "GET": "/api/forms/wheel-specifications"
                },
                "bogie_checksheet": {
                    "POST": "/api/forms/bogie-checksheet"
                },
                "health": "/api/forms/health"
            }
        }
    }



if __name__ == "__main__":
    import uvicorn

    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    debug = os.getenv("DEBUG", "true").lower() == "true"

    uvicorn.run(
        "app.main:app",
        host=host,
        port=port,
        reload=debug,
        log_level="info"
    )
