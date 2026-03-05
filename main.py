import uvicorn
from fastapi import FastAPI
from src.api import router
import warnings

warnings.filterwarnings("ignore")

app = FastAPI()
app.include_router(router)

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/")
def read_root():
    return {"status": "API is running. Send POST requests to /ask."}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
