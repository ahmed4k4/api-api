from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# السماح للفرونت يتواصل مع الباك
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ممكن تحدد ["http://127.0.0.1:5500"] بدل *
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# استقبال JSON والرد عليه
@app.post("/receive")
async def receive_data(request: Request):
    data = await request.json()
    return JSONResponse(content={"status": "success", "received": data})

# إرسال JSON
@app.get("/send")
async def send_data():
    json_data = {"message": "Hello from Python backend", "value": 123}
    return JSONResponse(content=json_data)


if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)
