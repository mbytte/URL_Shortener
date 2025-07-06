import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        data = req.get_json()
        url = data.get("url")
        if not url:
            return func.HttpResponse("Please provide 'url' in the JSON body", status_code=400)
        
        # Here you would create and store your short code, simplified example:
        short_code = "abc123"
        short_url = f"https://yourdomain.com/{short_code}"
        
        return func.HttpResponse(
            json.dumps({"short_url": short_url}),
            mimetype="application/json",
            status_code=200
        )
    except Exception as e:
        return func.HttpResponse(str(e), status_code=500)
