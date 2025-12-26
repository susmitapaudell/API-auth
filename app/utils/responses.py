from fastapi import status
from fastapi.responses import JSONResponse

def error_response(message: str, status_code: int):
    return JSONResponse(
        status_code= status_code,
        content={
            "success" : False,
            "error" : message
        }
    )

def success_response(data = None, message = "Success"):
    return {
        "success" : True,
        "message" : message,
        "data" : data
    }