from fastapi import FastAPI, HTTPException,APIRouter,Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse 
import os
from pydantic import BaseModel
from typing import List
app = FastAPI()
# os.environ['SENTENCE_TRANSFORMERS_HOME'] = './.cache' ## For Docker 
# app.mount("/files/", StaticFiles(directory='../app'), name="index")
origins = ["*"]
    # 'http://localhost:3000'
#]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
)
# class TextInput(BaseModel):
#     InputText: str 

def emotion_detection(str1: str) -> str:
    from transformers import pipeline
    pipe = pipeline(model="distilbert-base-uncased-finetuned-sst-2-english")
    expected=(pipe(str1))
    return expected[0].get('label')  
# @app.get("/")
# async def read_index():
#     return FileResponse('index.html')

@app.get("/testing/")
async def root(input_data):
    emotion= emotion_detection(input_data)
    response={"Text Entered":input_data,"emotion":emotion}
    return response

    
  
