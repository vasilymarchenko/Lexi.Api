from pydantic import BaseModel

class Word(BaseModel):
    id: int
    word: str
    translation: str
