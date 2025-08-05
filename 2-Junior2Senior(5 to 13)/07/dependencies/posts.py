from fastapi import Request, HTTPException


def check_feedback_length(request: Request):
    feedback = request.query_params["feedback"]
    if feedback == None:
        raise HTTPException(status_code=500, detail="feedback does not exist")
    if len(feedback) < 20:
        raise HTTPException(
            status_code=403, detail="length of feedback should not be lower than 20"
        )
