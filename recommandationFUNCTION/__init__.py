import logging
import json
import azure.functions as func


def main(req: func.HttpRequest, recommendationDOCUMENT: func.DocumentList) -> func.HttpResponse:
    if not recommendationDOCUMENT:
        logging.warning("ToDo item not found")
    else:
        logging.info("Found ToDo item, Description=%s",
                     len(recommendationDOCUMENT))
                     
    result = json.dumps(recommendationDOCUMENT[0]['articles'])
    #result = str(result)
    return func.HttpResponse(result, 
    mimetype="application/json", 
    status_code=200)
