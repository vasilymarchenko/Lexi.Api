from typing import List, Optional
from models.word import Word

class WordService:
    def __init__(self):
        # In-memory storage: dictionary mapping id -> Word
        self.words = {}
        self.next_id = 1

    def create_word(self, word: str, translation: str) -> Word:
        new_word = Word(id=self.next_id, word=word, translation=translation)
        self.words[self.next_id] = new_word
        self.next_id += 1
        return new_word

    def get_word(self, word_id: int) -> Optional[Word]:
        return self.words.get(word_id)

    def delete_word(self, word_id: int) -> bool:
        if word_id in self.words:
            del self.words[word_id]
            return True
        return False

    def list_words(self, page: int = 1, page_size: int = 20, search: Optional[str] = None) -> List[Word]:
        words_list = list(self.words.values())
        if search:
            words_list = [w for w in words_list if search.lower() in w.word.lower()]
        start = (page - 1) * page_size
        end = start + page_size
        return words_list[start:end]

# Global service instance for use in functions.
word_service_instance = WordService()
