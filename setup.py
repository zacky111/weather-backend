from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from main import router as endpoint_router

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000","https://weather-frontend-bdwz.onrender.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(endpoint_router)