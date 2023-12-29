from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
app = FastAPI()

class TextInput(BaseModel):
    InputText: str # python casing??????

def emotion_detection(str1: str) -> str:
    from transformers import pipeline
    pipe = pipeline(model="distilbert-base-uncased-finetuned-sst-2-english")
    expected=(pipe(str1))
    return expected[0].get('label')    

@app.post("/generate-emotion/")
async def detect_emotion(input_data: TextInput):
    text1 = input_data.InputText
    emotion= emotion_detection(text1)
    response={"Text Entered":text1,"emotion":emotion}
    return response