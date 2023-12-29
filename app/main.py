from fastapi import FastAPI, HTTPException,APIRouter,Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from typing import List
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse 
import os
app = FastAPI()
os.environ['SENTENCE_TRANSFORMERS_HOME'] = './.cache' ## For Docker 
app.mount("/files/", StaticFiles(directory='../app'), name="index")
class TextInput(BaseModel):
    InputText: str # python casing??????

def emotion_detection(str1: str) -> str:
    from transformers import pipeline
    pipe = pipeline(model="distilbert-base-uncased-finetuned-sst-2-english")
    expected=(pipe(str1))
    return expected[0].get('label')    
@app.get("/")
async def read_index():
    return FileResponse('index.html')
@app.post("/generate-emotion/")
async def detect_emotion(input_data: TextInput):
    text1 = input_data.InputText
    emotion= emotion_detection(text1)
    response={"Text Entered":text1,"emotion":emotion}
    return response