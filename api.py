import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# السماح للفرونت يوصل للباك
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # أو حط هنا دومين الفرونت بس
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "API is running successfully 🚀"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Railway بيدي متغير بيئة اسمه PORT
    uvicorn.run("api:app", host="0.0.0.0", port=port, reload=False)
