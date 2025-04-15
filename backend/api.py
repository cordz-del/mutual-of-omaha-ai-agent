from fastapi import FastAPI, Request
from nlu import interpret_query
from dialogue_manager import generate_response

app = FastAPI()

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message")
    
    intent = interpret_query(user_message)
    response = generate_response(intent, user_message)
    
    return {"response": response}
