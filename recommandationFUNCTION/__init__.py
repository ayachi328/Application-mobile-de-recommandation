import logging
import json
import azure.functions as func


def main(req: func.HttpRequest, todoitems: func.DocumentList) -> func.HttpResponse:
    if not todoitems:
        logging.warning("ToDo item not found")
    else:
        logging.info("Found ToDo item, Description=%s",
                     len(todoitems))
                     
    result = json.dumps(todoitems[0]['articles'])
    #result = str(result)
    return func.HttpResponse(result, 
    mimetype="application/json", 
    status_code=200)
