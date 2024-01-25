from fastapi import FastAPI
from utils import generate_response
from pydantic import BaseModel
app = FastAPI()

class Input_Text(BaseModel):
    data: str

@app.get("/test")
async def test_endpoint(name: str ="It`s test"):
    return {"message": f"Hi, {name}!"} 

@app.post("/consult")
async def consult_endpoint(input_text: Input_Text):
    response = generate_response(f"Input: {input_text.data}")
    return {"Consult answer": response}
