import azure.functions as func
import json
from services.word_service import word_service_instance

def main(req: func.HttpRequest, id: str) -> func.HttpResponse:
    try:
        word_id = int(id)
    except ValueError:
        return func.HttpResponse("Invalid ID", status_code=400)

    word = word_service_instance.get_word(word_id)
    if word is None:
        return func.HttpResponse("Word not found", status_code=404)
    return func.HttpResponse(json.dumps(word.dict()), status_code=200, mimetype="application/json")
