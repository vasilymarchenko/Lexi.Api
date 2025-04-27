import azure.functions as func
import json
from services.word_service import word_service_instance

def main(req: func.HttpRequest) -> func.HttpResponse:
    page = req.params.get("page")
    page_size = req.params.get("pageSize")
    search = req.params.get("search")
    
    try:
        page = int(page) if page else 1
        page_size = int(page_size) if page_size else 20
    except ValueError:
        return func.HttpResponse("Invalid paging parameters", status_code=400)

    words = word_service_instance.list_words(page=page, page_size=page_size, search=search)
    words_list = [word.dict() for word in words]
    return func.HttpResponse(json.dumps(words_list), status_code=200, mimetype="application/json")
