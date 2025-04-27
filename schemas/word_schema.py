from pydantic import BaseModel

# Schema for creating a new word (input)
class WordCreate(BaseModel):
    word: str
    translation: str

# Schema for responding with word data
class WordResponse(BaseModel):
    id: int
    word: str
    translation: str
