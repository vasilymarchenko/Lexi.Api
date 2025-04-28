import azure.functions as func
from azure.functions.decorators import FunctionApp
from functions.create_word import main as create_word_main
from functions.delete_word import main as delete_word_main
from functions.get_word import main as get_word_main
from functions.list_words import main as list_words_main

app = FunctionApp()

@app.route(route="words", methods=["POST"], auth_level=func.AuthLevel.ANONYMOUS)
def create_word(req: func.HttpRequest) -> func.HttpResponse:
    return create_word_main(req)

@app.route(route="words/{id}", methods=["DELETE"], auth_level=func.AuthLevel.ANONYMOUS)
def delete_word(req: func.HttpRequest) -> func.HttpResponse:
    # Extract 'id' from route params for the v2 programming model
    id = req.route_params.get('id')
    return delete_word_main(req, id)

@app.route(route="words/{id}", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
def get_word(req: func.HttpRequest) -> func.HttpResponse:
    id = req.route_params.get('id')
    return get_word_main(req, id)

@app.route(route="words", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
def list_words(req: func.HttpRequest) -> func.HttpResponse:
    return list_words_main(req)
