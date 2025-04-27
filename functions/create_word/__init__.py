import azure.functions as func
import json
from schemas.word_schema import WordCreate
from services.word_service import word_service_instance

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse("Invalid JSON body", status_code=400)

    try:
        word_create = WordCreate(**req_body)
    except Exception as e:
        return func.HttpResponse(f"Invalid request data: {str(e)}", status_code=400)

    new_word = word_service_instance.create_word(word_create.word, word_create.translation)
    response = new_word.dict()
    return func.HttpResponse(json.dumps(response), status_code=201, mimetype="application/json")
