from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI(title="Student Management API", version="1.0.0")

@app.get("/")
async def read_root():
    return JSONResponse(content={"message": "Welcome to the Student Management API"})

if __name__ == "__main__":
    # Start the FastAPI application with host and port configuration
    uvicorn.run(app, host="0.0.0.0", port=8000)