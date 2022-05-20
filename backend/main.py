from model import JournalEntry
from database import (
    fetch_all_entries,
    fetch_entry,
    create_entry,
)
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from transformers import pipeline
import uvicorn

nlp = pipeline(task='sentiment-analysis',
               model='nlptown/bert-base-multilingual-uncased-sentiment')

app = FastAPI()


origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.get('/')
# def index():
#     response = await fetch_all_entries()
#     return {"Hello": "World"}


@app.get('/entry/{title}')
async def get_entry(title):
    response = await fetch_entry(title)
    if response:
        return response
    raise HTTPException(404, "Entry not found")


@app.post('/entry', response_model=JournalEntry)
async def post_entry(entry: JournalEntry):
    response = await create_entry(entry.dict())
    if response:
        return response
    raise HTTPException(400, "Entry not created")


@app.post('/sentiment/{text}')
async def get_sentiment(text: str):
    return analyze_sentiment(text)


def analyze_sentiment(text):
    result = nlp(text)

    print(result)

    sent = ''
    if (result[0]['label'] == '1 star'):
        sent = 'very negative'
    elif (result[0]['label'] == '2 star'):
        sent = 'negative'
    elif (result[0]['label'] == '3 stars'):
        sent = 'neutral'
    elif (result[0]['label'] == '4 stars'):
        sent = 'positive'
    else:
        sent = 'very positive'

    prob = result[0]['score']

    # Format and return results
    return {'sentiment': sent, 'probability': prob}
# @app.get('/api/journal/{id}')
# async def get_journal()


if __name__ == '__main__':
    uvicorn.run(app)
