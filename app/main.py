from fastapi import FastAPI, HTTPException,APIRouter,Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse 
import os
from pydantic import BaseModel
from typing import List

app = FastAPI()

# uvicorn main:app --reload
# os.environ['SENTENCE_TRANSFORMERS_HOME'] = './.cache' ## For Docker 
# app.mount("/files/", StaticFiles(directory='../app'), name="index")
origins = ["*"]
    # 'http://localhost:3000'
#]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
)

def parsing(unparsed_text):                                                              # removes text that does not have a sentiment
    punctuation_chrs = "\"!,.?();:"                                                      # removing punctuation (these actually can contribute to sentiment but for our basic model we're gonna ignore them for now)
    filler_words = ["the","and","for", "with", "it's", "she","you","they","her","him","are"]   # removing preprepositional phrases 

    words = unparsed_text.split(" ")                                                     # split into individual words and remove spaces
    parsed_words = []
    for word in words:
        if word in punctuation_chrs or word in filler_words:
            pass
        elif "\n" in word:                                                               # removes newline characters
            parsed_words.append(word[2:])                                               
        elif len(word) < 3:                                                              # removes single chars and a decent amount of preprepositional phrases
            pass
        else:
            try:                                                                         # removes integers
                word = int(word)
            except ValueError:
                parsed_words.append(word)
    return parsed_words
    
def prediction(x, pos_reviews, neg_reviews):
    sentiment = None


    # Naive Bayes equation: P(c|x) = [ P(x|c) P(c) ]/ P(x)
    # x is text_inputted to Karen that has been parsed in list format 
        # for example: x = ['hello', 'today', 'great', 'day']
    # c is sentiment
        # for example: c = positive 
    # STEPS:
    # 1. Find P(x|c)
        # how many words in x are in c vocabulary (how many times they actually show up)
        # how many words in ['hello', 'today', 'great', 'day'] are in the positive vocabulary
    # 2. Find P(c)                                                                      
        # number of positive reviews in training_data / total # of reviews
        # should be a constant since number of positive reviews should be fixed
    # 3. Find P(x)
        # number of words in x that are in total vocabulary / # of total words in vocabulary
    # 4. Use Naive Bayes equation to find P(c|x)
    # 5. if P(c|x) > 0.5 the sentiment is positive, else the sentiment is negative 
    positiveWords = parsing(pos_reviews)
    negativeWords = parsing(neg_reviews)
    
    pxc = 0#words in positivitive vocabulary
    pc = 0.5 # this is true if reviewLength is used as the endpoint for both neg_reviews and pos_reviews above
    wordsinTotalVocab = 0
    for word in x:
        if word in positiveWords:
            wordsinTotalVocab += positiveWords.count(word)
        if word in negativeWords:
            wordsinTotalVocab += negativeWords.count(word)
    px = wordsinTotalVocab/(len(positiveWords)+len(negativeWords))#words in vocabulary
    for karenword in x:
       if karenword in positiveWords:
            pxc += positiveWords.count(karenword)
    pxc = pxc / len(positiveWords)
    pcx = (pxc * pc) / px

    pxc_neg = 0#words in positivitive vocabulary
    for karenword in x:
       if karenword in negativeWords:
            pxc_neg += negativeWords.count(karenword)
    pxc_neg /= len(negativeWords)
    pcx_neg = (pxc_neg * pc) / px
    
    if pxc > pxc_neg:
        sentiment = "POSITIVE!"
    else:
        sentiment = "NEGATIVE!"
    
    # NOTES:
    # in Scai I think they used logarithms in their algorithm to increase the accuracy as well as some sort of smoothing.. 
    # we should eventually implement both
    # I think it would be a good idea to make a class that encapsulates the prediction and parsing functions for elegance
    # (something that could initialize constants like P(c), pos_vocab, neg_vocab)
    # even though Sankie is an oop hater (raised eyebrow emoji) no i love it!! I LOVE OOP
    return sentiment
def sentiment_analysis(input_text):
    import nltk 
    from nltk.corpus import movie_reviews
    nltk.download('movie_reviews')
    pos_reviews = movie_reviews.raw(fileids=movie_reviews.fileids(categories='pos')[0:1150])
    neg_reviews = movie_reviews.raw(fileids=movie_reviews.fileids(categories='neg')[0:1150])
    parsed_input = parsing(input_text)
    sentiment = prediction(parsed_input, pos_reviews, neg_reviews)
    return sentiment

# def emotion_detection(str1: str) -> str:
#     return sentiment_analysis(str1)
    # from transformers import pipeline
    # pipe = pipeline(model="distilbert-base-uncased-finetuned-sst-2-english")
    # expected=(pipe(str1))
    # return expected[0].get('label')  
# @app.get("/")
# async def read_index():
#     return FileResponse('index.html')

@app.get("/testing/")
async def root(input_data):
    emotion= sentiment_analysis(input_data)
    response={"Text Entered":input_data,"emotion":emotion}
    return response

    
  
