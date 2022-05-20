from pydantic import BaseModel


class JournalEntry(BaseModel):
    title: str
    body: str
    date: str
    score: int
    # user_id: int
