from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
from script import extract_radius

app = FastAPI()

origins = [
    "http://localhost:3000",
    "https://eos-extractor-frontend.onrender.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/get_radius")
async def get_radius(file: UploadFile, mass: float = Form(required=True)):
    try:
        radius = extract_radius(file.file, mass)
        return {"radius": round(float(radius), 2)}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})


@app.get("/")
async def main():
    return {"message": "Hello! I am working :)"}
